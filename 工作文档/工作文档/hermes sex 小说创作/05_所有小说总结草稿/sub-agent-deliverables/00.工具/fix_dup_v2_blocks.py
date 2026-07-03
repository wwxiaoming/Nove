# -*- coding: utf-8 -*-
# **最后更新**：2026-06-23 12:40
r"""
fix_dup_v2_blocks.py - 修复因脚本重复运行导致的 v2 块重复

每个 batch 文件的 v2 块应该只出现 1 次（在标题后）。
本脚本会检测并删除重复的 v2 块。
"""

from pathlib import Path
import re

BASE = Path(r"c:\Users\Administrator\Desktop\623 11\优化Batch子代理输入")
SUB_DELIV = BASE / "documents" / "sub-agent-deliverables"

# v2 块的标记行
V2_MARKERS = [
    "> **创建时间**：2026-06-22 18:54",
    "> **最后更新**：2026-06-23 12:35",
    "> **配套 v2 任务模板**：",
    "> **同步状态**：v3 雷点约束",
]


def find_v2_block_ranges(lines):
    """找到所有 v2 块的范围（起始行号列表）"""
    ranges = []
    i = 0
    while i < len(lines):
        if any(m in lines[i] for m in V2_MARKERS):
            # 找到 v2 块开始
            start = i
            # 找到 v2 块结束（下一个空行 + ## 标题，或 v2 块结束位置）
            # v2 块有 4 行（4 个 marker） + 1 个空行
            end = i
            for j in range(i, min(i + 10, len(lines))):
                if lines[j].strip() == "" and j > i + 3:
                    end = j
                    break
                if j == min(i + 10, len(lines)) - 1:
                    end = j + 1
            ranges.append((start, end))
            i = end + 1
        else:
            i += 1
    return ranges


def fix_file(file_path: Path) -> bool:
    """删除重复的 v2 块，保留第一个"""
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"  [FAIL] 读取失败：{e}")
        return False

    lines = content.split("\n")
    ranges = find_v2_block_ranges(lines)

    if len(ranges) <= 1:
        return True  # 没有重复，无需修复

    # 删除从第二个 v2 块开始的所有重复块
    # 从后往前删除以保持索引
    for start, end in reversed(ranges[1:]):
        del lines[start:end]

    new_content = "\n".join(lines)
    try:
        file_path.write_text(new_content, encoding="utf-8")
        return True
    except Exception as e:
        print(f"  [FAIL] 写入失败：{e}")
        return False


def main():
    print("=== 修复 v2 块重复 ===\n")

    batch_dirs = sorted([d for d in SUB_DELIV.iterdir() if d.is_dir() and d.name.startswith("batch-")])

    total = 0
    fixed = 0
    for batch_dir in batch_dirs:
        for f in sorted(batch_dir.glob("*.md")):
            total += 1
            # 统计修复前的 v2 块数
            content = f.read_text(encoding="utf-8")
            count_before = sum(content.count(m) for m in V2_MARKERS) // len(V2_MARKERS)
            ok = fix_file(f)
            count_after_marker = "**创建时间**" in f.read_text(encoding="utf-8")
            count_after = sum(f.read_text(encoding="utf-8").count(m) for m in V2_MARKERS) // len(V2_MARKERS)
            status = "[FIXED]" if ok and count_after < count_before else ("[OK]" if count_after == 1 else "[FAIL]")
            rel = f.relative_to(SUB_DELIV)
            print(f"  {status} {rel}  (v2块：{count_before} → {count_after})")
            if count_after < count_before:
                fixed += 1

    print(f"\n=== 完成：{fixed}/{total} 份文件已修复 ===")


if __name__ == "__main__":
    main()
