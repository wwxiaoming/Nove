"""
R2 改写措辞 v2.4 优化脚本
- "仪式化去势感" → "榨精/龟头责/强制精尽"（R18 普通表述）
- "仪式化锁链" → "锁精环 + 反复榨取"（R18 普通表述）
- 涵盖：04.batch草稿 / 05.batch草稿 / 06.batch草稿 / 00.工具/派发任务_batch-04_4个子代理.md
"""
import re
from pathlib import Path

# 替换映射
REPLACEMENTS = {
    "仪式化去势感 + 锁链束缚 + 强制射精当众": "榨精/龟头责 + 锁精环束缚 + 强制射精当众",
    "仪式化去势感 / 锁链束缚 / 强迫当众": "榨精/龟头责 + 锁精环束缚 + 强制精尽",
    "仪式化去势感 / 锁链束缚 / 强制射精当众": "榨精/龟头责 + 锁精环束缚 + 强制射精当众",
    "仪式化去势感 + 锁链束缚 + 强制射精": "榨精/龟头责 + 锁精环束缚 + 强制射精",
    "仪式化锁链 / 强制射精当众": "锁精环 + 反复榨取 + 强制射精当众",
    "仪式化去势感 / 羞辱工具": "榨精/龟头责 + 羞辱工具",
    "仪式化去势感 / 锁链束缚": "榨精/龟头责 + 锁精环束缚",
    "仪式化去势感": "榨精/龟头责/强制精尽",
    "仪式化锁链": "锁精环束缚 + 反复榨取",
}

# 目标路径
TARGET_FILES = [
    # 04.batch草稿
    r"c:\Users\Administrator\Desktop\623 11\优化Batch子代理输入\documents\sub-agent-deliverables\04.batch草稿\pixiv小说_04_SA-04-A_圣兽战士_子段2.md",
    r"c:\Users\Administrator\Desktop\623 11\优化Batch子代理输入\documents\sub-agent-deliverables\04.batch草稿\pixiv小说_04_SA-04-B_圣兽战士_子段1.md",
    r"c:\Users\Administrator\Desktop\623 11\优化Batch子代理输入\documents\sub-agent-deliverables\04.batch草稿\pixiv小说_04_SA-04-C_乱七八糟的文都在这_子段1.md",
    r"c:\Users\Administrator\Desktop\623 11\优化Batch子代理输入\documents\sub-agent-deliverables\04.batch草稿\pixiv小说_04_SA-04-D_乱七八糟的文都在这_子段2.md",
    r"c:\Users\Administrator\Desktop\623 11\优化Batch子代理输入\documents\sub-agent-deliverables\04.batch草稿\pixiv小说_04_SA-04-D_圣兽战士_子段3.md",
    r"c:\Users\Administrator\Desktop\623 11\优化Batch子代理输入\documents\sub-agent-deliverables\04.batch草稿\pixiv小说_04_SA-04-E_为什么被榨精的总是我.md",
    r"c:\Users\Administrator\Desktop\623 11\优化Batch子代理输入\documents\sub-agent-deliverables\04.batch草稿\pixiv小说_04_SA-04-E_新.魔王与勇者（下）.md",
    r"c:\Users\Administrator\Desktop\623 11\优化Batch子代理输入\documents\sub-agent-deliverables\04.batch草稿\pixiv小说_04_SA-04-E_沉溺黏液的侦探无法逃离实验的结局.md",
    r"c:\Users\Administrator\Desktop\623 11\优化Batch子代理输入\documents\sub-agent-deliverables\04.batch草稿\pixiv小说_04_SA-04-E_海盗先生的精液拍卖会.md",
    r"c:\Users\Administrator\Desktop\623 11\优化Batch子代理输入\documents\sub-agent-deliverables\04.batch草稿\pixiv小说_04_SA-04-E_精疲力尽的小英雄不幸落入恶霸之手.md",
    r"c:\Users\Administrator\Desktop\623 11\优化Batch子代理输入\documents\sub-agent-deliverables\04.batch草稿\pixiv小说_04_SA-04-E_蟾神.md",
    r"c:\Users\Administrator\Desktop\623 11\优化Batch子代理输入\documents\sub-agent-deliverables\04.batch草稿\pixiv小说_04_SA-04-E_魅魔正太的裸足榨精游戏（一）.md",
    r"c:\Users\Administrator\Desktop\623 11\优化Batch子代理输入\documents\sub-agent-deliverables\04.batch草稿\pixiv小说_04_SA-04-E_鲨鱼系少年也会被触须凌辱.md",
    # 05.batch草稿
    r"c:\Users\Administrator\Desktop\623 11\优化Batch子代理输入\documents\sub-agent-deliverables\05.batch草稿\pixiv小说_05_SA-05-C_元灵战纪.md",
    r"c:\Users\Administrator\Desktop\623 11\优化Batch子代理输入\documents\sub-agent-deliverables\05.batch草稿\pixiv小说_05_SA-05-E-2_射精が一般化的世界_后半.md",
    r"c:\Users\Administrator\Desktop\623 11\优化Batch子代理输入\documents\sub-agent-deliverables\05.batch草稿\pixiv小说_05_SA-05-E_搾精生物から生き残れ！.md",
    # 06.batch草稿
    r"c:\Users\Administrator\Desktop\623 11\优化Batch子代理输入\documents\sub-agent-deliverables\06.batch草稿\pixiv小说_06_SA-06-A_光环 无限.md",
    r"c:\Users\Administrator\Desktop\623 11\优化Batch子代理输入\documents\sub-agent-deliverables\06.batch草稿\pixiv小说_06_SA-06-B_妨碍拯救世界的勇者居然是魅魔！.md",
    r"c:\Users\Administrator\Desktop\623 11\优化Batch子代理输入\documents\sub-agent-deliverables\06.batch草稿\pixiv小说_06_SA-06-C_帝国农场.md",
    r"c:\Users\Administrator\Desktop\623 11\优化Batch子代理输入\documents\sub-agent-deliverables\06.batch草稿\pixiv小说_06_SA-06-C_被奴役的大探险家.md",
    r"c:\Users\Administrator\Desktop\623 11\优化Batch子代理输入\documents\sub-agent-deliverables\06.batch草稿\pixiv小说_06_SA-06-D_奴隶调教中心.md",
    # 备用
    r"c:\Users\Administrator\Desktop\623 11\优化Batch子代理输入\documents\sub-agent-deliverables\备用\pixiv小说_05_SA-05-E_射精が一般化的世界.md",
    # 派发任务
    r"c:\Users\Administrator\Desktop\623 11\优化Batch子代理输入\documents\sub-agent-deliverables\00.工具\派发任务_batch-04_4个子代理.md",
]


def rewrite_file(path: str) -> tuple[str, int]:
    """重写文件，返回 (状态, 替换次数)"""
    p = Path(path)
    if not p.exists():
        return ("[SKIP] 文件不存在", 0)

    content = p.read_text(encoding="utf-8")
    original = content
    total_count = 0
    replacements_made = []

    # 优先匹配长字符串（避免短字符串误覆盖）
    sorted_items = sorted(REPLACEMENTS.items(), key=lambda x: -len(x[0]))
    for old, new in sorted_items:
        if old in content:
            count = content.count(old)
            content = content.replace(old, new)
            total_count += count
            replacements_made.append(f"{old}→{new}({count}次)")

    if content == original:
        return ("[NO-CHANGE]", 0)

    p.write_text(content, encoding="utf-8")
    return ("[OK] " + "; ".join(replacements_made), total_count)


def main():
    print("=" * 80)
    print("R2 改写措辞 v2.4 优化 — 全局替换")
    print("=" * 80)
    success = 0
    skip = 0
    nochange = 0
    total_replacements = 0
    for f in TARGET_FILES:
        name = Path(f).name
        status, count = rewrite_file(f)
        print(f"{status} — {name} (替换 {count} 处)")
        if "[OK]" in status:
            success += 1
            total_replacements += count
        elif "[SKIP]" in status:
            skip += 1
        else:
            nochange += 1
    print("=" * 80)
    print(f"总计: 修改 {success} 文件 / 跳过 {skip} / 无变化 {nochange} / 累计替换 {total_replacements} 处")
    print("=" * 80)


if __name__ == "__main__":
    main()
