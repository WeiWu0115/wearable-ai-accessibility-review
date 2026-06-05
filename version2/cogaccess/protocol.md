# Scoping Review Protocol — 认知无障碍设计原则 (Cognitive Accessibility Design Principles)

> 重点人群：自闭症 (Autism / ASD) · 同时覆盖其他认知障碍人群
> 数据库：ACM Digital Library + IEEE Xplore
> 时间窗：2015–2025 · 报告语言：中英混合
> 方法学框架：PRISMA-ScR (Tricco et al., 2018) + Arksey & O'Malley (2005) 五步法

---

## 1. 研究背景与目的 (Rationale)

认知无障碍 (cognitive accessibility) 关注信息、界面与交互对**认知、语言、学习与神经系统差异**人群的可达性。与视觉/听觉/运动无障碍相比，认知无障碍在 WCAG 等主流标准中长期被覆盖不足——WCAG 合规 ≠ 认知可用 (cognitive usability)。W3C 因此成立 **COGA (Cognitive and Learning Disabilities Accessibility Task Force)**，并发布《Making Content Usable for People with Cognitive and Learning Disabilities》。

本综述聚焦**设计原则 (design principles / guidelines / heuristics / patterns)** 这一层面：HCI 与无障碍研究社区为认知障碍人群提炼出了哪些可操作的设计规则？

### 研究问题 (Research Questions)

- **RQ1**（重点）：面向**自闭症 (ASD)** 人群的数字界面/交互，文献提出了哪些认知无障碍设计原则？覆盖哪些主题？
- **RQ2**：面向**其他认知障碍人群**（智力/学习障碍、痴呆/老年认知衰退、ADHD/阅读障碍、获得性脑损伤/失语）分别有哪些设计原则？
- **RQ3**（综合）：跨人群存在哪些**共性原则**？哪些是**人群特异性**原则？自闭症与其他人群的异同在哪里？
- **RQ4**：现有原则的**方法学来源**（专家共识 / 参与式设计 / 实证评估）与**证据空白**是什么？

---

## 2. 纳入与排除标准 (Eligibility — PCC 框架)

| 维度 | 纳入 | 排除 |
|---|---|---|
| **Population** | 自闭症 (ASD/autism)；智力障碍/IDD；学习障碍/dyslexia/dyscalculia；ADHD；痴呆/MCI/老年认知衰退；获得性脑损伤(TBI)/卒中/失语(aphasia)；广义"认知障碍/neurodivergent" | 纯感官（盲/聋）、纯运动障碍且不涉及认知；精神疾病（抑郁/焦虑）非认知可达性导向 |
| **Concept** | 设计原则 / 指南 / 启发式 / 设计模式 / 推荐 (design principles, guidelines, heuristics, patterns, recommendations) 面向数字界面、网页、移动应用、交互系统 | 纯医疗/药物干预；纯硬件工程；不产出可迁移设计规则的个案系统报告 |
| **Context** | 数字界面、Web、移动/平板、AAC、可穿戴、教育/工作/日常生活技术 | 物理空间/建筑无障碍（除非含数字界面） |
| **来源/类型** | ACM DL + IEEE Xplore 收录的会议论文、期刊、综述（含 Springer/W4A/CHI/ASSETS/INTERACT 等经 ACM 索引者） | 非英文且无英文版；纯海报摘要；无同行评议 |
| **时间** | 2015-01 至 2025-12 为主；**奠基性文献 (2005–2014)** 仅作背景引用，不计入主语料 | — |

---

## 3. 检索策略 (Search Strategy)

### 检索维度（概念 × 人群）

**概念词**：`cognitive accessibility` OR `accessibility guidelines` OR `design guidelines` OR `design principles` OR `heuristics` OR `design patterns` OR `recommendations` OR `inclusive design` OR `usability`

**人群词**：`autism` OR `ASD` OR `autistic` · `intellectual disability` OR `IDD` OR `learning disability` · `dyslexia` OR `dyscalculia` · `ADHD` · `dementia` OR `MCI` OR `cognitive decline` OR `older adults cognitive` · `traumatic brain injury` OR `TBI` OR `aphasia` OR `stroke` · `cognitive impairment` OR `neurodivergent` OR `neurodiverse`

**界面词**：`interface` OR `web` OR `mobile app` OR `interaction` OR `software` OR `text simplification` OR `easy-to-read`

### 已执行检索（按维度，site 限定 dl.acm.org / ieeexplore.ieee.org）

1. cognitive accessibility design principles + autism
2. autism design guidelines (IEEE)
3. intellectual disability accessibility design guidelines
4. dementia / age-related cognitive change + accessible tech design
5. ADHD / dyslexia web accessibility guidelines
6. aphasia / TBI accessible interface design
7. WCAG / COGA cognitive accessibility framework
8. autism software heuristics / educational app / tablet (ACM+IEEE)
9. cognitive load + neurodivergent + participatory design
10. easy-to-read / plain language / text simplification
11. intellectual disability mobile app design (IEEE)
12. autism adults workplace / sensory (CHI/ASSETS)
13. dementia UI guidelines / reminder app (IEEE)

### 工具与限制说明（透明性）

- 检索通过 Web 检索引擎对 `dl.acm.org` 与 `ieeexplore.ieee.org` 做站内限定完成；命中条目的题录与摘要可获取。
- **重要约束**：ACM (HTTP 403) 与 IEEE (HTTP 418) 对自动化全文抓取做了反爬封锁，故**全文未逐篇通读**；设计原则提取基于（a）题录+摘要，（b）开放获取镜像（arXiv / PMC / 期刊开放版），（c）权威开放标准（W3C COGA、GAIA 开源指南）。此为本综述的方法学局限，详见综述"局限"节。

---

## 4. 筛选与数据提取 (Screening & Extraction)

1. **去重** → 2. **题录/摘要筛选**（依据 §2） → 3. **数据提取**到 `corpus.md`：作者年份、venue、数据库、人群、研究类型、原则来源方法、核心设计原则。
2. **设计原则编码**：以 W3C COGA 八大目标为初始编码框架，自下而上补充人群特异性主题；编码结果见 `findings_design_principles.md`。

## 5. 分析与综合 (Synthesis)

- 描述性统计：人群分布、年份趋势、数据库/venue 分布、方法学类型 → `figures/`
- 主题综合：自闭症原则（重点）→ 各人群原则 → 跨人群共性 vs 特异性矩阵。

---

*Protocol v1 · 2026-06-03 · 对应任务 #1*
