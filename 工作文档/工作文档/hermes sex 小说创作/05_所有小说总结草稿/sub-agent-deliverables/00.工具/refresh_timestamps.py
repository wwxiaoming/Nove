# -*- coding: utf-8 -*-
"""
统一刷新所有16个batch规范/速查表的头部时间戳和v2同步状态时间戳。
"""
from pathlib import Path

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

OLD_LAST_UPDATE = "2026-06-23 12:35"


def refresh_file(file_path: Path) -> int:
    text = file_path.read_text(encoding="utf-8")
    new_text = text.replace(f"**最后更新**：{OLD_LAST_UPDATE}", f"**最后更新**：{TIMESTAMP}")
    new_text = new_text.replace(f"同步状态（{OLD_LAST_UPDATE}）", f"同步状态（{TIMESTAMP}）")
    new_text = new_text.replace(f"引用（{OLD_LAST_UPDATE}）", f"引用（{TIMESTAMP}）")
    updates = 0
    if new_text != text:
        file_path.write_text(new_text, encoding="utf-8")
        updates = new_text.count(TIMESTAMP) - text.count(TIMESTAMP)
    return updates


def main():
    print(f"=== Refresh timestamps to {TIMESTAMP} ===\n")
    total = 0
    for rel in TARGETS:
        fp = BASE / rel
        if not fp.exists():
            print(f"[SKIP] {rel}")
            continue
        n = refresh_file(fp)
        print(f"[OK] {rel}: {n} timestamp(s) updated")
        total += n
    print(f"\n=== Total: {total} timestamp(s) updated across {len(TARGETS)} files ===")


if __name__ == "__main__":
    main()
