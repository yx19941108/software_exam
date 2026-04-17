#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import time
import os
import re
import sys
import urllib.parse
from html import unescape
from pathlib import Path
from typing import Dict, Iterable, List

import requests


USER_AGENT = "Mozilla/5.0"
LOGIN_PAGE = (
    "https://wangxiao.xisaiwang.com/ucenter2/login.html"
    "?referer=http%253A%252F%252Fwangxiao.xisaiwang.com%252F%252Fapi3th%252Fuser%252FcheckZuoti.do"
)
LIST_PAGE_URLS = {
    1: "https://wangxiao.xisaiwang.com/tiku2/list-zt136-1.html?areaName=",
    2: "https://wangxiao.xisaiwang.com/tiku2/list-zt136-2.html?kyNature=&kyMode=&schoolCode=&keyword=",
}
SPECIAL_STEMS = {
    "2020年软件设计师考试基础知识真题": "2020下半年选择题",
    "2020年软件设计师考试应用技术真题": "2020下半年案例题",
    "2023年下半年软件设计师真题学员回忆版": "2023下半年选择题",
}


def get_ascii_key(query_str: str) -> str:
    obj: Dict[str, str] = {}
    for pair in query_str.split("&"):
        if not pair:
            continue
        key, value = (pair.split("=", 1) + [""])[:2]
        obj[urllib.parse.unquote_plus(key)] = urllib.parse.unquote_plus(value)
    ascii_str = "&".join(f"{key}={obj[key]}" for key in sorted(obj))
    return ascii_str[::3]


def safe_name(name: str) -> str:
    return re.sub(r'[\\/:*?"<>|]+', "_", name).strip()


def clean_text(text: str) -> str:
    text = unescape(text or "")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t\f\v]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def looks_like_json_payload(text: str) -> bool:
    stripped = clean_text(text)
    return (
        (stripped.startswith("[{") and stripped.endswith("}]"))
        or (stripped.startswith("{") and stripped.endswith("}"))
    )


def is_meaningful_html(text: str) -> bool:
    plain = clean_text(re.sub(r"<[^>]+>", " ", text or ""))
    return plain not in {"", "[]", "{}", "【】", "问题", "问题1"} and plain != " "


def parse_vars(html: str) -> Dict[str, str]:
    out: Dict[str, str] = {}
    for key in ["id", "paperType", "classifyChain", "subjectCode", "accessId", "realPrice"]:
        match = re.search(rf'var\s+{re.escape(key)}\s*=\s*"([^"]*)";', html)
        if match:
            out[key] = match.group(1)
    return out


def parse_title(html: str) -> str:
    title_match = re.search(r"<title>(.*?)</title>", html, re.S | re.I)
    title = clean_text(re.sub(r"<[^>]+>", "", title_match.group(1) if title_match else ""))
    for suffix in [
        "-软考在线试题测试中心-希赛网",
        "-软考在线试题测试中心 - 希赛网",
        "-历年真题在线考试题库-历年真题模拟试题及答案-软考在线试题测试中心-希赛网",
    ]:
        if title.endswith(suffix):
            title = title[: -len(suffix)].strip()
    title = re.sub(r"[_-](考试题库_)?希赛网$", "", title).strip()
    title = re.sub(r"_考试题库$", "", title).strip()
    return title


def infer_output_stem(title: str) -> str:
    for prefix, stem in SPECIAL_STEMS.items():
        if title.startswith(prefix):
            return stem
    year_match = re.search(r"(20\d{2})年", title)
    if not year_match:
        raise ValueError(f"无法从标题识别年份: {title}")
    year = year_match.group(1)
    term = "上半年" if "上半年" in title else "下半年" if "下半年" in title else ""
    category = "案例题" if "应用技术" in title else "选择题" if "基础知识" in title else ""
    if not term:
        raise ValueError(f"无法从标题识别上下半年: {title}")
    if not category:
        raise ValueError(f"无法从标题识别题型类别: {title}")
    return f"{year}{term}{category}"


def parse_list_page(session: requests.Session, page_no: int, year_start: int, year_end: int) -> List[Dict[str, str]]:
    if page_no not in LIST_PAGE_URLS:
        raise ValueError(f"不支持的列表页编号: {page_no}")
    url = LIST_PAGE_URLS[page_no]
    response = session.get(url, headers={"User-Agent": USER_AGENT}, timeout=30)
    response.raise_for_status()
    html = response.text
    items: List[Dict[str, str]] = []
    seen_urls = set()
    for match in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', html, re.S | re.I):
        href = match.group(1).strip()
        raw = re.sub(r"<[^>]+>", " ", match.group(2))
        text = clean_text(raw)
        if not text or text == "开始做题":
            continue
        year_match = re.search(r"(20\d{2})年", text)
        if not year_match:
            continue
        year = int(year_match.group(1))
        if year < year_start or year > year_end:
            continue
        if "软件设计师" not in text:
            continue
        if not href.startswith("/tiku2/136/tp"):
            continue
        tp_url = urllib.parse.urljoin(url, href)
        if tp_url in seen_urls:
            continue
        seen_urls.add(tp_url)
        items.append({"list_title": text, "tp_url": tp_url})
    return items


def extract_asset_urls(html: str) -> List[str]:
    urls: List[str] = []
    for attr in ["src", "href"]:
        for match in re.finditer(rf'{attr}\s*=\s*"([^"]+)"', html, re.I):
            url = match.group(1).strip()
            if not url or url.startswith("data:"):
                continue
            urls.append(url)
    return urls


def normalize_asset_url(url: str, base_url: str) -> str:
    return urllib.parse.urljoin(base_url, unescape(url))


def pick_asset_filename(url: str, fallback_prefix: str) -> str:
    parsed = urllib.parse.urlparse(url)
    raw_name = os.path.basename(parsed.path) or fallback_prefix
    raw_name = urllib.parse.unquote(raw_name)
    raw_name = safe_name(raw_name)
    if "." not in raw_name:
        raw_name = f"{raw_name}.bin"
    return raw_name


def replace_assets(
    html: str,
    *,
    session: requests.Session,
    assets_dir: Path,
    asset_ref_prefix: str,
    asset_prefix: str,
    base_url: str,
) -> str:
    counter = 0

    def repl(match: re.Match[str]) -> str:
        nonlocal counter
        tag = match.group(0)
        src_match = re.search(r'src\s*=\s*"([^"]+)"', tag, re.I)
        if not src_match:
            return ""
        counter += 1
        src = normalize_asset_url(src_match.group(1), base_url)
        filename = pick_asset_filename(src, f"{asset_prefix}_{counter}")
        target = assets_dir / filename
        if not target.exists():
            response = session.get(src, headers={"User-Agent": USER_AGENT}, timeout=30)
            response.raise_for_status()
            target.write_bytes(response.content)
        rel_path = f"{asset_ref_prefix}/{filename}"
        alt_match = re.search(r'alt\s*=\s*"([^"]*)"', tag, re.I)
        alt_text = clean_text(alt_match.group(1) if alt_match else "") or f"{asset_prefix}_{counter}"
        return f"![{alt_text}]({rel_path})"

    html = re.sub(r"<img\b[^>]*>", repl, html, flags=re.I)
    html = re.sub(r"<audio\b[^>]*src=\"([^\"]+)\"[^>]*>.*?</audio>", lambda m: f"[音频]({normalize_asset_url(m.group(1), base_url)})", html, flags=re.I | re.S)
    html = re.sub(r"<video\b[^>]*src=\"([^\"]+)\"[^>]*>.*?</video>", lambda m: f"[视频]({normalize_asset_url(m.group(1), base_url)})", html, flags=re.I | re.S)
    html = re.sub(r"<source\b[^>]*src=\"([^\"]+)\"[^>]*>", lambda m: f"[媒体]({normalize_asset_url(m.group(1), base_url)})", html, flags=re.I)
    return html


def html_to_markdown(
    html: str,
    *,
    session: requests.Session,
    assets_dir: Path,
    asset_ref_prefix: str,
    asset_prefix: str,
    base_url: str,
) -> str:
    html = html or ""
    html = replace_assets(
        html,
        session=session,
        assets_dir=assets_dir,
        asset_ref_prefix=asset_ref_prefix,
        asset_prefix=asset_prefix,
        base_url=base_url,
    )
    replacements = [
        (r"<br\s*/?>", "\n"),
        (r"</p\s*>", "\n\n"),
        (r"<p\b[^>]*>", ""),
        (r"</div\s*>", "\n"),
        (r"<div\b[^>]*>", ""),
        (r"</li\s*>", "\n"),
        (r"<li\b[^>]*>", "- "),
        (r"</tr\s*>", "\n"),
        (r"<tr\b[^>]*>", ""),
        (r"</t[dh]\s*>", " | "),
        (r"<t[dh]\b[^>]*>", ""),
        (r"</?tbody\b[^>]*>", ""),
        (r"</?thead\b[^>]*>", ""),
        (r"</?table\b[^>]*>", "\n"),
        (r"</?(strong|b)\b[^>]*>", "**"),
        (r"</?(em|i)\b[^>]*>", "*"),
        (r"</?u\b[^>]*>", ""),
        (r"</?span\b[^>]*>", ""),
        (r"</?small\b[^>]*>", ""),
        (r"<a\b[^>]*href=\"([^\"]+)\"[^>]*>(.*?)</a>", r"[\2](\1)"),
    ]
    text = html
    for pattern, replacement in replacements:
        text = re.sub(pattern, replacement, text, flags=re.I | re.S)
    text = re.sub(r"<[^>]+>", "", text)
    text = clean_text(text)
    lines = [line.rstrip(" |") for line in text.splitlines()]
    return "\n".join(line for line in lines if line.strip())


def do_login(session: requests.Session, username: str, password: str) -> None:
    request_with_retry(session, "GET", LOGIN_PAGE, headers={"User-Agent": USER_AGENT}, timeout=30)
    sid = session.cookies.get("_sid_") or ""
    body = urllib.parse.urlencode(
        [
            ("loginName", username),
            ("password", password),
            ("imgCode", ""),
            ("imgKey", "12345678"),
            ("sk", "loginName"),
        ]
    )
    headers = {
        "User-Agent": USER_AGENT,
        "Referer": LOGIN_PAGE,
        "Origin": "https://wangxiao.xisaiwang.com",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "clientType": "PC",
        "sid": sid,
        "sscc": hashlib.md5((sid + username).encode()).hexdigest(),
        "sscc2": get_ascii_key(body),
    }
    response = request_with_retry(
        session,
        "POST",
        "https://wangxiao.xisaiwang.com/ucenter2/user/doLogin.do",
        data=body,
        headers=headers,
        timeout=30,
    )
    response.raise_for_status()
    payload = response.json()
    if payload.get("resultCode") != "SUCCESS":
        raise RuntimeError(f"登录失败: {payload}")


def fetch_exam_meta(session: requests.Session, tp_url: str) -> Dict[str, str]:
    response = request_with_retry(session, "GET", tp_url, headers={"User-Agent": USER_AGENT}, timeout=30)
    response.raise_for_status()
    html = response.text
    meta = parse_vars(html)
    if {"id", "paperType", "classifyChain"} - set(meta):
        raise RuntimeError("试卷介绍页变量解析失败")
    meta["title"] = parse_title(html)
    meta["tp_url"] = tp_url
    return meta


def start_exam(session: requests.Session, meta: Dict[str, str]) -> int:
    headers = {
        "User-Agent": USER_AGENT,
        "clientType": "PC",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": meta["tp_url"],
    }
    check = request_with_retry(
        session,
        "POST",
        "https://wangxiao.xisaiwang.com/ucenterapi/api3th/user/checkZuoti.do",
        data={
            "paperId": meta["id"],
            "paperType": meta["paperType"],
            "classifyId": meta["classifyChain"],
        },
        headers=headers,
        timeout=30,
    )
    check.raise_for_status()
    check_payload = check.json()
    if check_payload.get("resultCode") != "SUCCESS":
        raise RuntimeError(f"checkZuoti 失败: {check_payload}")
    check_model = check_payload["model"]
    start = request_with_retry(
        session,
        "POST",
        "https://wangxiao.xisaiwang.com/tikuapi/api3th/zuoti/startExam.do",
        data={
            "dataId": meta["id"],
            "paperType": meta["paperType"],
            "classifyId": meta["classifyChain"],
            "key": check_model.get("key", ""),
            "stuClassifyId": check_model.get("stuClassifyId", ""),
            "skuId": check_model.get("skuId", ""),
            "testModel": "Exercise",
            "num": "0",
            "areaCode": "0",
        },
        headers=headers,
        timeout=30,
    )
    start.raise_for_status()
    start_payload = start.json()
    if start_payload.get("resultCode") != "SUCCESS":
        raise RuntimeError(f"startExam 失败: {start_payload}")
    return int(start_payload["model"]["testLogId"])


def load_scantron(session: requests.Session, test_log_id: int) -> List[int]:
    headers = {
        "User-Agent": USER_AGENT,
        "clientType": "PC",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": f"https://wangxiao.xisaiwang.com/tiku2/exam{test_log_id}.html",
    }
    response = request_with_retry(
        session,
        "POST",
        "https://wangxiao.xisaiwang.com/tikuapi/api3th/zuoti/loadScantron.do",
        data={"testLogId": str(test_log_id)},
        headers=headers,
        timeout=30,
    )
    response.raise_for_status()
    payload = response.json()
    if payload.get("resultCode") != "SUCCESS":
        raise RuntimeError(f"loadScantron 失败: {payload}")
    st_ids: List[int] = []
    for block in payload["model"]["data"]:
        for item in block["shitiList"]:
            st_ids.append(int(item["stId"]))
    return st_ids


def load_question(session: requests.Session, test_log_id: int, st_id: int) -> Dict[str, object]:
    headers = {
        "User-Agent": USER_AGENT,
        "clientType": "PC",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": f"https://wangxiao.xisaiwang.com/tiku2/exam{test_log_id}.html",
    }
    response = request_with_retry(
        session,
        "POST",
        "https://wangxiao.xisaiwang.com/tikuapi/api3th/zuoti/loadShitiInfo.do",
        data={"stId": str(st_id), "testLogId": str(test_log_id)},
        headers=headers,
        timeout=30,
    )
    response.raise_for_status()
    payload = response.json()
    if payload.get("resultCode") != "SUCCESS":
        raise RuntimeError(f"loadShitiInfo 失败: stId={st_id}, payload={payload}")
    return payload["model"]


def load_analysis(session: requests.Session, test_log_id: int, st_id: int) -> Dict[str, object]:
    headers = {
        "User-Agent": USER_AGENT,
        "clientType": "PC",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": f"https://wangxiao.xisaiwang.com/tiku2/exam{test_log_id}.html",
    }
    response = request_with_retry(
        session,
        "POST",
        "https://wangxiao.xisaiwang.com/tikuapi/api3th/zuoti/loadShitiAnalysis.do",
        data={"stId": str(st_id), "testLogId": str(test_log_id)},
        headers=headers,
        timeout=30,
    )
    response.raise_for_status()
    payload = response.json()
    if payload.get("resultCode") != "SUCCESS":
        raise RuntimeError(f"loadShitiAnalysis 失败: stId={st_id}, payload={payload}")
    return payload["model"]


def request_with_retry(
    session: requests.Session,
    method: str,
    url: str,
    *,
    retries: int = 3,
    retry_delay: float = 1.5,
    **kwargs: object,
) -> requests.Response:
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            response = session.request(method, url, **kwargs)
            response.raise_for_status()
            return response
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError, requests.exceptions.HTTPError) as exc:
            last_error = exc
            if attempt >= retries:
                raise
            time.sleep(retry_delay * attempt)
    if last_error:
        raise last_error
    raise RuntimeError(f"请求失败: {method} {url}")


def normalize_answer_values(value: object) -> List[str]:
    if isinstance(value, list):
        out: List[str] = []
        for item in value:
            if isinstance(item, list):
                text = "".join(str(x).strip() for x in item if str(x).strip())
            else:
                text = str(item).strip()
            if text:
                out.append(text)
        return out
    text = clean_text(str(value or ""))
    return [text] if text else []


def fill_answer_into_stem(stem_text: str, answer_text: str) -> str:
    if not answer_text:
        return stem_text
    patterns = [
        r"（\s*[）)]",
        r"\(\s*[)）]",
        r"（\s*）",
        r"\(\s*\)",
    ]
    replaced = stem_text
    for pattern in patterns:
        new_text, count = re.subn(pattern, f"（{answer_text}）", replaced, count=1)
        if count > 0:
            return new_text
    return stem_text


def format_answer_block(
    *,
    session: requests.Session,
    title: str,
    html: str,
    assets_dir: Path,
    asset_ref_prefix: str,
    asset_prefix: str,
    base_url: str,
) -> List[str]:
    if not is_meaningful_html(html):
        return [f"### {title}", "", "站点未提供标准答案/解析"]
    md = html_to_markdown(
        html,
        session=session,
        assets_dir=assets_dir,
        asset_ref_prefix=asset_ref_prefix,
        asset_prefix=asset_prefix,
        base_url=base_url,
    )
    if not md.strip():
        md = "站点未提供标准答案/解析"
    return [f"### {title}", "", md]


def format_question(
    *,
    session: requests.Session,
    question_index: int,
    question: Dict[str, object],
    analysis: Dict[str, object],
    assets_dir: Path,
    asset_ref_prefix: str,
    base_url: str,
) -> str:
    shiti: Dict[str, object] = question["shiti"]  # type: ignore[assignment]
    analysis_shiti: Dict[str, object] = analysis["shiti"]  # type: ignore[assignment]
    st_type_name = str(shiti.get("stTypeName", "")).strip() or "未知题型"
    st_id = int(shiti["id"])
    question_map = shiti.get("questionMap")
    tigan_md = html_to_markdown(
        str(shiti.get("tigan", "")),
        session=session,
        assets_dir=assets_dir,
        asset_ref_prefix=asset_ref_prefix,
        asset_prefix=f"q{question_index:02d}_st{st_id}_tigan",
        base_url=base_url,
    )
    answer_values = normalize_answer_values(analysis_shiti.get("answerArray"))
    if st_type_name in {"单选题", "多选题", "判断题"} and answer_values:
        tigan_md = fill_answer_into_stem(tigan_md, "/".join(answer_values))
    parts: List[str] = [f"## 第{question_index}题（{st_type_name}）", "", tigan_md or "题干为空"]
    if isinstance(question_map, list) and question_map:
        render_blocks: List[str] = []
        for sub_index, item in enumerate(question_map, start=1):
            if isinstance(item, dict):
                if len(question_map) > 1:
                    render_blocks.append(f"### 问题{sub_index}")
                for key, value in item.items():
                    option_md = html_to_markdown(
                        str(value),
                        session=session,
                        assets_dir=assets_dir,
                        asset_ref_prefix=asset_ref_prefix,
                        asset_prefix=f"q{question_index:02d}_st{st_id}_opt{sub_index}_{key}",
                        base_url=base_url,
                    )
                    render_blocks.append(f"- {key}. {option_md}")
            else:
                item_md = html_to_markdown(
                    str(item),
                    session=session,
                    assets_dir=assets_dir,
                    asset_ref_prefix=asset_ref_prefix,
                    asset_prefix=f"q{question_index:02d}_st{st_id}_sub{sub_index}",
                    base_url=base_url,
                )
                if len(question_map) > 1:
                    render_blocks.append(f"### 问题{sub_index}")
                render_blocks.append(item_md)
        if render_blocks:
            parts.extend(["", *render_blocks])
    extra_question = html_to_markdown(
        str(shiti.get("question", "")),
        session=session,
        assets_dir=assets_dir,
        asset_ref_prefix=asset_ref_prefix,
        asset_prefix=f"q{question_index:02d}_st{st_id}_question",
        base_url=base_url,
    )
    rendered_question_map_json = ""
    if question_map:
        rendered_question_map_json = clean_text(json.dumps(question_map, ensure_ascii=False))
    if (
        extra_question
        and extra_question not in tigan_md
        and extra_question != rendered_question_map_json
        and not looks_like_json_payload(extra_question)
    ):
        parts.extend(["", "### 补充题面", "", extra_question])

    if st_type_name in {"单选题", "多选题", "判断题"}:
        if answer_values:
            parts.extend(["", f"### 正确答案", "", "、".join(answer_values)])
        else:
            parts.extend(["", "### 正确答案", "", "站点未提供标准答案"])
        analysis_html = ""
        analysis_array = analysis_shiti.get("analysisArray")
        if isinstance(analysis_array, list) and analysis_array:
            chunks: List[str] = []
            for item in analysis_array:
                if isinstance(item, list):
                    chunks.extend(str(x) for x in item if str(x).strip())
                elif str(item).strip():
                    chunks.append(str(item))
            analysis_html = "\n".join(chunks)
        if not analysis_html:
            analysis_html = str(analysis_shiti.get("analysis", ""))
        parts.extend(
            [""] + format_answer_block(
                session=session,
                title="解析",
                html=analysis_html,
                assets_dir=assets_dir,
                asset_ref_prefix=asset_ref_prefix,
                asset_prefix=f"q{question_index:02d}_st{st_id}_analysis",
                base_url=base_url,
            )
        )
    else:
        answer_html = str(analysis_shiti.get("answer", ""))
        analysis_html = str(analysis_shiti.get("analysis", ""))
        parts.extend(
            [""] + format_answer_block(
                session=session,
                title="参考答案",
                html=answer_html,
                assets_dir=assets_dir,
                asset_ref_prefix=asset_ref_prefix,
                asset_prefix=f"q{question_index:02d}_st{st_id}_answer",
                base_url=base_url,
            )
        )
        parts.extend(
            [""] + format_answer_block(
                session=session,
                title="解析",
                html=analysis_html,
                assets_dir=assets_dir,
                asset_ref_prefix=asset_ref_prefix,
                asset_prefix=f"q{question_index:02d}_st{st_id}_analysis",
                base_url=base_url,
            )
        )
    return "\n".join(parts).strip() + "\n"


def build_markdown(
    *,
    session: requests.Session,
    meta: Dict[str, str],
    st_ids: Iterable[int],
    test_log_id: int,
    output_file: Path,
    assets_dir: Path,
) -> None:
    st_ids_list = list(st_ids)
    stem = output_file.stem
    asset_ref_prefix = f"../题目素材/{stem}"
    exam_url = f"https://wangxiao.xisaiwang.com/tiku2/exam{test_log_id}.html"
    sections = [
        f"# {stem}",
        "",
        f"- 来源标题: {meta['title']}",
        f"- 试卷介绍页: {meta['tp_url']}",
        f"- 练习页: {exam_url}",
        f"- 题量: {len(st_ids_list)}",
    ]
    question_blocks: List[str] = []
    for idx, st_id in enumerate(st_ids_list, start=1):
        model = load_question(session, test_log_id, st_id)
        analysis = load_analysis(session, test_log_id, st_id)
        question_blocks.append(
            format_question(
                session=session,
                question_index=idx,
                question=model,
                analysis=analysis,
                assets_dir=assets_dir,
                asset_ref_prefix=asset_ref_prefix,
                base_url=exam_url,
            )
        )
    document = "\n".join(sections).strip() + "\n\n" + "\n\n".join(question_blocks).strip() + "\n"
    output_file.write_text(document, encoding="utf-8")


def fetch_single_exam(
    *,
    session: requests.Session,
    tp_url: str,
    output_root: Path,
    stem_override: str = "",
) -> Dict[str, object]:
    meta = fetch_exam_meta(session, tp_url)
    stem = safe_name(stem_override or infer_output_stem(meta["title"]))
    questions_dir = output_root / "题目"
    assets_root = output_root / "题目素材"
    output_file = questions_dir / f"{stem}.md"
    assets_dir = assets_root / stem
    questions_dir.mkdir(parents=True, exist_ok=True)
    assets_dir.mkdir(parents=True, exist_ok=True)

    test_log_id = start_exam(session, meta)
    st_ids = load_scantron(session, test_log_id)
    build_markdown(
        session=session,
        meta=meta,
        st_ids=st_ids,
        test_log_id=test_log_id,
        output_file=output_file,
        assets_dir=assets_dir,
    )
    return {
        "output_file": str(output_file),
        "assets_dir": str(assets_dir),
        "question_count": len(st_ids),
        "title": meta["title"],
        "tp_url": tp_url,
    }


def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch a Xisai exam paper into Markdown.")
    parser.add_argument("--username", required=True)
    parser.add_argument("--password", required=True)
    parser.add_argument("--tp-url", help="Paper detail page, for example /tiku2/136/tp30417892.html?cid=136")
    parser.add_argument("--stem-override", default="", help="Override output markdown stem.")
    parser.add_argument(
        "--batch-list-pages",
        nargs="*",
        type=int,
        default=[],
        help="Batch mode: fetch all matching papers from list pages, e.g. --batch-list-pages 1 2",
    )
    parser.add_argument("--year-start", type=int, default=2015)
    parser.add_argument("--year-end", type=int, default=2025)
    parser.add_argument(
        "--output-root",
        default="doc/Software-Designer-master/真题/xisai_md",
        help="Root directory that will contain 题目 and 题目素材",
    )
    return parser.parse_args(argv)


def main(argv: List[str]) -> int:
    args = parse_args(argv)
    session = requests.Session()
    do_login(session, args.username, args.password)
    output_root = Path(args.output_root)
    if args.batch_list_pages:
        all_items: List[Dict[str, str]] = []
        seen_urls = set()
        for page_no in args.batch_list_pages:
            for item in parse_list_page(session, page_no, args.year_start, args.year_end):
                if item["tp_url"] in seen_urls:
                    continue
                seen_urls.add(item["tp_url"])
                all_items.append(item)
        results: List[Dict[str, object]] = []
        for item in all_items:
            results.append(
                fetch_single_exam(
                    session=session,
                    tp_url=item["tp_url"],
                    output_root=output_root,
                )
            )
        print(json.dumps({"count": len(results), "results": results}, ensure_ascii=False))
        return 0

    if not args.tp_url:
        raise SystemExit("单卷模式必须提供 --tp-url，或使用 --batch-list-pages")

    result = fetch_single_exam(
        session=session,
        tp_url=args.tp_url,
        output_root=output_root,
        stem_override=args.stem_override,
    )
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
