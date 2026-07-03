# Sub-agent 任务模板（v1 通用版）

> 适用：pixiv 深度阅读笔记的 4.X/5.X 段批量分析 sub-agent 派发
> 更新：2026-06-22（基于 batch-02b 13 sub-agent 实战总结）

---

## 📋 模板（复制后填 `{}` 占位符）

```markdown
你是 sub-agent **{SA_ID}**。

**任务**：通读下列 {N} 部小说（共 {TOTAL_KB} KB / {TOTAL_CH} 章），按 9 段标准结构写分析草稿到笔记的 {TARGET_SECTION} 段。

**步骤 1：定位源小说**（速查表给的路径前缀可能不存在）
```bash
ls /workspace/pixiv小说/{CATEGORY}/{WORK_DIR_1}/
ls /workspace/pixiv小说/{CATEGORY}/{WORK_DIR_2}/
# 实际路径前缀 = /workspace/pixiv小说/（不是 /workspace/帝王战队621 1：00/）
```

**步骤 2：读 2 份输入文档**（必须按此顺序）：
1. `/workspace/documents/sub-agent-deliverables/{BATCH_DIR}/速查表_{BATCH_DIR}.md`
2. `/workspace/documents/sub-agent-deliverables/{BATCH_DIR}/输入输出规范_{BATCH_DIR}.md`

**步骤 3：读源小说全部 {TOTAL_CH} 章**（单文件 >128KB 用 offset/limit 分段读）

**绝对禁止**：
- 不要读 `/workspace/深度阅读笔记/` 下任何文件
- 不要读其他 sub-agent 的源小说
- 不要读 references/ 下的标准答案文件

**硬要求**（v2 SKILL 升级建议 ≥ {SKILL_REQ} 条，3 大雷点 R1/R2/R3 明确判定）

---

### 源小说清单

| # | 作品 | 路径 | 章节数 | 大小 |
|---|---|---|---|---|
| 1 | {WORK_1} | `/workspace/pixiv小说/{CATEGORY}/{WORK_DIR_1}/` | {CH_1} | {KB_1} |
| 2 | {WORK_2} | `/workspace/pixiv小说/{CATEGORY}/{WORK_DIR_2}/` | {CH_2} | {KB_2} |

---

### 9 段标准结构（每部都写一套）

写到笔记的 {TARGET_SECTION}.X 段（X = 1, 2, 3, ...）：

1. **{TARGET_SECTION}.X.1 作品定位**：类型 / 流派 / 情绪 / 读者画像
2. **{TARGET_SECTION}.X.2 关键章节**（表格）：章节号 / 标题 / R18 浓度 / 剧情浓度 / 核心看点
3. **{TARGET_SECTION}.X.3 完整套路**（5-10 段）：核心叙事模式 + 反转节点 + 情绪曲线
4. **{TARGET_SECTION}.X.4 关键场景**（3-8 个）：场景名 / 位置 / 设定 / 核心动作 / 重要性
5. **{TARGET_SECTION}.X.5 角色弧光**（3-7 角色）：姓名 / 出场章节 / 弧光轨迹 / 与其他角色关系
6. **{TARGET_SECTION}.X.6 R18 元素**（3-8 条，**每条 ≥200 字**）：整理原文 + 权力结构 + 身体反应 + 心理反刍
7. **{TARGET_SECTION}.X.7 雷点命中**（R1/R2/R3 明确判定，证据 + 强度）
8. **{TARGET_SECTION}.X.8 写作技法**（3-8 项）：叙事装置 / 节奏 / 对话 / 视角 / 设定
9. **{TARGET_SECTION}.X.9 v2 SKILL 升级建议**（≥ {SKILL_REQ} 条）：具体可操作 + 对应输出模板改动

---

### 输出草稿路径

`/workspace/documents/sub-agent-deliverables/02.batch草稿/pixiv小说_{BATCH_TAG}_SA-{SA_ID}_{WORK_NAME}.md`

---

### 完成报告（极简版，**不输出 9 段结构和关键发现**）

```markdown
## {SA_ID} 完成报告
- **处理小说**：{N} 部（{WORK_LIST}）
- **实际读取章节**：X / {TOTAL_CH} 章
- **草稿路径**：{OUTPUT_PATH}
- **实际输出字符**：~XXXXX
- **异常情况**：（如有；如实际读 < 100% 需说明原因）
```

---

## 🔧 关键经验（已固化到模板）

### 1. 路径别名问题
- **速查表写的**：`/workspace/帝王战队621 1：00/pixiv小说/...`
- **实际存在**：`/workspace/pixiv小说/...`（无前缀）
- **处理**：步骤 1 强制 ls 自适应，13 sub-agent 中 11 个遇到了这个问题

### 2. 输入输出规范文档可能"仅含标题"
- batch-02b 规范文档早期版本只写了标题，正文在速查表
- **处理**：把"执行模式"全部固化到模板，不再依赖规范文档

### 3. 章节数 vs 速查表标注可能不符
- 常见：T（12 vs 13）、X（失落骑士 -1 / 牧勇录 -19）、Z（18 vs 25）、W（27 vs 23）
- **处理**：模板要求"异常情况"必须说明差值与原因

### 4. 单章超 128KB 需分段
- U 的第 47 章 132KB → 6 次 offset 读
- **处理**：模板步骤 3 显式提示"单文件 >128KB 用 offset/limit"

### 5. R18 字数与雷点判定
- **v1 缺陷**：R18 条目 100-200 字偏短，无法承载"权力结构→身体反应→心理反刍"分析
- **v2 优化**：R18 每条 ≥200 字（已固化到模板）
- **3 大雷点**：R1/R2/R3 全部命中需附"证据 + 强度"，不允许"未触发"敷衍

### 6. 完成报告精简
- **v1 缺陷**：9 段结构 + 关键发现 = 报告占输出 1/3，浪费 token
- **v2 优化**：完成报告仅含 5 行基本信息（处理小说 / 章节数 / 路径 / 字符 / 异常）

### 7. 重复内容警告
- W 的"淫堕英雄大陆"已由 SA-02-K 完成 4.2 节整本分析
- **处理**：模板"步骤 1"前加注"如本子段与 4.X 段已分析作品重合，仅做串联观察不重复 R18 描写"

---

## 🎯 占位符说明

| 占位符 | 含义 | 示例 |
|---|---|---|
| `{SA_ID}` | Sub-agent 编号 | `SA-02-O` |
| `{N}` | 处理小说部数 | `1` / `2` / `3` / `4` |
| `{TOTAL_KB}` | 总大小 KB | `408.1` |
| `{TOTAL_CH}` | 总章节数 | `21` |
| `{TARGET_SECTION}` | 目标段号 | `4.2` / `5.1` |
| `{SKILL_REQ}` | v2 SKILL 升级建议条数（默认 2） | `2` / `3` |
| `{CATEGORY}` | pixiv 分类子目录 | `02_勇者魔物奇幻` |
| `{WORK_DIR_n}` | 小说文件夹名 | `少年骑士长的恶堕` |
| `{WORK_n}` | 作品名 | `《少年骑士长的恶堕》` |
| `{CH_n}` / `{KB_n}` | 单部章节数 / KB | `21` / `406.9` |
| `{BATCH_DIR}` | 批次文件夹 | `batch-02b_勇者魔物奇幻_后` |
| `{BATCH_TAG}` | 文件名批次标签 | `02b` |
| `{WORK_NAME}` | 草稿文件名后缀 | `少年骑士长的恶堕` |
| `{OUTPUT_PATH}` | 草稿完整路径 | `/workspace/documents/sub-agent-deliverables/02.batch草稿/...` |
| `{WORK_LIST}` | 作品列表简写 | `少年骑士长的恶堕` |

---

## 📊 已用此模板的批次

| 批次 | sub-agent 数 | 成功率 | 备注 |
|---|---|---|---|
| batch-02a | 13 | 13/13 | 第一版模板，部分 R18 <200 字、报告偏长 |
| batch-02b | 13 | 10/13 首派 → 13/13 重派后 | 路径问题 + 3 个 result missing |

**v2 模板成功率**：待下批次验证（batch-03 计划）
