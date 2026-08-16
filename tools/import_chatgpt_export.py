#!/usr/bin/env python3
"""Import a user-owned ChatGPT data export and build a local archive.

This tool does NOT connect to a user's private ChatGPT account and does not
attempt to bypass access controls. It processes an export that the user has
legally downloaded and supplied.

Optional OpenAI enrichment can be enabled with OPENAI_API_KEY. The key is read
from the environment and is never stored in the repository.

Usage:
  python tools/import_chatgpt_export.py /path/to/conversations.json --out archive
  OPENAI_API_KEY=... python tools/import_chatgpt_export.py conversations.json --out archive --summarize
"""

import argparse
import json
import os
import re
from collections import Counter
from pathlib import Path
from typing import Any


def text_from_message(msg: dict[str, Any]) -> str:
    content = msg.get("content") or {}
    parts = content.get("parts") or []
    out = []
    for part in parts:
        if isinstance(part, str):
            out.append(part)
        elif isinstance(part, dict):
            # Keep text-like fields while avoiding binary payloads.
            for key in ("text", "value"):
                if isinstance(part.get(key), str):
                    out.append(part[key])
    return "\n".join(out).strip()


def extract_conversations(raw: Any) -> list[dict[str, Any]]:
    if isinstance(raw, list):
        return [x for x in raw if isinstance(x, dict)]
    if isinstance(raw, dict):
        for key in ("conversations", "items", "data"):
            if isinstance(raw.get(key), list):
                return [x for x in raw[key] if isinstance(x, dict)]
    raise ValueError("Could not find a conversation list in the supplied export.")


def flatten_conversation(c: dict[str, Any]) -> list[dict[str, Any]]:
    mapping = c.get("mapping")
    rows = []
    if isinstance(mapping, dict):
        for node in mapping.values():
            msg = (node or {}).get("message") or {}
            text = text_from_message(msg)
            if text:
                rows.append({
                    "author": (msg.get("author") or {}).get("role", "unknown"),
                    "created": msg.get("create_time"),
                    "text": text,
                })
    elif isinstance(c.get("messages"), list):
        for msg in c["messages"]:
            if isinstance(msg, dict):
                text = text_from_message(msg) or str(msg.get("text", ""))
                if text:
                    rows.append({
                        "author": msg.get("role", "unknown"),
                        "created": msg.get("create_time"),
                        "text": text,
                    })
    return sorted(rows, key=lambda x: (x.get("created") is None, x.get("created") or 0))


def safe_filename(name: str) -> str:
    name = re.sub(r"[^\w\-. ]+", "_", name, flags=re.UNICODE).strip()
    return (name[:100] or "conversation") + ".md"


def write_archive(conversations: list[dict[str, Any]], out: Path) -> dict[str, Any]:
    out.mkdir(parents=True, exist_ok=True)
    records = []
    years = Counter()

    for i, conv in enumerate(conversations, 1):
        title = conv.get("title") or f"Conversation {i}"
        rows = flatten_conversation(conv)
        first_time = next((r["created"] for r in rows if r.get("created")), None)
        if isinstance(first_time, (int, float)):
            from datetime import datetime, timezone
            dt = datetime.fromtimestamp(first_time, tz=timezone.utc)
            years[str(dt.year)] += 1
        md = [f"# {title}\n", f"Source index: {i}\n"]
        for row in rows:
            author = row.get("author", "unknown")
            md.append(f"## {author}\n\n{row['text']}\n")
        path = out / f"{i:05d}-{safe_filename(title)}"
        path.write_text("\n".join(md), encoding="utf-8")
        records.append({"index": i, "title": title, "path": str(path.relative_to(out)), "messages": len(rows)})

    manifest = {
        "conversation_count": len(conversations),
        "years": dict(sorted(years.items())),
        "records": records,
        "privacy_note": "Generated from a user-supplied export. Review and remove private information before publishing."
    }
    (out / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return manifest


def optional_openai_summary(manifest: dict[str, Any], out: Path) -> None:
    """Optional enrichment hook; intentionally requires explicit API-key opt-in."""
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        print("OPENAI_API_KEY not set; skipping AI enrichment.")
        return

    try:
        from openai import OpenAI
    except ImportError:
        raise SystemExit("Install the OpenAI SDK first: python -m pip install openai")

    client = OpenAI(api_key=key)
    sample = manifest["records"][:20]
    prompt = (
        "Create a concise thematic index for this conversation archive. "
        "Do not invent content. Mark uncertainty. Return Markdown headings and bullets.\n\n"
        + json.dumps(sample, ensure_ascii=False)
    )
    response = client.responses.create(
        model=os.getenv("OPENAI_MODEL", "gpt-5"),
        input=prompt,
    )
    (out / "AI_THEMATIC_INDEX.md").write_text(response.output_text, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("export", type=Path)
    parser.add_argument("--out", type=Path, default=Path("archive"))
    parser.add_argument("--summarize", action="store_true")
    args = parser.parse_args()

    raw = json.loads(args.export.read_text(encoding="utf-8"))
    conversations = extract_conversations(raw)
    manifest = write_archive(conversations, args.out)
    if args.summarize:
        optional_openai_summary(manifest, args.out)
    print(f"Imported {manifest['conversation_count']} conversations into {args.out}")


if __name__ == "__main__":
    main()
