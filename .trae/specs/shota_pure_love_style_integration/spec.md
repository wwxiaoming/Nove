# 正太纯爱文风模块 - Product Requirement Document

## Overview
- **Summary**: 在 `/workspace/Chinese-WebNovel-Skill-2/Chinese-WebNovel-Skill-2/references/modules/` 下新建独立的 `shota_pure_love` 专项模块，遵循标准模块结构（README/tutorial/runtime/good_examples/bad_examples/source_index + sources/raw）。将《星辰之下》《年轻房东小房客》及其他11篇正太BL小说作为文风素材，在sources/raw下分三个子目录存放原文：xingchen（星辰之下单独）、nianqing（年轻房东系列单独）、others（其他所有小说）。模块将总结三种主要文风体系：星辰风（二次元萌系奇幻纯爱）、房东风（第一人称写实后宫甜宠）、其他风格群（黑暗英雄调教、日常纯爱、综漫爽文、黑暗产业、鬼畜极H）。
- **Purpose**: 现有Skill缺少正太纯爱/色色文的专项文风指导。本模块专门解决：1) 如何写出《星辰之下》那样萌系轻小说感的纯爱文；2) 如何写出《年轻房东》那样第一人称写实后宫感的文；3) 如何根据题材选择合适的正太BL文风（从纯爱甜宠到黑暗调教全覆盖）；4) 提供大量正反例让AI能匹配风格，避免写出来千篇一律。
- **Target Users**: 使用Chinese-WebNovel-Skill进行正太BL/纯爱/色色文创作的作者。

## Goals
- 在modules下新建独立模块 `shota_pure_love/`，遵循标准模块目录结构
- 复制所有原始小说到 sources/raw/ 下三个子目录：xingchen、nianqing、others
- 创建 README.md - 说明模块用途、调用时机、阅读顺序、文件说明
- 创建 tutorial.md - 系统讲解正太纯爱文的写作框架、三大文风体系对比、每种文风的核心技法
- 创建 runtime.md - 明确调用规则、风格诊断流程、动笔前局部计划、写作执行步骤、写完自查清单
- 创建 good_examples.md - 按文风分类整理至少20个正例片段，标注"该学什么"
- 创建 bad_examples.md - 按错误类型整理至少15个反例片段，标注"错在哪里"
- 创建 source_index.md - 原始素材索引，说明每篇小说的定位、参考价值、主要/补充/噪音

## Non-Goals (Out of Scope)
- 不修改bl_r18_writing模块内的任何文件（本模块是独立平行的新模块）
- 不修改主SKILL.md（README.md已足够）
- 不清洗/修改原始小说文件，原样保留在sources/raw/下
- 不进行小说文本的全文校对或格式修正
- 不创建examples_*.md这类bl_r18_writing专属格式的文件（遵循标准模块结构）
- 不覆盖或修改现有任何模块

## Background & Context
- 标准模块结构参考：module_template.md，所有模块统一包含 README.md、tutorial.md、runtime.md、good_examples.md、bad_examples.md、source_index.md，可选sources/raw/存放原始素材
- 现有参考模块：opening/、dialogue/、milking_techniques/等都遵循此结构
- 素材来源：`/workspace/shota_pure_love/正太纯爱色色文/` 共18个文件，去重后17篇作品：
  - xingchen子目录（1篇）：星辰之下.txt（955KB，萌系奇幻纯爱，代表"星辰风"）
  - nianqing子目录（5篇）：年轻房东小房客全5季（约600KB，第一人称写实后宫甜宠，代表"房东风"）
  - others子目录（11篇，去重后10篇）：
    - 少年英雄系列4篇（moecloud）：黑暗英雄陷落调教系
    - 正义战队by落雪冰痕：战队英雄调教
    - 神奇少年【长篇完结】：超能力少年调教
    - 宝贝今年十四岁：伪兄弟日常纯爱
    - 运动裤下的秘密：校园日常纯爱
    - [综漫]正太控的世界旅行：综漫穿越爽文后宫
    - 正太会所：黑暗产业设定系
    - 正太滋味BY奴玉：鬼畜触手极H系

## Functional Requirements
- **FR-1**: 创建模块目录结构
  - `/workspace/Chinese-WebNovel-Skill-2/Chinese-WebNovel-Skill-2/references/modules/shota_pure_love/`
  - 下含：README.md、tutorial.md、runtime.md、good_examples.md、bad_examples.md、source_index.md
  - 下含：sources/raw/xingchen/、sources/raw/nianqing/、sources/raw/others/
  - 将所有txt原始文件按分类复制到对应子目录

- **FR-2**: 创建 README.md
  - 明确模块解决什么问题（正太BL文风选择、萌系/写实/黑暗等风格写法）
  - 明确什么时候调用（写正太BL、纯爱甜宠、萌系文、第一人称后宫文、黑暗调教文时）
  - 建议阅读顺序
  - 文件说明表

- **FR-3**: 创建 tutorial.md（核心教程）
  - 统一定义：什么是正太纯爱/色色文，它和其他BL题材的区别
  - 三大文风体系详解：
    - 星辰风（二次元萌系纯爱）：核心特征、词汇库、叙事节奏、心理描写、R18尺度、意象使用（星辰/狼羊隐喻）
    - 房东风（第一人称写实后宫）：核心特征、第一人称吐槽写法、生活化对话、多人物平衡、R18写实尺度
    - 其他风格群：分5个子类讲解（黑暗英雄调教、日常纯爱、综漫爽文、黑暗产业、鬼畜极H）
  - 底层原则：正太BL写作的通用原则（萌点密度、情感vs色情平衡、角色年龄与行为匹配）
  - 文风选择决策树：什么题材选什么文风

- **FR-4**: 创建 runtime.md（执行入口）
  - 什么时候必须调用本模块
  - 文风诊断流程：根据用户需求/题材判断该用哪种文风
  - 分层分类：先选大系（纯爱/后宫/黑暗）→再选具体文风
  - 正反例匹配规则
  - 动笔前局部计划模板（必须先写计划再动笔）
  - 不同任务类型的处理方式（写开篇、写H场景、写日常互动、改写现有段落）
  - 写完后自查清单

- **FR-5**: 创建 good_examples.md
  - 至少20个正例片段
  - 按文风分组：星辰风组、房东风组、其他风格组
  - 每条正例标注：来源作品、片段类型（开篇/日常/H场景/告白/吃醋等）、该学什么（结构/用词/节奏/心理描写等）
  - 开头提供快速索引表

- **FR-6**: 创建 bad_examples.md
  - 至少15个反例片段（可从原文中选取写得不好的段落，或构造典型错误）
  - 按错误类型分组：OOC错误、节奏错误、尺度错误、萌点缺失错误、对话不自然错误等
  - 每条反例标注：错在哪里、为什么错、该怎么改
  - 关键错误簇补充"这类通常该补什么"

- **FR-7**: 创建 source_index.md
  - 列出sources/raw/下所有文件
  - 标注每个文件的定位：主参考/补充参考/风格参考/噪音较大
  - 明确说明本模块主要依赖了哪些资料
  - 标注重复文件（如宝贝今年十四岁有两个版本）

## Non-Functional Requirements
- **NFR-1**: 所有.md文件遵循标准模块格式，markdown排版清晰
- **NFR-2**: good_examples和bad_examples中的片段必须来源于原始小说，不能凭空编造
- **NFR-3**: 文风总结必须准确，要让人看完就能区分出星辰风和房东风的差异
- **NFR-4**: runtime.md必须是可执行的流程，不是空泛理论，要给出明确的"先做什么再做什么"
- **NFR-5**: 保留原始小说文件在sources/raw/下，不做修改
- **NFR-6**: 文件大小：tutorial.md 30-50KB，good_examples.md 40-60KB，bad_examples.md 20-40KB，其他文件5-20KB

## Constraints
- **Technical**: 必须严格遵循module_template.md规定的文件结构和命名
- **Business**: 必须遵守现有core_principles.md（bl_r18_writing模块）的所有硬性禁令和内容红线
- **Dependencies**: 原始素材在/workspace/shota_pure_love/正太纯爱色色文/，标准模块模板参考modules/module_template.md

## Assumptions
- module_template.md的结构是所有模块必须遵守的标准
- 三大文风分类（星辰风、房东风、其他风格群）足以覆盖用户的正太BL写作需求
- 原始小说文件原样保留在sources/raw/下即可，不需要清洗格式
- 本模块是文风指导模块，与bl_r18_writing（榨精技法模块）是平行互补关系，不是替代关系

## Acceptance Criteria

### AC-1: 目录结构完整
- **Given**: 模块创建完成
- **When**: 查看shota_pure_love目录
- **Then**: 包含所有6个标准.md文件 + sources/raw/下3个子目录，所有原始小说已复制到对应子目录
- **Verification**: `programmatic`

### AC-2: README.md符合标准
- **Given**: README.md已创建
- **When**: 阅读README
- **Then**: 清晰说明模块用途、调用时机、阅读顺序、文件说明，对齐opening/README.md的格式
- **Verification**: `human-judgment`

### AC-3: tutorial.md文风总结准确
- **Given**: tutorial.md已创建
- **When**: 审查三大文风体系的讲解
- **Then**: 星辰风和房东风有明确区分，每个文风都有具体特征、用词示例、片段佐证；其他风格群分类清晰
- **Verification**: `human-judgment`

### AC-4: runtime.md可执行
- **Given**: runtime.md已创建
- **When**: 按照runtime流程执行
- **Then**: 可以根据用户需求完成"诊断文风→选正例反例→写局部计划→写作→自查"的完整流程，步骤明确可操作
- **Verification**: `human-judgment`

### AC-5: good_examples.md质量
- **Given**: good_examples.md已创建
- **When**: 检查正例
- **Then**: 至少20个正例，按文风分组，每条都标注"该学什么"，片段来源于原始小说
- **Verification**: `programmatic` + `human-judgment`

### AC-6: bad_examples.md质量
- **Given**: bad_examples.md已创建
- **When**: 检查反例
- **Then**: 至少15个反例，按错误类型分组，每条都标注"错在哪里"和改进方向
- **Verification**: `programmatic` + `human-judgment`

### AC-7: source_index.md索引完整
- **Given**: source_index.md已创建
- **When**: 检查索引
- **Then**: 所有原始文件都有记录，标注了主参考/补充参考/重复文件等信息
- **Verification**: `programmatic`

### AC-8: 与现有模块兼容
- **Given**: 模块创建完成
- **When**: 与现有模块（特别是bl_r18_writing）配合使用
- **Then**: 不冲突，可以平行调用，文风模块负责风格选择，技法模块负责具体R18技法
- **Verification**: `human-judgment`

## Open Questions
- [ ] 其他风格群中的5个子类（黑暗英雄/日常纯爱/综漫/会所/鬼畜）是否需要在tutorial中同等详细讲解，还是只做概要介绍、重点放在星辰和房东上？
- [ ] sources/raw/下的文件是否需要重命名为编号格式（如1.txt、2.txt），还是保留原文件名？
