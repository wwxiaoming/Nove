"""
同步 v2.3.1 实时写入机制到 8 份批次规范文档
- 头部"最后更新"时间戳 → 17:00
- 在"## 📋 v2 任务模板同步状态"前插入"## ⚡ v2.3.1 实时写入同步"段
"""
import re
from pathlib import Path

# 8 份规范文档
SPECS = [
    r"c:\Users\Administrator\Desktop\623 11\优化Batch子代理输入\documents\sub-agent-deliverables\batch-01_战队特摄\输入输出规范_batch-01_战队特摄.md",
    r"c:\Users\Administrator\Desktop\623 11\优化Batch子代理输入\documents\sub-agent-deliverables\batch-02a_勇者魔物奇幻_前\输入输出规范_batch-02a_勇者魔物奇幻_前.md",
    r"c:\Users\Administrator\Desktop\623 11\优化Batch子代理输入\documents\sub-agent-deliverables\batch-02b_勇者魔物奇幻_后\输入输出规范_batch-02b_勇者魔物奇幻_后.md",
    r"c:\Users\Administrator\Desktop\623 11\优化Batch子代理输入\documents\sub-agent-deliverables\batch-03a_正太校园堕落_前\输入输出规范_batch-03a_正太校园堕落_前.md",
    r"c:\Users\Administrator\Desktop\623 11\优化Batch子代理输入\documents\sub-agent-deliverables\batch-03b_正太校园堕落_后\输入输出规范_batch-03b_正太校园堕落_后.md",
    r"c:\Users\Administrator\Desktop\623 11\优化Batch子代理输入\documents\sub-agent-deliverables\batch-04_调教拍卖+异种触手\输入输出规范_batch-04_调教拍卖+异种触手.md",
    r"c:\Users\Administrator\Desktop\623 11\优化Batch子代理输入\documents\sub-agent-deliverables\batch-05_修真玄幻+外语\输入输出规范_batch-05_修真玄幻+外语.md",
    r"c:\Users\Administrator\Desktop\623 11\优化Batch子代理输入\documents\sub-agent-deliverables\batch-06_同人+女性向\输入输出规范_batch-06_同人+女性向.md",
]

# v2.3.1 实时写入同步段（插入到"## 📋 v2 任务模板同步状态"前）
V231_SYNC_BLOCK = """## ⚡ v2.3.1 实时写入同步（2026-06-23 17:00）

> **本规范已与** **`00.工具/sub-agent任务模板_v1.md` v2.3.1** **同步**，新增**实时读取 + 实时写入**机制，避免上下文压力爆炸。

### 核心机制

- **读完即写，不积压**：每读完 1 部作品 / 1 个子段 / 3-5 章 → 立即 `Write` 1 份草稿 .md 落盘
- **N 部 = N 份草稿**：严禁全部读完统一写（**v2.3 实战：单 SA 读完 5 文件 + 4 份草稿后上下文超限，丢失早期细节**）
- **完成报告一次性**：N 份草稿写完 → 一次性向主代理回报 5 行完成报告（不穿插）

### 5 种分批读场景（步骤 3 实时分批）

| 场景 | 读完触发 | 写草稿动作 |
|---|---|---|
| **单部作品** | 单次 `Read` 完整读 | 立即写 1 份 .md |
| **多部聚合包** | 每读完 1 部 | 立即写 1 份 .md（N 部 = N 份）|
| **超限本子段（>500KB）** | 每读完 1 个 `offset/limit` 分段 | 立即写 1 份 .md |
| **多文件子段（#1-#13 系列）** | 每读完 1 个文件 | 立即追加写子段 .md（不阻塞）|
| **单文件 > 128KB 无分段** | 全读 | 先标章节数差值，再写 1 份 .md |

### 不要（v2.3 实战反面教材）

- ❌ 读完所有 N 部再统一写（上下文爆炸）
- ❌ 每读完一章写一份（碎片化过度）
- ❌ 边读边写（注意力分散，丢失关键细节）
- ❌ 把 N 份草稿堆到最后一次性回报（完成报告无意义）

> **完整 v2.3.1 任务模板**：[`00.工具/sub-agent任务模板_v1.md`](file:///c:/Users/Administrator/Desktop/623%2011/%E4%BC%98%E5%8C%96Batch%E5%AD%90%E4%BB%A3%E7%90%86%E8%BE%93%E5%85%A5/documents/sub-agent-deliverables/00.%E5%B7%A5%E5%85%B7/sub-agent%E4%BB%BB%E5%8A%A1%E6%A8%A1%E6%9D%BF_v1.md) §1 步骤 3-4

***

"""

# 头部"最后更新"时间戳正则（匹配各种时间，如 13:40 / 16:35 / 16:23 / 13:10）
HEADER_TIME_PATTERN = re.compile(r"^> \*\*最后更新\*\*：2026-06-23 \d{2}:\d{2}", re.MULTILINE)


def sync_spec(path: str) -> str:
    """同步单个规范文档，返回状态"""
    p = Path(path)
    if not p.exists():
        return f"[FAIL] 文件不存在: {path}"

    content = p.read_text(encoding="utf-8")

    # 1. 修改头部"最后更新"时间戳到 17:00
    new_content, count1 = HEADER_TIME_PATTERN.subn(
        "> **最后更新**：2026-06-23 17:00", content
    )
    if count1 == 0:
        return f"[FAIL] {p.name}: 未找到头部'最后更新'时间戳"

    # 2. 在"## 📋 v2 任务模板同步状态"前插入 v2.3.1 同步段
    # 避免重复插入（用唯一标记）
    marker = "## ⚡ v2.3.1 实时写入同步（2026-06-23 17:00）"
    if marker in new_content:
        result = "已存在 v2.3.1 同步段"
    else:
        # 找到"## 📋 v2 任务模板同步状态"的位置
        target = "## 📋 v2 任务模板同步状态"
        if target not in new_content:
            return f"[FAIL] {p.name}: 未找到 '{target}' 段"
        # 在该段前插入 v2.3.1 同步段
        new_content = new_content.replace(
            target,
            V231_SYNC_BLOCK + target,
            1
        )
        result = f"插入 v2.3.1 同步段"

    # 3. 写回
    p.write_text(new_content, encoding="utf-8")

    return f"[OK] {p.name}: {result} (头部时间戳更新: {count1} 处)"


def main():
    print("=" * 80)
    print("v2.3.1 实时写入同步脚本 — 8 份批次规范")
    print("=" * 80)
    success = 0
    fail = 0
    for spec in SPECS:
        msg = sync_spec(spec)
        print(msg)
        if "[OK]" in msg:
            success += 1
        else:
            fail += 1
    print("=" * 80)
    print(f"总计: 成功 {success} / 失败 {fail} / 共 8 份")
    print("=" * 80)


if __name__ == "__main__":
    main()
