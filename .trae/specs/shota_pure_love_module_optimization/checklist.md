# 正太纯爱模块多子模块架构优化 - 验证检查清单

## 目录结构检查
- [ ] 父模块 shota_pure_love/ 目录存在
- [ ] 父模块下有 4 个子目录：xingchen/、nianqing/、yingxiong/、zhengtai/
- [ ] 每个子目录下都有 sources/raw/ 子目录
- [ ] 旧的单模块文件（旧的tutorial.md、runtime.md、good_examples.md、bad_examples.md、source_index.md）已删除
- [ ] 旧的 sources/raw/ 三层目录结构（xingchen/nianqing/others）已删除
- [ ] 父模块只保留 README.md 作为总索引，没有其他冗余文件

## 文件分类检查（原始小说）
- [ ] xingchen/sources/raw/ 下有且仅有 1 个文件：星辰之下.txt
- [ ] nianqing/sources/raw/ 下有 5 个文件：年轻房东小房客第一季到第五季
- [ ] yingxiong/sources/raw/ 下有 6 个文件：少年英雄by moecloud、少年英雄·零、少年英雄·黑色闪电、少年英雄与地下医院、正义战队by落雪冰痕、神奇少年【长篇完结】
- [ ] zhengtai/sources/raw/ 下有 6 个文件：[综漫]正太控的世界旅行(1)、《宝贝今年十四岁》...、宝贝今年14岁、正太会所、正太滋味 BY奴玉、运动裤下的秘密
- [ ] 原始小说总数 1+5+6+6=18 篇，无遗漏无重复（宝贝今年十四岁两个版本都保留）

## 父模块 README.md 检查
- [ ] 说明 shota_pure_love 是包含 4 个独立子模块的模块组
- [ ] 4 个子模块各自的定位、文风特征、适用场景都有清晰说明
- [ ] 有 4 个子模块的对比表格（文风、视角、核心特点、适用题材）
- [ ] 有文风选择决策树或选择流程
- [ ] 有子模块组合调用说明（什么时候需要组合参考）
- [ ] 有快速开始/快速调用指引
- [ ] 阅读完父 README 就能明确知道该用哪个子模块

## 星原子模块（xingchen）检查
- [ ] xingchen/README.md 存在，符合标准模块格式
- [ ] xingchen/source_index.md 存在，标注这是主参考1，有章节重点说明
- [ ] xingchen/tutorial.md 行数 ≥ 800 行
- [ ] tutorial.md 包含：核心定义、词汇库（各分类≥20个）、强反差开篇3-5种变体、日常萌点≥10种、情感12阶段细化、人物塑造分层、意象系统示例、心理描写模式和强度级别、R18尺度4种停止模式、5种章节结构
- [ ] xingchen/runtime.md 存在，是针对星辰风的专用诊断流程（不是通用版）
- [ ] xingchen/good_examples.md 正例数量 ≥ 40 个
- [ ] good_examples 按技法分组，每个例子都有"该学什么"的详细拆解
- [ ] xingchen/bad_examples.md 反例数量 ≥ 25 个
- [ ] bad_examples 包含星辰风特有错误（叠词滥用、反差只在设定里、意象断裂等）
- [ ] 内容比原有单模块的星辰风部分扩充≥50%，明显更丰富深入

## 房東子模块（nianqing）检查
- [ ] nianqing/README.md 存在，符合标准模块格式
- [ ] nianqing/source_index.md 存在，标注这是主参考2，有各季特点和重点章节说明
- [ ] nianqing/tutorial.md 行数 ≥ 800 行
- [ ] tutorial.md 包含：核心定义、第一人称内心戏5个度的级别和吐槽边界、生活化语言3层次和人物语言指纹、多人物后宫处理（新人物加入5方式/争宠6模式/戏份平衡3方法）、≥10种日常场景写法、≥8种日常→亲密过渡路径、R18"甜而不淫"5原则、单元剧5变体和伏笔技巧
- [ ] nianqing/runtime.md 存在，是针对房东风的专用诊断流程
- [ ] nianqing/good_examples.md 正例数量 ≥ 35 个
- [ ] nianqing/bad_examples.md 反例数量 ≥ 25 个
- [ ] bad_examples 包含房东风特有错误（内心戏猥琐、多人物工具人、过渡突兀、对话不生活化等）
- [ ] 内容比原有单模块的房东风部分扩充≥50%，明显更丰富深入
- [ ] 第一人称内心戏边界清晰，明确区分"嘴硬心软"和"人渣猥琐"

## 英雄子模块（yingxiong）检查
- [ ] yingxiong/README.md 存在，符合标准模块格式
- [ ] yingxiong/source_index.md 存在，区分了少年英雄系列/正义战队/神奇少年三类的参考价值
- [ ] yingxiong/tutorial.md 行数 ≥ 500 行
- [ ] tutorial.md 包含：英雄风核心张力（正义vs堕落等）、3个子类（少年英雄系/战队系/超能力系）写法差异、英雄三层人设塑造、反派塑造原则、张力构建方法、陷落5阶段（抵抗→犹豫→动摇→屈服→接受）、R18尺度把控和情感底线、注意事项（不虐而无爱）
- [ ] yingxiong/runtime.md 存在，包含英雄风调用时机判断
- [ ] yingxiong/good_examples.md 正例数量 ≥ 25 个，来自6篇小说
- [ ] yingxiong/bad_examples.md 反例数量 ≥ 20 个
- [ ] bad_examples 包含英雄风特有错误（虐而无爱、人物脸谱化、陷落太突兀、为黑暗而黑暗等）
- [ ] 强调黑暗是张力来源，结局要有救赎或人物弧光

## 正太子模块（zhengtai）检查
- [ ] zhengtai/README.md 存在，明确这是综合补充工具箱
- [ ] zhengtai/source_index.md 存在，区分了日常纯爱/综漫爽文/黑暗产业/鬼畜极H/校园等子类
- [ ] zhengtai/tutorial.md 行数 ≥ 500 行
- [ ] tutorial.md 包含：模块定位（补充选择）、4个子类文风详解（日常纯爱/综漫爽文/黑暗产业/鬼畜极H）、通用正太写作技巧（年龄感/身份关系/正太视角）、调用决策树
- [ ] 鬼畜极H风明确标注"仅作节奏/张力技法参考，不鼓励直接使用"
- [ ] zhengtai/runtime.md 存在，包含子类选择流程
- [ ] zhengtai/good_examples.md 正例数量 ≥ 25 个
- [ ] zhengtai/bad_examples.md 反例数量 ≥ 20 个
- [ ] bad_examples 包含正太题材通用错误（年龄感混乱、题材杂糅、OOC等）

## 内容红线和质量检查
- [ ] 所有子模块的 .md 文件中无露骨描写
- [ ] 所有涉及亲密场景的内容只讲叙事原则、结构、情感层面，不涉及具体动作描写
- [ ] 心理描写尺度得当，无低俗/猥琐内容
- [ ] 所有子模块的文件格式一致，都遵循 transition 模块的标准格式
- [ ] 正例的"该学什么"部分具体可迁移，不是泛泛而谈
- [ ] 反例的"错在哪里"部分分析到位，有改进方向
- [ ] 各子模块 runtime.md 是可执行的流程，不是空泛理论
- [ ] 文风总结准确，星辰风和房东风的区分清晰，英雄风和正台风定位明确

## 兼容性和完整性检查
- [ ] 没有修改其他现有模块（bl_r18_writing、transition等）
- [ ] 没有修改主 SKILL.md
- [ ] 原始小说文件都是原样保留，没有修改内容
- [ ] 所有子模块之间没有内容重复冗余
- [ ] 父模块索引和子模块内容对应正确
- [ ] shota_pure_love 模块组作为整体，能和 bl_r18_writing 模块平行调用，不冲突
