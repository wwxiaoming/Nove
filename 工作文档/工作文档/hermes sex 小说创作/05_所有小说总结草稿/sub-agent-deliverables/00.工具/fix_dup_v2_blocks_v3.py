# -*- coding: utf-8 -*-
"""
修复所有batch-XX规范和速查表中的重复v2块。
对每个文件：
1. 找到所有v2块（"📋 v2 任务模板同步状态"或"📋 v2 任务模板引用"）
2. 保留第一个，删除后续的
3. 同步时间戳为最新
"""
from pathlib import Path
import re

BASE = Path(r"c:\Users\Administrator\Desktop\623 11\优化Batch子代理输入\documents\sub-agent-deliverables")
TIMESTAMP = "2026-06-23 12:50"

TARGETS = [
    "batch-01_战队特摄/输入输出规范_batch-01_战队特摄.md",
    "batch-01_战队特摄/速查表_batch-01_战队特摄.md",
    "batch-02a_勇者魔物奇幻_前/输入输出规范_batch-02a_勇者魔物奇幻_前.md",
    "batch-02a_勇者魔物奇幻_前/速查表_batch-02a_勇者魔物奇幻_前.md",
    "batch-02b_勇者魔物奇幻_后/输入输出规范_batch-02b_勇者魔物奇幻_后.md",
    "batch-02b_勇者魔物奇幻_后/速查表_batch-02b_勇者魔物奇幻_后.md",
    "batch-03a_正太校园堕落_前/输入输出规范_batch-03a_正太校园堕落_前.md",
    "batch-03a_正太校园堕落_前/速查表_batch-03a_正太校园堕落_前.md",
    "batch-03b_正太校园堕落_后/输入输出规范_batch-03b_正太校园堕落_后.md",
    "batch-03b_正太校园堕落_后/速查表_batch-03b_正太校园堕落_后.md",
    "batch-04_调教拍卖+异种触手/输入输出规范_batch-04_调教拍卖+异种触手.md",
    "batch-04_调教拍卖+异种触手/速查表_batch-04_调教拍卖+异种触手.md",
    "batch-05_修真玄幻+外语/输入输出规范_batch-05_修真玄幻+外语.md",
    "batch-05_修真玄幻+外语/速查表_batch-05_修真玄幻+外语.md",
    "batch-06_同人+女性向/输入输出规范_batch-06_同人+女性向.md",
    "batch-06_同人+女性向/速查表_batch-06_同人+女性向.md",
]

V2_HEADERS = [
    "## 📋 v2 任务模板同步状态",
    "## 📋 v2 任务模板引用",
]


def fix_file(file_path: Path) -> dict:
    """删除从第二个v2块开始的所有块。"""
    text = file_path.read_text(encoding="utf-8")
    lines = text.split("\n")

    block_starts = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        for header in V2_HEADERS:
            if stripped == header or stripped.startswith(header):
                block_starts.append(i)
                break

    if len(block_starts) <= 1:
        return {"file": str(file_path), "blocks_found": len(block_starts), "blocks_deleted": 0}

    blocks_deleted = 0
    for start in reversed(block_starts[1:]):
        end = start + 1
        while end < len(lines):
            if lines[end].strip() in V2_HEADERS or lines[end].startswith("# "):
                break
            if end > start + 1 and (lines[end].startswith("## ") or lines[end].startswith("# ")):
                break
            end += 1
        while end > start and lines[end - 1].strip() == "":
            end -= 1
        if end < len(lines) and lines[end].strip() == "":
            end += 1
        del lines[start:end]
        blocks_deleted += 1

    new_text = "\n".join(lines)
    file_path.write_text(new_text, encoding="utf-8")

    return {"file": str(file_path), "blocks_found": len(block_starts), "blocks_deleted": blocks_deleted}


def main():
    print(f"=== v2 block dedup run @ {TIMESTAMP} ===\n")
    total_deleted = 0
    for rel in TARGETS:
        fp = BASE / rel
        if not fp.exists():
            print(f"[SKIP] {rel} (not found)")
            continue
        result = fix_file(fp)
        if result["blocks_deleted"] > 0:
            print(f"[FIXED] {rel}: deleted {result['blocks_deleted']} duplicate block(s) (found {result['blocks_found']})")
            total_deleted += result["blocks_deleted"]
        else:
            print(f"[OK]    {rel}: {result['blocks_found']} block(s) (no duplicates)")
    print(f"\n=== Total: {total_deleted} duplicate block(s) deleted ===")


if __name__ == "__main__":
    main()
