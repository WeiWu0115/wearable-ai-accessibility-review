# Scope & Search Strategy — 会议决策稿

> 用途:与医学合作者 + HCI researcher 当面敲定 scoping review 的**主题与检索策略**。
> 每个决策格留了 `□ 同意 / 调整为: ____`,会上直接填。
> 配套:`PROPOSAL.md`(立项)· `../health-aspect/ADSR2.docx`(神经四层证据图)· `../cogaccess/`(屏幕端无障碍原则)
> v0.1 · 2026-06-04

---

## 1. 主题陈述 (一句话开场)

> 综述对象 = **perceptual engineering**:*有意去微调 / 增强 / 替代 / 衰减人类感官知觉的交互技术*(结合 CS + 神经生物学 + 心理生理学)。用一条**全人类共有的神经感知处理链(受器 → 门控 → 整合 → 情感)**当透镜,问 HCI 在为谁、用什么手段、作用于哪一层做这件事,并揭示感官多样人群的系统性缺席。

中心问题:**What Do We Engineer When We Engineer Perception?**

---

## 2. 核心纳入判据(最重要的一条筛选线)

> **技术必须"作用于知觉本身",而非只是"呈现信息"。**
> EMS 让手动、GVS 改变平衡、热致幻、电子味觉、感官替代 → 纳入;普通 AR 卡片、普通通知 → 排除。

`□ 同意 / 调整为: ____`

---

## 3. Scope 五维(逐格拍板)

| 维度 | 推荐 | 决策 |
|---|---|---|
| **感官域** | 全九感纳入:视 / 听 / 触压 / 痛温 / 本体 / 前庭 / 内感受 / **嗅 / 味**。*与 `ADSR2` 故意分道*:ADSR2 因"难可穿戴测"排除嗅味,但感知工程 HCI 的嗅味子领域活跃,本综述纳入。 | `□ 同意 / 调整: ____` |
| **作用模态** | 电(EMS/GVS/电触觉/电味/tDCS·tACS)· 机械触觉(振动/力反馈/超声触觉/pseudo-haptic)· 热(Peltier/热致幻)· 化学(嗅显示/味觉)· 光与声(**错觉级,非内容级**)· 感官替代(跨模态映射)· 生理反馈(HRV/EDA 闭环) | `□ 同意 / 补漏: ____` |
| **时间窗** | **2010–2025**(EMS/actuated 浪潮 + 化学感官近十年爆发);Bach-y-Rita 1969 等奠基只在 Background 引,不进 corpus | `□ 同意 / 调整: ____` |
| **数据库 / venue** | **ACM DL + IEEE Xplore + Scopus**。venue:CHI / UIST / TEI / DIS / CHI EA / **Augmented Humans** / IMWUT·UbiComp / ISS / MobileHCI;IEEE:**World Haptics / ToH / IEEE VR**。Scopus 做跨学科补全 + snowballing。PubMed 选配(RQ4 神经依据交叉核对) | `□ 同意 / 增删: ____` |
| **纳入 / 排除** | **纳入**:有 HCI/交互设计贡献且有意作用于知觉。**排除**:纯信息展示 UI;纯临床疗效试验(无设计贡献);纯 read-out/控制型 BCI;非英文;二次综述 | `□ 同意 / 调整: ____` |

---

## 4. 两位专家专属决策清单(会议重点)

**给医生(临床 / 神经边界):**
- `□` 神经刺激(tDCS / tACS / TMS)纳入还是单列?(推荐:HCI venue 内、针对知觉的纳入;侵入式 BCI 另案)
- `□` 临床假体(人工耳蜗 / 视网膜假体 / TENS 镇痛)只进 Background、不进 corpus?(推荐:是)
- `□` 背书 RQ4 编码口径(神经科学被怎么用:motivation / mechanism / evaluation / inspiration / 缺席 × 承重)

**给 HCI researcher(领域边界):**
- `□` VR/AR 切法:**知觉级**(redirected walking / 跨模态错觉 / 感官重映射)纳入、**内容级**排除?(推荐:是)
- `□` 感官替代 / 辅助设备(vOICe / BrainPort)算 perceptual engineering?(推荐:纳入,是 margins→everyday 的桥)
- `□` venue / 模态有无遗漏(SIGGRAPH 知觉工作?ToH 触觉错觉?)

---

## 5. 检索策略(三组关键词笛卡尔组合,仿 Rao et al. Fig.2)

`A 感知目标` **AND** `B 作用 / 工程化动作` **AND** (`C 语境` 或改用 venue 限定)

```
A — 感知 / 感官目标:
(perception OR perceptual OR sensory OR multisensory OR cross-modal OR
 propriocept* OR vestibular OR haptic OR tactile OR thermal OR
 olfact* OR smell OR gustat* OR taste OR interocept* OR "sensory substitution")

B — 作用 / 工程化(关键的 "act on" 动词,排掉纯展示):
(stimulat* OR "electrical muscle stimulation" OR EMS OR "galvanic vestibular" OR GVS OR
 electrotactile OR "electro-tactile" OR actuat* OR augment* OR substitut* OR
 illusion OR "pseudo-haptic" OR modulat* OR "sensory feedback" OR biofeedback OR
 "perceptual engineering")

C — HCI 语境(若已用 venue 限定可省略):
(HCI OR "human-computer interaction" OR interface OR wearable OR
 "interaction design" OR "user experience" OR on-body OR "augmented human")
```

务实提醒:
- 先在 ACM DL 跑 **pilot**(取前 ~20% 读),按命中率收紧 B 组(`augment*`/`modulat*` 会带进太多无关 UI,靠 venue + 标题/摘要筛兜底)。
- 目标 corpus 体量对标 Rao 的 ~192;靠"必须作用于知觉"这条线 + venue 限定把初筛压到可读规模。

---

## 6. 计划产出图表

1. **★ 各感官模态"出现 / 爆发"时间线(signature 图)** —— papers/year 按模态分层。Covidence 提取含 `年份 × 模态`,**编码即副产品**。
   - 预期叙事(待 corpus 证实):视/听 → 触觉·力反馈(2000s)→ **EMS/GVS 身体致动(~2013 起爆)** → 热/嗅/味化学感官(2010s 后段)→ **内感受/情感界面(~2018+,最新)**。
   - 论点:**HCI 在时间上一路从"屏幕附近的外感受"钻向"身体内部的内感受/情感"——而内部正是 `ADSR2` 标出的可穿戴前沿与 autism 内感受失配所在。领域轨迹笔直开向感官多样性最要紧、却刚抵达的那片地。** 同时坐实 Past→Present→Future 与 margins→everyday。
2. 模态 × 处理层(受器/门控/整合/情感)矩阵 —— 看声称作用在哪层 vs. 真有神经证据在哪层(对接 RQ4 + `ADSR2` "门控被高估")。
3. augment ↔ substitute ↔ regulate/attenuate 谱 × 目标人群(对接 RQ5,显示 perceptual diversity 缺席)。
4. 句式模板汇总图(actuation × sensory target × 处理层 × 神经根据 × 人群)。

---

## 7. 会后下一步

1. 把第 3–4 节的决策填定 → 锁 scope。
2. 据此定稿双库检索式 + 跑 pilot search。
3. 在 Covidence 单独做数据提取(charting),字段在 Covidence 配置。
4. 画时间线 v0(哪怕用 pilot 子集),验证第 6.1 节叙事。

*v0.1 · 2026-06-04 · 会议决策稿*
