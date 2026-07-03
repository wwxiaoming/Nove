# -*- coding: utf-8 -*-
# **最后更新**：2026-06-23 12:42
r"""
fix_dup_v2_blocks_v2.py - 修复规范文件中 v2 块重复（v2 修复版）

v1 失败原因：v2 块之间没有空行，旧脚本找"下一个空行"作为结束位置失败。
v2 方案：v2 块固定 4 行（4 个 marker），用"4 行一组"识别 + 删除。
"""

from pathlib import Path

BASE = Path(r"c:\Users\Administrator\Desktop\623 11\优化Batch子代理输入")
SUB_DELIV = BASE / "documents" / "sub-agent-deliverables"

# v2 块的 4 个 marker
V2_MARKERS = [
    "> **创建时间**：2026-06-22 18:54",
    "> **最后更新**：2026-06-23 12:35",
    "> **配套 v2 任务模板**：",
    "> **同步状态**：v3 雷点约束",
]


def fix_file(file_path: Path) -> int:
    """
    删除重复的 v2 块，保留第一个。
    返回删除的块数。
    """
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"  [FAIL] 读取失败：{e}")
        return 0

    lines = content.split("\n")

    # 找到所有 v2 块的开始行号
    block_starts = []
    for i, line in enumerate(lines):
        if "> **创建时间**：2026-06-22 18:54" in line:
            block_starts.append(i)

    if len(block_starts) <= 1:
        return 0  # 没有重复

    # 删除从第二个 v2 块开始的所有块（每个块 4 行）
    blocks_deleted = 0
    for start in reversed(block_starts[1:]):
        # 删除这个块（4 行）+ 后面可能的空行
        end = start + 4
        # 如果后面跟着空行，删一个
        if end < len(lines) and lines[end].strip() == "":
            end += 1
        del lines[start:end]
        blocks_deleted += 1

    new_content = "\n".join(lines)
    try:
        file_path.write_text(new_content, encoding="utf-8")
        return blocks_deleted
    except Exception as e:
        print(f"  [FAIL] 写入失败：{e}")
        return 0


def main():
    print("=== 修复 v2 块重复（v2 修复版）===\n")

    batch_dirs = sorted([d for d in SUB_DELIV.iterdir() if d.is_dir() and d.name.startswith("batch-")])

    total = 0
    total_blocks_deleted = 0
    for batch_dir in batch_dirs:
        for f in sorted(batch_dir.glob("*.md")):
            total += 1
            content_before = f.read_text(encoding="utf-8")
            count_before = content_before.count("> **创建时间**：2026-06-22 18:54")
            deleted = fix_file(f)
            content_after = f.read_text(encoding="utf-8")
            count_after = content_after.count("> **创建时间**：2026-06-22 18:54")
            rel = f.relative_to(SUB_DELIV)
            ftype = "规范" if "输入输出规范" in f.name else "速查表"
            if deleted > 0:
                print(f"  [FIXED] {rel} ({ftype})  v2块：{count_before} -> {count_after} (删除 {deleted} 个)")
                total_blocks_deleted += deleted
            else:
                print(f"  [OK] {rel} ({ftype})  v2块：{count_before}")

    print(f"\n=== 完成：删除 {total_blocks_deleted} 个重复 v2 块 ===")


if __name__ == "__main__":
    main()
