# -*- coding: utf-8 -*-
"""
最终清理：去除所有规范文件中残留的"速查表"引用。
"""
from pathlib import Path
import re

BASE = Path(r"c:\Users\Administrator\Desktop\623 11\优化Batch子代理输入\documents\sub-agent-deliverables")

TARGETS = [
    "batch-01_战队特摄/输入输出规范_batch-01_战队特摄.md",
    "batch-02a_勇者魔物奇幻_前/输入输出规范_batch-02a_勇者魔物奇幻_前.md",
    "batch-02b_勇者魔物奇幻_后/输入输出规范_batch-02b_勇者魔物奇幻_后.md",
    "batch-03a_正太校园堕落_前/输入输出规范_batch-03a_正太校园堕落_前.md",
    "batch-03b_正太校园堕落_后/输入输出规范_batch-03b_正太校园堕落_后.md",
    "batch-04_调教拍卖+异种触手/输入输出规范_batch-04_调教拍卖+异种触手.md",
    "batch-05_修真玄幻+外语/输入输出规范_batch-05_修真玄幻+外语.md",
    "batch-06_同人+女性向/输入输出规范_batch-06_同人+女性向.md",
]

# 各种需要清理的速查表引用
CLEANUPS = [
    # §一 定位
    (
        r"- sub-agent \*\*按\*\* \*\*`sub-agent分配速查表\.md`\*\* \*\*中的分配\*\*逐本阅读",
        "- sub-agent **按本规范 §三 + 9 段标准结构指引** 逐本阅读",
    ),
    # §七 Files to Execute 头部块：本批配套速查表
    (
        r"> \*\*本批配套速查表\*\*：`[^>]+>",
        "",
    ),
    # §七 Files to Execute 头部块：总速查表
    (
        r"> \*\*总速查表（旧版 v5，6 批量）\*\*：`[^>]+>",
        "",
    ),
    # §七 Files to Execute 表格中"源小说（按速查表指定路径）"
    (
        r"源小说（按速查表指定路径；单段 ≤500KB 直接读）",
        "源小说（按子类型对应路径，单段 ≤500KB 直接读）",
    ),
    # 路径硬约束中提到"速查表标注的" — 保留，但改成"原规划中"
    (
        r"速查表标注的 `/workspace/帝王战队621 1：00/` 路径 \*\*不存在\*\*",
        "原规划中标注的 `/workspace/帝王战队621 1：00/` 路径 **不存在**",
    ),
    # 头部"配套速查表"残留
    (
        r"> 配套：`速查表_batch-[^`]+`",
        "",
    ),
]


def fix_spec(file_path: Path) -> dict:
    text = file_path.read_text(encoding="utf-8")
    original = text
    changes = []

    for pat, repl in CLEANUPS:
        if re.search(pat, text):
            text = re.sub(pat, repl, text, count=1)
            changes.append(f"清理：{pat[:40]}...")

    if text != original:
        file_path.write_text(text, encoding="utf-8")
    return {"file": file_path.name, "changes": changes, "modified": text != original}


def main():
    print(f"=== 最终清理规范文件中的速查表引用 ===\n")
    for rel in TARGETS:
        fp = BASE / rel
        if not fp.exists():
            print(f"[SKIP] {rel}")
            continue
        result = fix_spec(fp)
        if result["modified"]:
            print(f"[FIXED] {rel}")
            for c in result["changes"]:
                print(f"   - {c}")
        else:
            print(f"[NO-CHANGE] {rel}")


if __name__ == "__main__":
    main()
