# 进度 / 续作 (Progress — Resume Here)

> Perceptual Engineering Scoping Review · 更新于 2026-06-05
> **下次打开先读这页。** 它说明现在到哪一步、已锁的决策、文件分工、下一步该干嘛。

---

## 一句话状态

立项 + scope + **双臂检索策略已定稿**(2026-06-05 会上,医生 + HCI researcher 各给检索式)。**下一步 = 跑 pilot 拿真实命中量**,再据此微调检索式、建 Covidence 库、开始两遍筛。

---

## 这篇论文是什么

- **题:** *What Do We Engineer When We Engineer Perception?*(reflexive 主题)· 副题 *From the Margins to the Everyday Interaction Medium*
- **对象:** perceptual engineering(有意作用于人类知觉的 HCI 技术)。
- **核心论点:** HCI 把神经科学的**词与工具**搬进感知工程,却**没搬医学的纪律与伦理**(neural veneer / 拿临床工具靠「你感觉到了吗」验证 / 改神经通路不顾后果)。用临床理解神经多样性的**真实通路(受器→门控→脑岛整合→情感)**当尺,从 autism/neurodiverse 切入推普适,为 wearable AI 立**有据、可问责、可及**的议程。
- **结构 intent:** 仿 Rao et al.《Smart Buildings》(CHI'25);PRISMA-ScR。

## 已锁决策(2026-06-05)

- **时间窗 2013–2025**(医学:DSM-5 统一 ASD + 感觉异常列核心;HCI:可穿戴/泛在计算成 daily device)。
- **对称双臂流程**:每个领域专家在自己臂当 1st reviewer、在对方臂当 2nd;Covidence 两遍筛(标题摘要→全文)+ 第三 reviewer 解冲突;两臂最终 corpus 沿四层**相互 map**。
- **臂 A(HCI)** = 收敛单一 A/B/C(纳入嗅/味);**臂 B(临床 autism dx/tx)** = 按 **7 感觉域**分块(嗅味默认排除)。
- **纳排:** 技术须作 **intervention**(仅作 evaluation 者排除);非-autism 临床假体(人工耳蜗/视网膜/TENS)仅 Background/Future。
- **量表口径:** 自评/量表是 proxy(非特异 + autism baseline drift),合理但**不可单独**为机制 claim 背书 = neural veneer 判据。
- **四层 = coding/合流脚手架;搜索按感觉域(臂B)/ A·B·C(臂A)组织。**
- **charting 在 Covidence 单独做**,不在本仓库。

## 文件分工(version2/perception-engineering-review/)

| 文件 | 内容 |
|---|---|
| `PROPOSAL.md` / `perception_review_proposal.html` | 立项:中心问题、5 RQ、四层骨架、方法、伦理、贡献(含 abstract 中英) |
| `SCOPE.md` / `perception_review_scope.html` | scope 决策稿 + **现场可编辑双臂检索构建器**(§5,导出 CSV/决策摘要) |
| `SEARCH_STRATEGY.md` | **检索式权威定稿**(v3:臂A 收敛 A/B/C;臂B 7 感觉域) |
| `../../search_protocol_v2.html` | 双臂检索协议(read 版,网页);v1 = 原 CAWI 七层协议保留 |
| `PILOT_PLAN.md` | pilot 流程 + 预期命中量估算 + **回填表(待填真实 n)** |
| `../health-aspect/ADSR2.docx` | 医学侧神经四层证据图(臂B MeSH 来源) |
| `../cogaccess/` | 屏幕端 COGA 无障碍设计原则 |

> 私有(已 gitignore,不在 repo):`recording for scope/`(会议录音 + 转录 + 纪要 meeting_notes_2026-06-05.md)。

## 下一步(TODO)

1. **跑 pilot**:臂 A 在 ACM DL 跑 A AND B AND C(2013–2025),读前 ~20%,算 precision → 填 `PILOT_PLAN.md` 回填表。
2. 据 precision 微调臂 A B 组(噪声大→退具名技术子集);两位专家均会再微调。
3. 全量上 IEEE + Scopus(臂A)/ PubMed + Scopus(臂B)→ Covidence 建库。
4. 两遍筛 → 两臂最终 corpus → 沿四层 map。
5. 画**各感官模态时间线** signature 图(验证「钻向内感受」叙事)。

## 线上

- 主页 https://weiwu0115.github.io/wearable-ai-accessibility-review/
- Proposal `/perception_review_proposal.html` · Scope `/perception_review_scope.html` · Protocol v2 `/search_protocol_v2.html`

*Resume note · 2026-06-05*
