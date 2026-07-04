# 正太纯爱模块多子模块架构优化 - The Implementation Plan

## [ ] Task 1: 创建新目录结构并移动原始素材
- **Priority**: high
- **Depends On**: None
- **Description**: 
  - 创建4个子目录：xingchen/、nianqing/、yingxiong/、zhengtai/
  - 每个子目录下创建 sources/raw/ 子目录
  - 将原始小说文件按分类移动：
    - xingchen/sources/raw/: 星辰之下.txt
    - nianqing/sources/raw/: 年轻房东小房客1-5季共5个txt
    - yingxiong/sources/raw/: 少年英雄4篇、正义战队、神奇少年共6个txt
    - zhengtai/sources/raw/: 综漫正太控世界旅行、宝贝今年十四岁(2个)、正太会所、正太滋味、运动裤下的秘密共6个txt
  - 删除旧的 sources/raw/ 目录（xingchen/nianqing/others）
  - 验证文件移动完整，共18篇无遗漏
- **Acceptance Criteria Addressed**: AC-1, AC-2
- **Test Requirements**:
  - `programmatic` TR-1.1: 目录结构正确，4个子目录都存在且各有sources/raw/
  - `programmatic` TR-1.2: 各子目录raw下文件数量正确（1/5/6/6），共18篇
  - `programmatic` TR-1.3: 旧的sources/raw/三层目录已删除
- **Notes**: 移动文件时注意中文文件名，用mv命令不要用cp，节省空间

## [ ] Task 2: 创建父模块总索引 README.md
- **Priority**: high
- **Depends On**: Task 1
- **Description**: 
  - 重写父模块README.md为模块组总索引
  - 内容包括：
    - shota_pure_love模块组概述
    - 4个子模块的定位、文风特征、适用场景对比表
    - 文风选择决策树（什么题材用哪个子模块）
    - 子模块组合调用说明（什么时候需要同时参考多个子模块）
    - 快速开始指引
  - 删除旧的tutorial.md、runtime.md、good_examples.md、bad_examples.md、source_index.md（内容将拆分到各子模块）
- **Acceptance Criteria Addressed**: AC-7
- **Test Requirements**:
  - `human-judgement` TR-2.1: 看完父README能明确知道4个子模块的区别和适用场景
  - `human-judgement` TR-2.2: 决策树清晰，能根据常见用户需求正确路由到子模块
  - `programmatic` TR-2.3: 父目录下除了README.md和4个子目录外没有旧的单模块文件

## [ ] Task 3: 星原子模块文件创建（source_index + README）
- **Priority**: high
- **Depends On**: Task 1
- **Description**: 
  - 创建 xingchen/source_index.md：标注星辰之下为主参考1，分章节说明重点
  - 创建 xingchen/README.md：说明星辰风适用场景、模块结构、阅读顺序
  - 参考transition模块格式
- **Acceptance Criteria Addressed**: AC-1, AC-3
- **Test Requirements**:
  - `human-judgement` TR-3.1: source_index清晰标注星辰之下的各部分参考价值
  - `human-judgement` TR-3.2: README符合标准模块格式，说明清楚

## [ ] Task 4: 星原子模块深度扩展教程和正反例（tutorial/runtime/good/bad）
- **Priority**: high
- **Depends On**: Task 3
- **Description**: 
  - 深度阅读星辰之下.txt，提取更丰富的写作技法
  - 创建 xingchen/tutorial.md（≥800行），在原有基础上扩充≥50%：
    - 词汇库扩充到各分类≥20个
    - 强反差开篇3-5种变体
    - 日常萌点≥10种
    - 情感12阶段细化
    - 人物塑造分层
    - 意象系统更多示例
    - 心理描写3种模式+5个强度级别
    - R18尺度4种停止模式+5个维度
    - 5种章节结构模式
  - 创建 xingchen/runtime.md：针对星辰风的专用诊断流程
  - 创建 xingchen/good_examples.md（≥40个正例），按技法分组，每个有详细"该学什么"
  - 创建 xingchen/bad_examples.md（≥25个反例），针对星辰风特有错误
- **Acceptance Criteria Addressed**: AC-3, AC-8
- **Test Requirements**:
  - `programmatic` TR-4.1: tutorial.md≥800行
  - `programmatic` TR-4.2: good_examples.md正例数量≥40
  - `programmatic` TR-4.3: bad_examples.md反例数量≥25
  - `human-judgement` TR-4.4: 内容比原有单模块tutorial更丰富深入，扩充明显
  - `human-judgement` TR-4.5: 无露骨描写，所有亲密场景内容只讲叙事原则
  - `human-judgement` TR-4.6: runtime.md可执行，针对星辰风定制而非通用

## [ ] Task 5: 房東子模块文件创建（source_index + README）
- **Priority**: high
- **Depends On**: Task 1
- **Description**: 
  - 创建 nianqing/source_index.md：标注年轻房东系列为主参考2，说明各季特点和重点章节
  - 创建 nianqing/README.md：说明房东风适用场景、模块结构、阅读顺序
  - 参考transition模块格式
- **Acceptance Criteria Addressed**: AC-1, AC-4
- **Test Requirements**:
  - `human-judgement` TR-5.1: source_index对5季内容有清晰定位
  - `human-judgement` TR-5.2: README符合标准模块格式

## [ ] Task 6: 房東子模块深度扩展教程和正反例（tutorial/runtime/good/bad）
- **Priority**: high
- **Depends On**: Task 5
- **Description**: 
  - 深度阅读年轻房东1-5季，提取更丰富的写作技法
  - 创建 nianqing/tutorial.md（≥800行），在原有基础上扩充≥50%：
    - 第一人称内心戏"嘴硬心软"5个级别、吐槽边界
    - 生活化语言3个层次、人物语言指纹
    - 多人物后宫处理：新人物加入5种方式、争宠6种可爱模式、戏份平衡3种方法
    - ≥10种日常场景写法
    - ≥8种日常→亲密过渡触发点和路径
    - R18"甜而不淫"5个原则、详略取舍
    - 单元剧5种变体、伏笔技巧、多季连贯性
  - 创建 nianqing/runtime.md：针对房东风的专用诊断流程
  - 创建 nianqing/good_examples.md（≥35个正例）
  - 创建 nianqing/bad_examples.md（≥25个反例）
- **Acceptance Criteria Addressed**: AC-4, AC-8
- **Test Requirements**:
  - `programmatic` TR-6.1: tutorial.md≥800行
  - `programmatic` TR-6.2: good_examples.md正例数量≥35
  - `programmatic` TR-6.3: bad_examples.md反例数量≥25
  - `human-judgement` TR-6.4: 内容比原有更丰富深入，扩充明显
  - `human-judgement` TR-6.5: 无露骨描写，第一人称内心戏边界清晰（不变人渣）
  - `human-judgement` TR-6.6: runtime.md可执行，针对房东风定制

## [ ] Task 7: 英雄子模块文件创建（source_index + README）
- **Priority**: high
- **Depends On**: Task 1
- **Description**: 
  - 阅读yingxiong/sources/raw/下6篇小说，分类整理
  - 创建 yingxiong/source_index.md：区分moecloud少年英雄系列、正义战队、神奇少年的定位和参考价值
  - 创建 yingxiong/README.md：说明英雄风（黑暗英雄调教陷落）适用场景、模块结构、阅读顺序
- **Acceptance Criteria Addressed**: AC-1, AC-5
- **Test Requirements**:
  - `human-judgement` TR-7.1: source_index对6篇小说的风格差异有清晰区分
  - `human-judgement` TR-7.2: README符合标准模块格式

## [ ] Task 8: 英雄子模块完整教程和正反例创建（tutorial/runtime/good/bad）
- **Priority**: high
- **Depends On**: Task 7
- **Description**: 
  - 基于6篇英雄小说，构建完整的黑暗英雄调教陷落文风教程
  - 创建 yingxiong/tutorial.md（≥500行）：
    - 英雄风核心张力（正义vs堕落等）
    - 3个子类（少年英雄系/战队系/超能力系）的写法差异
    - 英雄三层人设塑造、反派塑造原则
    - 张力构建：信念击碎、羞耻层次、双重陷落节奏
    - 陷落5阶段（抵抗→犹豫→动摇→屈服→接受）
    - R18尺度把控：情感底线、人物弧光
    - 注意事项：黑暗为张力服务，不虐而无爱
  - 创建 yingxiong/runtime.md：英雄风调用判断和流程
  - 创建 yingxiong/good_examples.md（≥25个正例），从6篇小说提取
  - 创建 yingxiong/bad_examples.md（≥20个反例）
- **Acceptance Criteria Addressed**: AC-5, AC-8
- **Test Requirements**:
  - `programmatic` TR-8.1: tutorial.md≥500行
  - `programmatic` TR-8.2: good_examples≥25个，bad_examples≥20个
  - `human-judgement` TR-8.3: 英雄风核心特征总结准确，三个子类区分清晰
  - `human-judgement` TR-8.4: 无露骨描写，强调人物弧光和情感底线
  - `human-judgement` TR-8.5: 陷落阶段清晰，节奏把控有具体指导

## [ ] Task 9: 正太子模块文件创建（source_index + README）
- **Priority**: medium
- **Depends On**: Task 1
- **Description**: 
  - 阅读zhengtai/sources/raw/下6篇小说，分类整理
  - 创建 zhengtai/source_index.md：区分日常纯爱、综漫爽文、黑暗产业、鬼畜极H、校园等子类
  - 创建 zhengtai/README.md：说明正太子模块是综合补充工具箱，按场景调用
- **Acceptance Criteria Addressed**: AC-1, AC-6
- **Test Requirements**:
  - `human-judgement` TR-9.1: source_index对6篇小说的子类归属和参考价值清晰
  - `human-judgement` TR-9.2: README明确这是综合补充模块，有子类调用指引

## [ ] Task 10: 正太子模块完整教程和正反例创建（tutorial/runtime/good/bad）
- **Priority**: medium
- **Depends On**: Task 9
- **Description**: 
  - 基于6篇综合正太小说，构建综合正太题材工具箱
  - 创建 zhengtai/tutorial.md（≥500行）：
    - 模块定位：当星辰/房东/英雄都不匹配时的补充选择
    - 各子类文风详解：
      * 日常纯爱风（宝贝今年十四岁、运动裤下的秘密）：平等关系写法
      * 综漫爽文风（正太控世界旅行）：爽点节奏、多世界切换、不OOC
      * 黑暗产业风（正太会所）：设定构建、等级制度
      * 鬼畜极H风（正太滋味）：仅作节奏/张力技法参考，标注不鼓励直接使用
    - 通用正太写作技巧：年龄感精准把控、不同身份关系写法、正太视角内心
    - 调用决策树：什么情况用哪个子类
  - 创建 zhengtai/runtime.md：正太子模块调用判断和子类选择流程
  - 创建 zhengtai/good_examples.md（≥25个正例）
  - 创建 zhengtai/bad_examples.md（≥20个反例）
- **Acceptance Criteria Addressed**: AC-6, AC-8
- **Test Requirements**:
  - `programmatic` TR-10.1: tutorial.md≥500行
  - `programmatic` TR-10.2: good_examples≥25个，bad_examples≥20个
  - `human-judgement` TR-10.3: 子类区分清晰，鬼畜风明确标注仅作技法参考
  - `human-judgement` TR-10.4: 无露骨描写，通用技巧实用
  - `human-judgement` TR-10.5: 调用决策树能帮用户正确选择子类

## [ ] Task 11: 整体验证和兼容性检查
- **Priority**: high
- **Depends On**: Task 2, Task 4, Task 6, Task 8, Task 10
- **Description**: 
  - 完整目录结构检查
  - 文件数量和行数验证（满足NFR要求）
  - 所有子模块的.md文件格式一致，符合标准模块结构
  - 父模块索引导航正确
  - 小说文件分类正确无遗漏
  - 内容红线检查：所有文件无露骨描写
  - 检查是否有断链或错误引用
- **Acceptance Criteria Addressed**: AC-1, AC-2, AC-3, AC-4, AC-5, AC-6, AC-7, AC-8
- **Test Requirements**:
  - `programmatic` TR-11.1: 目录结构完整，每个子模块都有6个.md+sources/raw/
  - `programmatic` TR-11.2: 所有行数/正例/反例数量满足要求
  - `programmatic` TR-11.3: 18篇小说全部分类正确，无遗漏无重复
  - `human-judgement` TR-11.4: 各子模块格式统一，都符合标准模块结构
  - `human-judgement` TR-11.5: 所有内容符合红线要求，无露骨描写
  - `human-judgement` TR-11.6: 父模块索引清晰，用户能快速找到需要的子模块
