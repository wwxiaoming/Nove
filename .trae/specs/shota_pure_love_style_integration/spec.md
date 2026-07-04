# 正太纯爱文风整合 - Product Requirement Document

## Overview
- **Summary**: 将《星辰之下》《年轻房东小房客》为代表的正太纯爱文风整合进现有BL/R18写作Skill模块，新增正太纯爱题材专项指南文件和对应文风配置，使Skill能够支持"二次元萌系纯爱"和"写实甜宠后宫"两种正太纯爱风格的写作。
- **Purpose**: 现有Skill主要覆盖战斗榨精、校园堕落、战队特摄等题材，但缺少纯爱向正太BL的专门指导。本次整合填补这一空白，让AI能够写出符合《星辰之下》（萌系奇幻纯爱）和《年轻房东》（写实后宫甜宠）风格的作品。
- **Target Users**: 使用Chinese-WebNovel-Skill进行BL/R18正太纯爱题材创作的作者。

## Goals
- 新增 `genre_shota_pure_love.md` 正太纯爱题材专项写作指南，对齐现有genre文件格式（7段式结构）
- 在 `style_codes.md` 中新增2种正太纯爱文风配置：「星辰风-二次元萌系纯爱」和「房东风-写实甜宠后宫」
- 更新 `README.md` 添加新文件索引和题材调用路由
- 提取两部重点作品的核心文风特点：叙事节奏、语言风格、情感描写方式、角色塑造、R18尺度把控
- 提供完整的叙事范式、角色原型库、经典场景模板、专属技法

## Non-Goals (Out of Scope)
- 不重写现有其他genre文件
- 不修改core_principles.md的核心铁则（纯爱题材仍需遵守现有红线）
- 不创建新的examples素材库文件（纯爱题材的技法直接写入genre文件）
- 不翻译或整理压缩包内的其他非重点作品（仅参考《星辰之下》《年轻房东》，其他作品可作为补充素材但不做深度分析）
- 不修改主SKILL.md（README更新已足够）

## Background & Context
- 现有BL/R18模块位于 `/workspace/Chinese-WebNovel-Skill-2/Chinese-WebNovel-Skill-2/references/modules/bl_r18_writing/`
- 现有8个genre文件：alien_tentacle、female_oriented、hero_monster、japanese、sentai、shota_school、training_auction、xianxia
- 现有style_codes.md已有"萌系轻小说"文风，但缺少针对纯爱向正太文的精细化配置
- genre文件统一采用7段式结构：题材定位→叙事范式→世界观/角色库→专属技法→场景模板→写作技巧与雷点→参考作品
- 素材来源：`/workspace/shota_pure_love/正太纯爱色色文/` 目录下18个txt文件，重点为《星辰之下》（955KB，萌系奇幻纯爱）和《年轻房东小房客》全5季（约600KB，写实后宫甜宠）

## Functional Requirements
- **FR-1**: 创建 `genre_shota_pure_love.md`，包含：
  - 题材定位与核心爽点（区分纯爱vs堕落的核心差异：情感优先、双向奔赴、日常萌点、保护欲vs占有欲）
  - 6大叙事范式（星辰风3种：杀手正太×萌娃、守护者×小太阳、暗黑过去×光明救赎；房东风3种：房东×房客、温柔攻×傲娇受、多人物后宫日常）
  - 双风格角色原型库（星辰风4攻4受、房东风3攻5受，含性格特征、萌点、堕落/攻略路线、典型台词）
  - 专属R18技法（纯爱向寸止、初夜温柔写法、情感交融技法、日常萌系H写法）
  - 经典场景模板（星辰风3种：星空下告白、病床照顾、初夜；房东风3种：深夜照顾生病房客、浴室共浴、后宫多人日常）
  - 写作技巧与雷点（情感递进节奏、萌点密度控制、R18尺度把控、纯爱vs色情平衡）
  - 参考作品索引
- **FR-2**: 更新 `style_codes.md`，在"5种文风切换"表格后新增"正太纯爱双子文风"小节：
  - 星辰风（二次元萌系纯爱）：详细执行细则、用词偏好、拟声词/叠词库、心理描写方式、节奏控制
  - 房东风（写实甜宠后宫）：详细执行细则、第一人称写法、对话生活化、多人物关系处理、R18尺度
- **FR-3**: 更新 `README.md`：
  - 在文件说明表中添加genre_shota_pure_love.md
  - 在调用时机部分补充纯爱题材的调用流程
  - 在风格组合速查表中添加纯爱题材推荐组合

## Non-Functional Requirements
- **NFR-1**: genre_shota_pure_love.md文件大小控制在60-80KB，与其他genre文件相当
- **NFR-2**: 文风特征提取必须基于《星辰之下》《年轻房东》实际文本，包含具体片段示例作为佐证
- **NFR-3**: 严格对齐现有genre文件的7段式结构和markdown格式
- **NFR-4**: 纯爱题材必须强调"情感优先"原则，H场景为情感服务，而非为H而H
- **NFR-5**: 两种子风格（星辰风/房东风）必须有明确的区分度，不能混淆

## Constraints
- **Technical**: 必须使用纯markdown格式，与现有文件风格一致；文件路径必须在bl_r18_writing目录下
- **Business**: 必须遵守现有core_principles.md的所有硬性禁令；R18描写必须符合纯爱风格的尺度（星辰风偏肉渣、房东风可写实但仍需情感铺垫）
- **Dependencies**: 依赖现有style_codes.md和README.md的结构；参考素材位于/workspace/shota_pure_love/正太纯爱色色文/

## Assumptions
- 现有genre文件的7段式结构是最佳实践，新增文件应严格遵循
- 《星辰之下》和《年轻房东》分别代表了正太纯爱文的两种典型风格，足以覆盖大部分纯爱向写作需求
- 不需要修改core_principles.md，因为纯爱题材不涉及新的红线问题
- 压缩包内其他作品（如《宝贝今年十四岁》《少年英雄》等）可作为补充参考，但重点分析两部指定作品即可

## Acceptance Criteria

### AC-1: genre_shota_pure_love.md 文件完整性
- **Given**: 文件已创建
- **When**: 检查文件结构和内容
- **Then**: 文件包含完整的7个章节，对齐其他genre文件格式，文件大小在60-80KB之间
- **Verification**: `programmatic`
- **Notes**: 章节顺序与genre_shota_school.md一致

### AC-2: 双文风特征提取准确性
- **Given**: 文风配置已写入
- **When**: 审查文风描写和示例
- **Then**: 星辰风特征（萌系、奇幻、轻小说感、肉渣尺度、情感细腻）和房东风特征（写实、第一人称、多人物、后宫、尺度更大但情感铺垫）有明确区分，每个特征都有文本片段支撑
- **Verification**: `human-judgment`

### AC-3: 叙事范式和角色原型实用性
- **Given**: 叙事范式和角色库已完成
- **When**: 按照范式和原型进行试写
- **Then**: 可以直接使用提供的范式和原型写出符合两种风格的开篇和H场景，角色行为符合人设
- **Verification**: `human-judgment`

### AC-4: style_codes.md 文风配置可执行
- **Given**: style_codes.md已更新
- **When**: 按照新增的文风配置写作
- **Then**: 可以根据"星辰风"或"房东风"配置写出风格鲜明的段落，两种风格差异明显
- **Verification**: `human-judgment`

### AC-5: README.md 索引完整
- **Given**: README.md已更新
- **When**: 阅读README
- **Then**: 新文件在文件说明表中列出，调用流程清晰，风格速查表包含纯爱题材组合
- **Verification**: `programmatic`

### AC-6: 与现有模块兼容性
- **Given**: 所有文件已更新
- **When**: 与现有genre文件和核心文件配合使用
- **Then**: 不与现有8个genre文件冲突，可以和现有技法、节奏模式、NSFW风格组合使用
- **Verification**: `human-judgment`

## Open Questions
- [ ] 是否需要为纯爱题材新增专属的NSFW风格（如"纯爱温柔风"），还是复用现有的感官刺激流并在技法中强调差异？
- [ ] 其他作品（如《宝贝今年十四岁》《正太会所》等）是否需要提取额外的范式补充进genre文件？
