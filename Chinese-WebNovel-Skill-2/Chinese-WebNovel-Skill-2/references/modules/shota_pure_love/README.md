# 正太纯爱文风模块组

这是一个包含4个独立子模块的模块组，每个子模块针对一种特定的正太BL文风。它们各自是完整独立的标准模块，可单独调用，也可组合使用。

## 子模块概览

| 子模块 | 文风名称 | 叙事视角 | 核心特征 | 适用题材 | 小说篇数 |
|--------|----------|----------|----------|----------|----------|
| [xingchen/](xingchen/) | 星辰风（二次元萌系奇幻纯爱） | 第三人称有限视角 | 强反差开篇、萌系语言、纯爱肉渣、意象贯穿 | 奇幻/杀手/萌系纯爱/单CP | 1篇（主参考） |
| [nianqing/](nianqing/) | 房东风（第一人称写实后宫甜宠） | 第一人称 | 内心吐槽嘴硬心软、生活化对话、多人物和谐后宫、日常→亲密自然过渡 | 现代/日常/后宫/甜宠 | 5篇（主参考） |
| [yingxiong/](yingxiong/) | 英雄风（黑暗英雄调教陷落） | 第三人称 | 正义vs堕落张力、英雄信念逐步击碎、羞耻感层次、人物弧光 | 英雄/战队/超能力/黑暗调教 | 6篇（补充） |
| [zhengtai/](zhengtai/) | 正台风（综合正太题材工具箱） | 多种视角 | 覆盖日常纯爱/综漫爽文/黑暗产业/鬼畜极H等子类 | 校园/伪兄弟/综漫/设定系等综合题材 | 6篇（补充） |

## 文风选择决策树

按以下问题顺序判断，快速锁定最适合的子模块：

1. **你要写萌系/奇幻/单CP纯爱？** → 选 [xingchen/](xingchen/)（星辰风）
2. **你要写第一人称/现代日常/后宫甜宠？** → 选 [nianqing/](nianqing/)（房东风）
3. **你要写英雄/正义角色陷落/黑暗调教？** → 选 [yingxiong/](yingxiong/)（英雄风）
4. **你要写校园/伪兄弟/综漫/会所设定？** → 选 [zhengtai/](zhengtai/)（正台风）

## 子模块组合调用

当单一子模块不能满足需求时，可组合调用：

- 想要**萌系+英雄**：xingchen + yingxiong
- 想要**多人物但萌系**：xingchen + nianqing
- 想要**黑暗但有纯爱救赎**：yingxiong + xingchen
- **不确定具体风格**：先看本README决策树，再进入对应子模块

## 推荐使用顺序

无论选择哪个子模块，都建议按以下顺序使用：

1. 根据题材选择对应子模块
2. 进入子模块先读 README.md 了解该文风
3. 再读 source_index.md 了解素材分布
4. 需要系统学习时读 tutorial.md
5. 写作/改稿时按 runtime.md 流程诊断问题
6. 去 good_examples.md 找近似正例，bad_examples.md 避坑
7. 动笔前先按子模块runtime写写作计划

## 文件结构

```text
shota_pure_love/
├── README.md                 ← 你在这里（模块组总索引）
├── xingchen/                 ← 子模块1：星辰风
│   ├── README.md
│   ├── tutorial.md
│   ├── good_examples.md
│   ├── bad_examples.md
│   ├── runtime.md
│   ├── source_index.md
│   └── sources/raw/
├── nianqing/                 ← 子模块2：房东风
│   ├── README.md
│   ├── tutorial.md
│   ├── good_examples.md
│   ├── bad_examples.md
│   ├── runtime.md
│   ├── source_index.md
│   └── sources/raw/
├── yingxiong/                ← 子模块3：英雄风
│   ├── README.md
│   ├── tutorial.md
│   ├── good_examples.md
│   ├── bad_examples.md
│   ├── runtime.md
│   ├── source_index.md
│   └── sources/raw/
└── zhengtai/                 ← 子模块4：正台风
    ├── README.md
    ├── tutorial.md
    ├── good_examples.md
    ├── bad_examples.md
    ├── runtime.md
    ├── source_index.md
    └── sources/raw/
```

## 注意事项

- **主参考优先级**：星辰风和房东风是主参考，覆盖80%以上常见正太纯爱写作场景
- **补充参考定位**：英雄风和正台风是补充参考，用于特定题材
- **内容边界**：所有内容聚焦写作技巧、风格把控、叙事结构、人物塑造，不涉及露骨描写
- **模块独立性**：每个子模块都是独立完整的标准模块，可单独调用，不需要依赖其他子模块
- **组合使用**：组合调用时，以主模块为基调，补充模块提供特定元素即可，不要混用核心叙事视角
