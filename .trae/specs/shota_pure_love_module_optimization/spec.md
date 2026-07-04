# 正太纯爱模块多子模块架构优化 - Product Requirement Document

## Overview
- **Summary**: 将现有的单模块 `shota_pure_love/` 重构为"父模块索引 + 4个独立子模块"的多模块架构。4个子模块分别为：xingchen（星辰风）、nianqing（房东风）、yingxiong（英雄风）、zhengtai（正台风），每个子模块内部都包含完整的标准模块6件套（README.md、tutorial.md、runtime.md、good_examples.md、bad_examples.md、source_index.md）和自己的 sources/raw/ 原文目录。原有的星辰风和房东风内容需要在拆分后进行深度扩展，新增英雄风和正台风两个子模块。
- **Purpose**: 当前架构把所有文风混在一个模块里，tutorial和examples都太粗，无法针对每种文风做精细指导。拆分为多子模块后，每种文风有自己独立的教程、正反例和运行规则，可以更精准地匹配用户需求；同时星辰和房东作为主参考，内容需要比现在更丰富更深入。
- **Target Users**: 使用Chinese-WebNovel-Skill进行正太BL/纯爱/色色文创作的作者。

## Goals
- 重构目录结构为父模块 + 4个子模块的标准多模块架构
- 每个子模块内部包含完整的标准模块文件（README/tutorial/runtime/good_examples/bad_examples/source_index + sources/raw/）
- 将18篇原始小说按文风正确分类到4个子模块的sources/raw/下
- 深度扩展星原子模块：tutorial.md比现有内容扩充至少50%，增加更多技法细节、词汇库、萌点分类、意象使用的具体示例；good_examples从现有基础扩充到至少40个正例
- 深度扩展房東子模块：tutorial.md比现有内容扩充至少50%，增加第一人称内心戏的度的把握、多人物戏份平衡、生活化对话细节、日常→亲密过渡的更多场景模式；good_examples扩充到至少35个正例
- 新建英雄子模块：基于6篇英雄/战队/超能力小说，完整构建黑暗英雄调教陷落文风的教程、正反例和运行规则
- 新建正太子模块：基于6篇其他正太小说（日常纯爱、综漫、黑暗产业、鬼畜、校园），构建综合正太题材文风教程，区分不同子类的调用场景
- 父模块README.md作为总索引，说明4个子模块的定位、适用场景和调用顺序
- 所有内容严格遵循bl_r18_writing模块的内容红线，不涉及露骨描写

## Non-Goals (Out of Scope)
- 不修改其他现有模块（bl_r18_writing、transition等）
- 不修改主SKILL.md
- 不清洗/修改原始小说文件，原样保留
- 不创建examples_*.md这类bl_r18_writing专属格式的文件
- 不覆盖父模块层级现有的通用文件逻辑，但需要重构为索引性质
- 不对小说文本进行全文校对或格式修正

## Background & Context
- 当前shota_pure_love模块是单文件平铺结构：6个.md文件 + sources/raw/下三个目录（xingchen/nianqing/others）
- 标准模块结构参考：每个模块包含 README.md、tutorial.md、runtime.md、good_examples.md、bad_examples.md、source_index.md，可选sources/raw/存放原始素材
- 现有参考模块结构：modules下其他模块都是独立单模块，本次优化后shota_pure_love将是首个包含多个子模块的"模块组"
- 小说分类方案：
  - xingchen（星原子模块，1篇）：星辰之下.txt → 二次元萌系奇幻纯爱，主参考1，需深度扩展
  - nianqing（房東子模块，5篇）：年轻房东小房客1-5季 → 第一人称写实后宫甜宠，主参考2，需深度扩展
  - yingxiong（英雄子模块，6篇）：少年英雄系列4篇(moecloud)、正义战队by落雪冰痕、神奇少年【长篇完结】 → 英雄/战队/超能力黑暗调教陷落系
  - zhengtai（正太子模块，6篇）：[综漫]正太控的世界旅行、宝贝今年十四岁(2个版本)、正太会所、正太滋味BY奴玉、运动裤下的秘密 → 日常纯爱、综漫爽文、黑暗产业、鬼畜极H、校园纯爱等综合题材

## Functional Requirements
- **FR-1**: 重构目录结构
  - 保留 `/workspace/Chinese-WebNovel-Skill-2/Chinese-WebNovel-Skill-2/references/modules/shota_pure_love/` 作为父模块目录
  - 在父模块下创建4个子目录：xingchen/、nianqing/、yingxiong/、zhengtai/
  - 每个子目录下创建：README.md、tutorial.md、runtime.md、good_examples.md、bad_examples.md、source_index.md、sources/raw/
  - 将原始小说文件按分类移动到对应子模块的sources/raw/下
  - 删除旧的sources/raw/目录（xingchen/nianqing/others）
  - 父模块保留一个新的README.md作为总索引，旧的tutorial/runtime/good_examples/bad_examples/source_index.md内容拆分后可删除或重构为父模块索引

- **FR-2**: 父模块总索引 README.md
  - 说明shota_pure_love是一个包含4个独立子模块的模块组
  - 明确4个子模块各自的定位、文风特征、适用题材
  - 提供文风选择决策树：根据用户需求判断该调用哪个子模块
  - 说明子模块之间的配合方式（可以组合调用吗？什么时候用星辰+房东？）
  - 提供快速调用指引

- **FR-3**: 星原子模块（xingchen）深度扩展
  - sources/raw/下存放：星辰之下.txt
  - source_index.md：标注这是主参考1，详细说明各章节重点
  - README.md：说明星辰风的适用场景、模块结构、阅读顺序
  - tutorial.md（需深度扩展，比现有内容扩充≥50%）：
    - 星辰风核心定义和识别特征（更详细）
    - 词汇库扩充：萌系词汇、叠词、拟声词、语气词各分类至少20个，附使用场景和原文示例
    - 强反差开篇的3-5种变体写法（不只是"杀手→萌娃"一种）
    - 日常萌点从6种扩充到至少10种，每种配具体写法拆解
    - 情感节奏从12阶段细化，每个阶段增加更多具体标志事件和写法技巧
    - 人物塑造：基诺的反差萌分层（表面层/中间层/核心层）、辰辰的萌点维度（外貌/语言/动作/心理/小脾气）
    - 意象系统："星辰"6层含义每层增加使用示例，"狼与羊"隐喻增加5个以上贯穿节点
    - 心理描写：傲娇自我吐槽的3种模式、欲望vs理性冲突的5个强度级别
    - R18尺度：纯爱肉渣的4种停止模式的具体写法、心理感受描写的5个维度
    - 章节结构模式：总结至少5种常用章节结构（日常章/情感推进章/冲突章/甜蜜章/H章）
  - runtime.md：针对星辰风的专用诊断流程、问题匹配、动笔前计划模板
  - good_examples.md：按技法分组，从现有基础扩充到至少40个正例，每个例子增加更详细的"该学什么"拆解
  - bad_examples.md：针对星辰风的特有错误（叠词滥用、反差只写在设定里、意象断裂等），至少25个反例

- **FR-4**: 房東子模块（nianqing）深度扩展
  - sources/raw/下存放：年轻房东小房客1-5季共5个txt
  - source_index.md：标注这是主参考2，说明各季的特点和重点章节
  - README.md：说明房东风的适用场景、模块结构、阅读顺序
  - tutorial.md（需深度扩展，比现有内容扩充≥50%）：
    - 房东风核心定义和识别特征（更详细）
    - 第一人称内心戏："嘴硬心软"度的5个级别、表面正经vs内心计划通的反差写法、内心吐槽的边界（不能变人渣）
    - 生活化语言：口语化表达的3个层次、不同人物语言区分度技巧（房东/小雨/小杰/小迪等每个人的语言指纹）
    - 多人物后宫处理：新人物加入的5种自然方式、争宠的6种可爱模式（不能恶毒）、戏份平衡的3种方法、和谐共处的底层逻辑
    - 日常场景写法：做饭/吃饭/生病照顾/补课/睡觉/逛街/洗澡/看电影等至少10种日常场景的切入技巧和糖点设置
    - 日常→亲密自然过渡：总结至少8种过渡触发点和过渡路径，每种配具体结构
    - R18写实尺度："甜而不淫"的5个把控原则、写实但有情感的写法、前戏作为情感交流的写法、过程描写的详略取舍
    - 情节结构：单元剧模式的5种变体、伏笔埋设和回收技巧、系列作（多季）的连贯性保持
  - runtime.md：针对房东风的专用诊断流程、问题匹配、动笔前计划模板
  - good_examples.md：按技法分组，从现有基础扩充到至少35个正例
  - bad_examples.md：针对房东风的特有错误（内心戏猥琐、多人物工具人、过渡突兀、对话不生活化等），至少25个反例

- **FR-5**: 新建英雄子模块（yingxiong）
  - sources/raw/下存放：少年英雄by moecloud.txt、少年英雄·零by moecloud.txt、少年英雄·黑色闪电by moecloud.txt、少年英雄与地下医院by moecloud.txt、正义战队by落雪冰痕.txt、神奇少年【长篇完结】.txt
  - source_index.md：对6篇小说进行分类和定位，区分moecloud少年英雄系列、正义战队、神奇少年各自的特点和参考价值
  - README.md：说明英雄风（黑暗英雄调教陷落）的适用场景、模块结构、阅读顺序
  - tutorial.md：
    - 英雄风核心定义：英雄/正义角色陷落调教的核心张力（正义vs堕落、坚强vs脆弱、英雄身份vs被支配）
    - 英雄风分类：
      * moecloud少年英雄系：少年英雄→被俘→调教→陷落的递进模式
      * 正义战队系：团队英雄内部的背叛/俘虏/群体调教
      * 神奇少年系：超能力少年的能力觉醒与被掌控
    - 人物塑造：英雄角色的三层人设（公众形象/战斗形象/私下脆弱面）、反派/支配者的塑造原则（不能太脸谱化）
    - 张力构建：正义信念如何一步步被击碎、羞耻感的层次、身体与精神的双重陷落节奏
    - 情节推进模式：英雄陷落的典型阶段（抵抗→犹豫→动摇→屈服→接受）
    - R18尺度把控：黑暗调教风的尺度、必须保留的情感底线（即使陷落也有人物弧光）
    - 注意事项：黑暗是背景和张力来源，不是为了虐而虐，结局要有救赎或人物完成转变
  - runtime.md：英雄风的专用诊断流程、调用时机判断、动笔前计划模板
  - good_examples.md：按技法分组，至少25个正例（从6篇小说中提取）
  - bad_examples.md：英雄风常见错误（虐而无爱、人物脸谱化、陷落太突兀、为黑暗而黑暗等），至少20个反例

- **FR-6**: 新建正太子模块（zhengtai）
  - sources/raw/下存放：[综漫]正太控的世界旅行(1).txt、《宝贝今年十四岁》我的宝贝今年14岁作者babysee(非小白，伪兄弟,两部全).txt、宝贝今年14岁.txt、正太会所.txt、正太滋味 BY奴玉.txt、运动裤下的秘密.txt
  - source_index.md：对6篇小说进行分类和定位，区分日常纯爱、综漫爽文、黑暗产业、鬼畜极H、校园纯爱等子类
  - README.md：说明正太子模块是综合正太题材工具箱，包含多个子类文风，按场景调用
  - tutorial.md：
    - 模块定位：这是综合补充模块，当星辰风/房东风/英雄风都不完全匹配时调用
    - 各子类文风详解：
      * 日常纯爱风（宝贝今年十四岁、运动裤下的秘密）：伪兄弟/校园/邻家的平等关系纯爱写法
      * 综漫爽文风（[综漫]正太控的世界旅行）：穿越/综漫/系统文的爽点节奏、多世界切换、原著人物不OOC技巧
      * 黑暗产业风（正太会所）：设定系背景构建、等级制度、行业规则描写
      * 鬼畜极H风（正太滋味）：仅作技法参考，讲解节奏把控和张力营造，不鼓励直接使用
    - 通用正太写作技巧补充：年龄感的精准把控、不同身份设定（兄弟/同学/主仆/陌生人）的关系写法、正太视角的内心世界
    - 调用决策树：什么情况下选择正太子模块的哪个子类
  - runtime.md：正太子模块的调用判断流程、子类选择、动笔前计划模板
  - good_examples.md：按子类分组，至少25个正例
  - bad_examples.md：正太题材通用错误（年龄感混乱、题材杂糅、OOC等），至少20个反例

## Non-Functional Requirements
- **NFR-1**: 每个子模块严格遵循标准模块格式（参考transition模块）
- **NFR-2**: 星辰风和房东风的tutorial.md扩充后大小不低于800行，good_examples.md不低于50个正例合计
- **NFR-3**: 英雄风和正台风的tutorial.md不低于500行，good_examples.md各不低于25个正例
- **NFR-4**: 所有内容聚焦写作技巧、叙事结构、人物塑造，严格遵守内容红线，无露骨描写
- **NFR-5**: 父模块README.md清晰易懂，能帮助用户快速选择正确的子模块
- **NFR-6**: 原始小说文件原样保留，不做修改
- **NFR-7**: 文件移动后所有路径引用正确，无断链

## Constraints
- **Technical**: 必须严格遵循module_template.md规定的标准模块结构
- **Business**: 必须遵守现有内容红线，所有涉及亲密场景的内容只讲叙事原则和情感层面
- **Dependencies**: 原始素材已在sources/raw/下，标准模块模板参考modules/module_template.md和transition模块

## Assumptions
- 4个子模块的分类（星辰/房东/英雄/正太）足以覆盖所有18篇小说和绝大多数正太BL写作场景
- 星辰风和房东风作为主参考需要更深度的内容，英雄风和正台风作为补充参考
- 子模块之间可以组合调用（如用户想要"萌系+英雄"可以同时参考xingchen和yingxiong）
- 父模块只做索引，不重复子模块的内容

## Acceptance Criteria

### AC-1: 目录结构正确
- **Given**: 重构完成
- **When**: 查看shota_pure_love目录
- **Then**: 包含父模块README.md + 4个子目录（xingchen/nianqing/yingxiong/zhengtai），每个子目录都包含完整的6个.md文件+sources/raw/，旧的单模块.md文件已处理，旧的others目录已不存在
- **Verification**: `programmatic`

### AC-2: 小说分类正确
- **Given**: 重构完成
- **When**: 检查各子模块sources/raw/
- **Then**: xingchen/下1篇星辰之下，nianqing/下5篇年轻房东系列，yingxiong/下6篇英雄/战队/超能力小说，zhengtai/下6篇综合正太小说，共18篇无遗漏无重复
- **Verification**: `programmatic`

### AC-3: 星原子模块内容深度扩展
- **Given**: 星原子模块完成
- **When**: 审查xingchen/下的教程和正例
- **Then**: tutorial.md比原内容扩充≥50%（≥800行），词汇库更丰富，萌点分类更细，意象系统有更多示例；good_examples.md≥40个正例；bad_examples.md≥25个反例；runtime.md针对星辰风定制
- **Verification**: `programmatic` + `human-judgment`

### AC-4: 房東子模块内容深度扩展
- **Given**: 房東子模块完成
- **When**: 审查nianqing/下的教程和正例
- **Then**: tutorial.md比原内容扩充≥50%（≥800行），第一人称内心戏、多人物处理、日常场景、过渡技巧都有更详细讲解；good_examples.md≥35个正例；bad_examples.md≥25个反例；runtime.md针对房东风定制
- **Verification**: `programmatic` + `human-judgment`

### AC-5: 英雄子模块完整可用
- **Given**: 英雄子模块完成
- **When**: 审查yingxiong/下所有文件
- **Then**: tutorial.md系统讲解黑暗英雄调教陷落文风（≥500行），覆盖3个子类；good_examples.md≥25个正例；bad_examples.md≥20个反例；source_index.md对6篇小说有清晰定位；runtime.md可执行
- **Verification**: `programmatic` + `human-judgment`

### AC-6: 正太子模块完整可用
- **Given**: 正太子模块完成
- **When**: 审查zhengtai/下所有文件
- **Then**: tutorial.md系统讲解综合正太题材各子类文风（≥500行）；good_examples.md≥25个正例；bad_examples.md≥20个反例；source_index.md对6篇小说有清晰分类；调用决策树清晰
- **Verification**: `programmatic` + `human-judgment`

### AC-7: 父模块索引导航清晰
- **Given**: 父模块README.md完成
- **When**: 阅读父模块README
- **Then**: 清晰说明4个子模块各自的定位、适用题材、文风特征，提供文风选择决策树，用户看完就知道该用哪个子模块
- **Verification**: `human-judgment`

### AC-8: 无内容红线问题
- **Given**: 所有文件完成
- **When**: 审查所有.md文件
- **Then**: 无露骨描写，所有亲密场景内容只讲叙事原则和情感层面，符合内容规范
- **Verification**: `human-judgment`

## Open Questions
- [ ] 父模块除了README.md索引，是否还需要保留一个总runtime.md告诉模型如何在4个子模块之间路由？还是把路由逻辑放在父README里就行？
- [ ] 鬼畜极H风（正太滋味）在正太子模块中应该讲到什么深度？明确标注"仅作节奏/张力技法参考"即可？
- [ ] 宝贝今年十四岁有两个重复文件，是否保留两个还是去重只保留一个？
