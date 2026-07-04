# 正太纯爱文风整合 - The Implementation Plan (Decomposed and Prioritized Task List)

## [ ] Task 1: 深度阅读并提取《星辰之下》文风精华
- **Priority**: high
- **Depends On**: None
- **Description**: 
  - 完整阅读 `/workspace/shota_pure_love/正太纯爱色色文/星辰之下.txt`
  - 提取核心文风要素：萌系词汇库、叠词/拟声词用法、心理描写模式、情感递进节奏、R18前戏描写手法、日常互动萌点、反差萌塑造方式
  - 记录关键片段示例（每类至少3个）：开篇方式、告白场景、初吻/初夜描写、吃醋场景、日常互动
  - 输出结构化的星辰风文风提取笔记
- **Acceptance Criteria Addressed**: [AC-2]
- **Test Requirements**:
  - `programmatic` TR-1.1: 笔记覆盖至少8个文风维度（词汇、对话、心理、节奏、描写、R18、萌点、意象）
  - `human-judgement` TR-1.2: 每个维度都有原文片段作为示例，片段选择具有代表性
- **Notes**: 重点关注"星辰"意象的反复使用、"狼与羊"的隐喻、基诺的傲娇心理、辰辰的萌系语言

## [ ] Task 2: 深度阅读并提取《年轻房东》文风精华
- **Priority**: high
- **Depends On**: None
- **Description**: 
  - 完整阅读《年轻房东小房客》全5季
  - 提取核心文风要素：第一人称叙事特点、生活化对话模式、多人物关系处理、R18写实描写尺度、后宫关系平衡、日常→H的自然过渡、角色个性化语言
  - 记录关键片段示例：第一人称内心吐槽、房东房客初遇、照顾生病场景、多人物互动、H场景的情感铺垫
  - 输出结构化的房东风文风提取笔记
- **Acceptance Criteria Addressed**: [AC-2]
- **Test Requirements**:
  - `programmatic` TR-2.1: 笔记覆盖第一人称、对话、人物塑造、R18、后宫关系、日常描写6个维度
  - `human-judgement` TR-2.2: 准确捕捉到"房东风"的写实感和第一人称吐槽特点，片段示例能体现其风格
- **Notes**: 注意商仁（房东）的第一人称心理活动与实际行为的反差、小雨的傲娇、小杰的痞气、小迪的成长变化

## [ ] Task 3: 创建 genre_shota_pure_love.md 主体框架（前4章）
- **Priority**: high
- **Depends On**: [Task 1, Task 2]
- **Description**: 
  - 参照 genre_shota_school.md 的7段式结构，创建 genre_shota_pure_love.md
  - 完成第1-4章：
    - 第一章：题材定位与核心爽点（纯爱vs堕落的本质区别、两种子风格定位、核心爽点对比）
    - 第二章：6大叙事范式（星辰风3种+房东风3种，每种含核心设定、关系模式、剧情推进路线、经典桥段）
    - 第三章：双风格世界观与角色原型库（星辰风世界观2种+角色8个，房东风世界观2种+角色8个）
    - 第四章：专属R18技法（纯爱向技法，区别于榨精技法，强调温柔、情感交融）
  - 文件大小控制在30-40KB
- **Acceptance Criteria Addressed**: [AC-1, AC-2, AC-3]
- **Test Requirements**:
  - `programmatic` TR-3.1: 章节结构完整对齐genre_shota_school.md，前4章无缺失
  - `human-judgement` TR-3.2: 叙事范式可直接用于创作，角色原型有区分度、有萌点、有攻略路线
  - `human-judgement` TR-3.3: R18技法符合纯爱定位，与现有writing_guide.md中的榨精技法有明显区别
- **Notes**: 角色原型要标注"星辰风"或"房东风"，避免混淆

## [ ] Task 4: 完成 genre_shota_pure_love.md 后3章并补全
- **Priority**: high
- **Depends On**: [Task 3]
- **Description**: 
  - 完成第5-7章：
    - 第五章：经典场景模板（星辰风3个+房东风3个，每个含场景要素、标准流程、关键细节、对话示例）
    - 第六章：写作技巧与雷点（情感递进节奏、萌点密度、R18尺度把控、常见错误避雷）
    - 第七章：参考作品索引
  - 补充前4章中缺少的示例片段
  - 调整整体内容，确保两种子风格（星辰/房东）占比均衡
  - 最终文件大小控制在60-80KB
- **Acceptance Criteria Addressed**: [AC-1, AC-3]
- **Test Requirements**:
  - `programmatic` TR-4.1: 7个章节完整，文件大小60-80KB
  - `human-judgement` TR-4.2: 场景模板包含完整流程和细节，可直接套用写作
  - `human-judgement` TR-4.3: 雷点章节明确指出纯爱写作的常见错误，如情感铺垫不足、OOC、尺度失控
- **Notes**: 写完后通读一遍，确保两种风格不串味

## [ ] Task 5: 更新 style_codes.md 添加双子文风配置
- **Priority**: high
- **Depends On**: [Task 1, Task 2]
- **Description**: 
  - 在现有"5种文风切换"表格后，新增"六、正太纯爱双子文风"小节
  - 添加「星辰风-二次元萌系纯爱」：
    - 核心特征表格（语言特点、对话占比、描写重点、适用场景、R18尺度）
    - 详细执行细则（用词偏好：叠词/拟声词/萌系词汇库；心理描写方式；节奏控制；意象使用）
    - 与现有"萌系轻小说"文风的区别和联系
  - 添加「房东风-写实甜宠后宫」：
    - 核心特征表格（第一人称特点、对话占比、描写重点、适用场景、R18尺度）
    - 详细执行细则（第一人称内心吐槽写法；生活化对话；多人物关系平衡；写实H写法）
    - 与其他文风的区别
  - 在"五、风格组合速查表"中添加纯爱题材的推荐组合行
- **Acceptance Criteria Addressed**: [AC-4, AC-6]
- **Test Requirements**:
  - `programmatic` TR-5.1: style_codes.md原有内容完整保留，新内容插入位置正确
  - `human-judgement` TR-5.2: 两种新风的执行细则具体可操作，包含用词示例和写法指导
  - `human-judgement` TR-5.3: 风格组合速查表新增条目准确，能指导实际创作
- **Notes**: 新风不要替换现有文风，而是作为补充的专项文风

## [ ] Task 6: 更新 README.md 添加索引和调用说明
- **Priority**: medium
- **Depends On**: [Task 3, Task 4, Task 5]
- **Description**: 
  - 在"文件说明"表格中添加 genre_shota_pure_love.md 条目
  - 在"调用时机"或"强制执行规则"部分补充纯爱题材的调用流程：先选双子文风→再调用genre_shota_pure_love
  - 在"建议阅读顺序"中提及纯爱题材的阅读路径
  - 如需要，在"核心设计哲学"中补充纯爱题材的核心原则（情感优先等）
- **Acceptance Criteria Addressed**: [AC-5]
- **Test Requirements**:
  - `programmatic` TR-6.1: 新文件在README中有索引，链接路径正确
  - `human-judgement` TR-6.2: 调用流程清晰，用户能看懂如何使用新模块
- **Notes**: 改动要小，不要重写README其他部分

## [ ] Task 7: 整体验证与兼容性测试
- **Priority**: high
- **Depends On**: [Task 4, Task 5, Task 6]
- **Description**: 
  - 验证所有文件改动：
    - genre_shota_pure_love.md结构完整、大小达标、两种风格均衡
    - style_codes.md新风配置清晰、与现有文风不冲突
    - README.md索引完整
  - 进行兼容性检查：确认新genre文件可以和现有技法、节奏、NSFW风格组合使用
  - 进行试写验证：分别用星辰风和房东风各写一个200字左右的开篇片段，验证风格配置有效
- **Acceptance Criteria Addressed**: [AC-1, AC-2, AC-4, AC-5, AC-6]
- **Test Requirements**:
  - `programmatic` TR-7.1: 所有文件存在，genre文件大小在60-80KB
  - `human-judgement` TR-7.2: 试写片段风格鲜明，星辰风和房东风差异明显，符合原作特征
  - `human-judgement` TR-7.3: 不与现有模块冲突，可正常组合使用
- **Notes**: 试写片段不需要很长，能体现风格差异即可
