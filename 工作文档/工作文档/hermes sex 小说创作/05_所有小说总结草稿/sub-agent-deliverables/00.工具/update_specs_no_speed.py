# -*- coding: utf-8 -*-
"""
综合修改 8 份输入输出规范：
1. 删除头部"配套速查表"引用
2. 删除"输入清单"中的速查表行
3. 改 4 步工作流（删除 Read 速查表）
4. 改 §0 主代理前置检查
5. 改 §3.5：删除开头段 + 改 12 份 references 括号
6. 改 §5 D7
7. 改 §七 Files to Execute：删除速查表行 + "主代理合并后的正式笔记"行
8. 改 §八 文档关系图
9. 改 v2 引用块的段 6/段 8
10. 改"本规范自身"块的速查表引用
"""
from pathlib import Path

BASE = Path(r"c:\Users\Administrator\Desktop\623 11\优化Batch子代理输入\documents\sub-agent-deliverables")
TIMESTAMP = "2026-06-23 12:50"

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

# 12 份 references 的填入建议映射
REF_FILLS = {
    "subtype_decision_tree.md": "9 大子类型决策表 / 9 类作品特征与判定流程可填入",
    "r18_elements_library.md": "R18 元素库 / 各子型专属 R18 元素清单可填入",
    "quality_weight_rubric.md": "质量打分标尺 / 1-10 分判定标准与分档依据可填入",
    "multi_subtype_blend.md": "多子类型融合模式 / 5 种经典融合 + 冲突清单可填入",
    "extraction_creatures.md": "榨精生物图鉴 / 各类榨精生物特征 + 战斗模式可填入",
    "extraction_tools.md": "榨精道具库 / 各类榨精道具外形 + 使用方法可填入",
    "body_data_card_extended.md": "数据卡 8-10 项扩展 / 身高体重等 5+5 项字段值可填入",
    "subtype_priority_guide.md": "子类型优先级 / 6 批量 → 9 子类型建议权重可填入",
    "boundary_handling_sop.md": "边界处理 SOP / R1/R2/R3 命中处理流程可填入",
    "rhythm_subtype_specifics.md": "节奏子类型特化 / 各子型专属节奏模板可填入",
    "vocabulary_subtype_specifics.md": "词汇子类型特化 / 各子型专属词汇与对白风格可填入",
    "extraction_methods.md": "榨精方式指南 / 榨精手法 + 龟责技巧 + 边缘控制技巧可填入",
}


def fix_spec(file_path: Path) -> dict:
    text = file_path.read_text(encoding="utf-8")
    original = text
    changes = []

    # === 1. 头部配套速查表引用 ===
    old1 = "> 配套：`速查表_batch-XX_XXX.md`（仅做分配）+ `tmp/execution_packets.md`（小说元数据）"
    if old1 in text:
        text = text.replace(old1, "")
        changes.append("头部：删除'配套速查表'引用")

    # 2a. 头部 batch-XX 形式的引用 — 通用模式：去掉"配套速查表"行
    import re
    pattern1 = r">\s*配套：\s*`速查表_batch-[^`]+`（[^）]+）\s*([+\s]+\s*`tmp/execution_packets\.md`（[^）]+）)?\s*\n"
    m = re.search(pattern1, text)
    if m:
        text = re.sub(pattern1, "", text, count=1)
        changes.append("头部：删除速查表配套行（正则）")

    # === 2. 输入清单：删"文档 1 速查表"行 + 调整 4 步工作流 ===
    # 删整行：| 文档 1 | 速查表 | ... | ... |
    pattern_input = r"\|\s*文档\s*1\s*\|\s*速查表\s*\|[^|]*\|[^|]*\|\s*\n"
    if re.search(pattern_input, text):
        text = re.sub(pattern_input, "", text, count=1)
        changes.append("输入清单：删除'文档 1 速查表'行")

    # 调整"输入由 3 部分组成" -> "2 部分"
    text = re.sub(
        r"\*\*本 sub-agent 的输入由\s*3\s*部分组成\*\*：",
        "**本 sub-agent 的输入由 2 部分组成**：",
        text,
    )
    changes.append("输入清单：3 部分 -> 2 部分")

    # 4 步工作流：步骤 1 Read 速查表 -> 删步骤 1 整体（保留 Read 输入输出规范为第 1 步）
    # 原：
    # 1. **Read** 速查表 → 找到自己的 SA-XX-X
    # 2. **Read** 输入输出规范（同目录配套文件）→ 了解执行模式 + 灵活模板
    # 3. **Read** 源小说（按速查表指定路径...）
    # 4. **Write** 草稿...
    # 改：
    # 1. **Read** 输入输出规范（本文件）→ 了解执行模式 + 灵活模板 + 9 段结构
    # 2. **Read** 源小说（按子类型对应路径，在小说文件夹内；单段 ≤500KB 直接读，超 500KB 的子段用 `offset`/`limit` 分段）
    # 3. **Write** 草稿（按 SA-XX-X 指定的 4.X / 5.X 段）
    # 3 步工作流
    old_workflow = (
        "**sub-agent 4 步工作流**：\n"
        "\n"
        "1. **Read** 速查表 → 找到自己的 SA-XX-X\n"
        "2. **Read** 输入输出规范（同目录配套文件）→ 了解执行模式 + 灵活模板\n"
        "3. **Read** 源小说（按速查表指定路径，在小说文件夹内；单段 ≤500KB 直接读，超 500KB 的子段用 `offset`/`limit` 分段）\n"
        "4. **Write** 草稿（按 SA-XX-X 指定的 4.X / 5.X 段）\n"
    )
    new_workflow = (
        "**sub-agent 3 步工作流**：\n"
        "\n"
        "1. **Read** 输入输出规范（本文件）→ 了解执行模式 + 灵活模板 + 9 段标准结构\n"
        "2. **Read** 源小说（按子类型对应路径，在小说文件夹内；单段 ≤500KB 直接读，超 500KB 的子段用 `offset`/`limit` 分段）\n"
        "3. **Write** 草稿（按 SA-ID 指定的 4.X / 5.X 段）\n"
    )
    if old_workflow in text:
        text = text.replace(old_workflow, new_workflow)
        changes.append("工作流：4 步 -> 3 步，删 Read 速查表")

    # === 3. §0 主代理前置检查 ===
    # Step 0 第 1 步："Read 速查表（统一 1 次/批次）"  -> "Read 本规范（统一 1 次/批次）"
    text = re.sub(
        r"1\.\s*Read\s*速查表（统一\s*1\s*次/批次）",
        "1. Read 本规范（统一 1 次/批次）",
        text,
    )
    # Step 0 第 3 步："将速查表内容 + 本规范嵌入 sub-agent `message` 字段" -> "将本规范嵌入 sub-agent `message` 字段"
    text = re.sub(
        r"3\.\s*将速查表内容\s*\+\s*本规范嵌入 sub-agent `message` 字段",
        "3. 将本规范嵌入 sub-agent `message` 字段",
        text,
    )
    changes.append("§0：改主代理前置检查")

    # === 4. §3.5 删除开头段（4 行） + 改 12 份 references 括号 ===
    # 删除"### 3.5 12 份可选增量 references 建议"下方的 5 行说明（v5 增量 + v6 增量 + 候选清单...）
    old_35_header = (
        "### 3.5 12 份可选增量 references 建议\n"
        "\n"
        "> 草稿做完后，用户会基于深度阅读笔记决定是否新增以下 references 到 xiaoyingxiong skill。本节是**候选清单**，**不**是必含。\n"
        ">\n"
        "> v5 增量：**删除** `sibling_dynamic_patterns.md`（兄弟/双子 互动模式），保留 `extraction_creatures.md` + `extraction_tools.md`（v4 英文名统一）。  \n"
        "> **v6 增量**：新增 `extraction_methods.md`（榨精方式指南 — 榨精手法 / 龟责技巧 / 边缘控制技巧 等）。\n"
        "\n"
    )
    if old_35_header in text:
        text = text.replace(
            old_35_header,
            "### 3.5 12 份可选增量 references 建议\n"
            "\n"
            "**填入规则**：AI 根据本小说实际内容，从下方 12 份候选 references 中**挑选 2-5 份**作为本次升级建议；每份括号内为可填入内容方向。\n"
            "\n",
        )
        changes.append("§3.5：改开头段为'填入规则'")

    # 改 12 份 references 括号
    for fname, fill in REF_FILLS.items():
        # 匹配 `xxx.md`（**简介**：xxx） 或 `xxx.md`（xxx）
        # 处理带 **简介** 前缀的
        old_a = f"`{fname}`（**简介**："
        old_b = f"`{fname}`（"
        # 用更精确的方式：直接抓 `xxx.md`（...）整段
        for old_prefix in [f"`{fname}`（**简介**：", f"`{fname}`（**新增**：", f"`{fname}`（"]:
            idx = text.find(old_prefix)
            if idx == -1:
                continue
            # 找匹配的右括号（中文括号）
            close_idx = text.find("）", idx)
            if close_idx == -1:
                continue
            old_full = text[idx:close_idx + 1]
            # 新内容：保留文件名 + 填入建议
            if "**简介**" in old_prefix:
                new_full = f"`{fname}`（{fill}）"
            elif "**新增**" in old_prefix:
                new_full = f"`{fname}`（{fill}）"
            else:
                new_full = f"`{fname}`（{fill}）"
            text = text.replace(old_full, new_full, 1)
            changes.append(f"§3.5：改 {fname} 括号")

    # === 5. §5 D7 改 ===
    text = re.sub(
        r"\|\s*D7\s*\|\s*sub-agent 前置输入\s*\|\s*速查表\s*\+\s*本规范预填到 message\s*\|",
        "| D7 | sub-agent 前置输入 | 本规范预填到 message |",
        text,
    )
    changes.append("§5 D7：改 sub-agent 前置输入")

    # === 6. §七 Files to Execute ===
    # 删"速查表"行
    pattern_speed = r"\|\s*`[^`]*速查表_batch-[^`]+`\s*\|\s*\*\*读\*\*\s*\|[^|]*\|\s*\n"
    if re.search(pattern_speed, text):
        text = re.sub(pattern_speed, "", text, count=1)
        changes.append("§七：删速查表行")

    # 删"主代理合并后的正式笔记"行
    pattern_main = r"\|\s*`[^`]*pixiv_深度阅读笔记_[^`]+`[^|]*\|\s*\*\*写\*\*\s*\|\s*主代理合并后的正式笔记\s*\|\s*\n"
    if re.search(pattern_main, text):
        text = re.sub(pattern_main, "", text, count=1)
        changes.append("§七：删'主代理合并后的正式笔记'行")

    # 删"总速查表（旧版 v5，6 批量）"块
    pattern_old_speed = r">\s*\*\*总速查表（旧版 v5，6 批量）\*\*：[^>]+>\s*\n"
    if re.search(pattern_old_speed, text):
        text = re.sub(pattern_old_speed, "", text, count=1)
        changes.append("§七：删'总速查表'块")

    # === 7. §八 文档关系图 ===
    old_doc_rel = (
        "sub-agent分配速查表.md（仅做分配，含 SA-ID / 路径 / 章节 / 段号）\n"
        "        ↓\n"
        "sub-agent输入输出规范.md（本文件：执行模式 + 灵活模板 + 风险）"
    )
    new_doc_rel = (
        "sub-agent输入输出规范.md（本文件：执行模式 + 灵活模板 + 9 段结构 + 风险）"
    )
    if old_doc_rel in text:
        text = text.replace(old_doc_rel, new_doc_rel)
        changes.append("§八：改文档关系图")

    # === 8. v2 引用块 9 段标准结构表 ===
    # 段 6：每条 ≥ 200 字 -> 5-15条，每条 ≥ 200 字 ; 整理原文 + 权力结构 + 身体反应 + 心理反刍 -> 整理原文 + 身体反应 + 心理反刍
    old_seg6 = "|  6 | R18 元素        | **每条 ≥ 200 字** | 整理原文 + 权力结构 + 身体反应 + 心理反刍  |"
    new_seg6 = "|  6 | R18 元素        | **5-15条，每条 ≥ 200 字** | 整理原文 + 身体反应 + 心理反刍  |"
    if old_seg6 in text:
        text = text.replace(old_seg6, new_seg6)
        changes.append("v2 引用块：段 6 R18 元素对齐任务模板")

    # 段 8：写作技法 3-8 项 -> 每条 ≥ 200 字 ; 叙事装置 / 节奏 / 对话 / 视角 / 设定
    old_seg8 = "|  8 | 写作技法          |      3-8 项     | 叙事装置 / 节奏 / 对话 / 视角 / 设定   |"
    new_seg8 = "|  8 | 写作技法          | **每条 ≥ 200 字** | 叙事装置 / 节奏 / 对话 / 视角 / 设定   |"
    if old_seg8 in text:
        text = text.replace(old_seg8, new_seg8)
        changes.append("v2 引用块：段 8 写作技法 → 每条 ≥ 200 字")

    # === 9. 头部"本规范自身"块中：删"本批配套速查表"行 ===
    pattern_self_speed = r">\s*\*\*本批配套速查表\*\*：[^>]+>\s*\n"
    if re.search(pattern_self_speed, text):
        text = re.sub(pattern_self_speed, "", text, count=1)
        changes.append("头部：删'本批配套速查表'行")

    # === 10. 更新最后更新时间戳 ===
    text = re.sub(
        r"\*\*最后更新\*\*：2026-06-23 12:50",
        f"**最后更新**：{TIMESTAMP}",
        text,
    )
    # 同步 v2 引用块时间戳
    text = re.sub(
        r"v2 任务模板同步状态（2026-06-23 12:50）",
        f"v2 任务模板同步状态（{TIMESTAMP}）",
        text,
    )

    if text != original:
        file_path.write_text(text, encoding="utf-8")
    return {"file": file_path.name, "changes": changes, "modified": text != original}


def main():
    print(f"=== 综合修改 8 份输入输出规范 @ {TIMESTAMP} ===\n")
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
