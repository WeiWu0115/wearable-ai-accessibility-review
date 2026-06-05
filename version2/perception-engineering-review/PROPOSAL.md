# What Do We Engineer When We Engineer Perception?

**副标题(working):** A Scoping Review of Perceptual Engineering in HCI — *From the Margins to the Everyday Interaction Medium*

> 一页 review proposal / protocol 骨架 · v0.1 · 2026-06-04
> 配套基础:`../health-aspect/ADSR2.docx`(神经感知四层证据图)· `../cogaccess/`(COGA 屏幕端无障碍设计原则)
> 结构 intent 参考:Rao et al., *What Do We Design for When We Design "Smart Buildings"?* (CHI'25)

---

## 0. 中心问题 (Central Question)

> 当 HCI 构建"微调/改变人类感知"的技术时,我们究竟在工程化什么——**瞄准哪些感官、用什么手段、作用在谁的身体上、以什么科学为据、又为谁设计?**

一句话立场:感知工程当下主要服务(神经典型的)**增强/表达/娱乐**;但按 HCI 设计史的 **curb-cut 规律**,真正会沉淀为下一代日常交互 media 的,往往是为**感官非典型人群**解决"调节/容纳"而生的设计。AI + wearable 正在催生新的 everyday 交互 media——本综述**整理之前的**(感知工程版图),并据此**看向长远的**(With-Not-For 的感知多样性设计议程)。

---

## 1. 论文时间弧 (Past → Present → Future)

1. **PAST — Background 叙事:边缘→主流的扩散史。** Universal Design (Mace)、Inclusive Design ("solve for one, extend to many")、ability-based design (Wobbrock)、interdependence (Bennett/Brady/Branham);curb-cut effect 证据链:路缘坡、字幕、TTS/语音助手、预测输入、深色模式、OXO Good Grips。
2. **PRESENT — 实证主体 (corpus):** 广义 perceptual-engineering 版图。锚定 perception HCI / perceptual engineering 谱系(Jas Brooks 的味嗅温触感知工程;Ken Nakagaki / AxLab 的电刺激改变感官;EMS 的 Lopes 谱系;GVS、thermal、sensory substitution)。核心追问:**它在重复扩散规律,还是错过了它?**
3. **FUTURE — Discussion/议程:** wearable AI 作为新 everyday media;sense→actuate 闭环;接 CAWI。With, Not For(Makin & Clode, CHI'26 closing keynote)作为伦理与设计哲学。

---

## 2. 研究问题 (5 RQs)

- **RQ1 · 感知目标 (target):** 这些工作瞄准/改变哪些感官与感知目标?(沿神经四层:受器 / 门控 / 整合 / 情感)
- **RQ2 · 设计机制 (mechanism):** 用什么设计机制与刺激/调节模态?(EMS、GVS、thermal、chemical/olfactory/gustatory、vibrotactile、sensory substitution…)
- **RQ3 · 技术与身体 (technology & body):** 用什么技术与形态,与身体是 **on / in / around** 何种关系?
- **RQ4 · 如何调用神经科学 (reflexive #1):** 神经科学/心理生理学被怎么用——*motivation / mechanism / evaluation / inspiration / 缺席* × **承重程度**(表层引用 vs. load-bearing)?
- **RQ5 · 为谁设计与扩散定位 (reflexive #2,普适论点抓手):** 起点目标人群(临床/障碍特定 vs. 通用/增强)、是否声称/想象向主流 everyday 扩散、是否援引 universal design / accessibility 脉络?

> RQ1–3 = 描述版图;RQ4 = "neuroscience veneer / 神经科学贴皮"批评;RQ5 = curb-cut / 普适性批评。

---

## 3. 演绎骨架:神经感知四层模型 (deductive scaffold)

借 Rao 用"comfort 四维"当演绎种子的做法,本综述用 **`ADSR2` 的四层处理链**当 deductive coding 骨架——它是**全人类共有**的感知处理模型,神经多样人群只是其上的一种参数化(variation),因此框架天然普适、非"autism 专用":

| 层 | 功能 | 典型可作用/可感知接口 |
|---|---|---|
| **受器 Receptor** | 把物理能量转成神经信号 | 多为临床(ERG/ABR);可穿戴 proxy 有限 |
| **门控 Gating** | 筛选/调音量(E/I、SOR) | EDA / HRV(感知);attenuation(作用) |
| **整合 Integration** | 多感觉绑定、TBW、姿势 | IMU(感知);sensory substitution / TBW 训练(作用) |
| **情感 Affective** | 给信号贴威胁/效价标签 | HRV+心跳任务(感知);interoceptive feedback(作用) |

**跨域呼应(预期 finding):** `ADSR2` 发现 autism 文献里"**门控层被普遍高估**";若感知工程 HCI 也大量"调节注意/过滤"的 claim 而证据薄,即为同一批评的跨域汇合。

---

## 4. 综合句式模板 (Fig.3 analog)

> *In this paper, **[actuation / sensing technology]** is used to **[augment / substitute / attenuate / calibrate]** **[sensory target]** by acting on **[perceptual processing layer]**, grounded in **[neuroscience construct]**, for **[population / generalization framing]**.*

并据此把领域排在一条谱上:**augment 增强 ↔ substitute 替代 ↔ regulate/attenuate 调节衰减**,问:perceptual diversity 落在哪儿(预期:几乎缺席 = 核心 gap)。

---

## 5. 方法 (PRISMA-ScR · Arksey & O'Malley 五阶段)

**PCC:**
- **Population/Perspective:** 被作用的使用者/身体(全体;标注 atypical vs. typical 感知)。
- **Concept:** perceptual engineering — 有意 *modulate / augment / substitute / attenuate* 人类感官感知的技术。
- **Context:** HCI 研究(CHI / UIST / TEI / DIS / IMWUT / CHI EA 等)。

**检索框架(双库 = "桥"的方法学签名):** ACM DL + 生物医学/工程库(Scopus 和/或 PubMed/IEEE)。三组关键词笛卡尔组合(仿 Rao Fig.2):
`感官/感知 terms` × `刺激/作用/感知工程 terms` × `HCI venue/context terms`。

**编码:** hybrid deductive(四层 + RQ4 两轴 + RQ5 人群/扩散轴)+ inductive(机制/技术主题归纳)。charting 模板记录:title / authors / year / venue / 技术 / 模态 / 目标层 / 神经调用类型·承重 / 目标人群 / 扩散定位 / 关键发现。

**Scope 决策(写作前枚举再主动取舍,仿 `ADSR2` §0.5):** 纳入的感官域、刺激模态、是否含 VR/AR 感官改写、是否含纯临床/医疗器械(倾向排除无 HCI 设计意图者)、时间窗(default **2013–2025**,覆盖 EMS/感知工程兴起期,待定)。

---

## 6. 伦理立场 (必须正面接)

curb-cut 的反面:把残障/神经多样人群当"主流创新的 R&D 实验室"是 instrumentalizing(cf. Liz Jackson, *disability dongle*)。**本综述立场:不是"为边缘设计好让主流捡便宜",而是"与 perceptual diversity 一起设计(With, Not For),扩散是副产品而非目的"。** "With, Not For" 在此承重,而非装饰。

---

## 7. 贡献 (Contribution claims)

1. 首个以**神经感知处理模型(四层)为演绎骨架**、跨 ACM DL + 生物医学库的 perceptual-engineering HCI 范围综述——方法学本身即"神经 × HCI"的桥。
2. 一套描述领域的**框架 + 句式模板**(actuation × sensory target × 处理层 × 神经根据 × 人群)+ augment↔substitute↔regulate 谱。
3. 经 RQ4/RQ5 揭示 **"神经科学贴皮" + "门控被高估"的跨域汇合**,与 **perceptual diversity 在感知工程中的系统性缺席**,据此提出 **From-the-Margins-to-the-Everyday / With-Not-For** 设计议程,接 wearable AI / CAWI 闭环。

---

## 8. 局限 (Limitations)

- scoping review:描绘版图与缺口,不做质量评级 / 效果 meta。
- 全文逐篇通读受数据库访问限制(承接 `ADSR2` / `cogaccess` 既有局限);正式投稿前需逐篇核对。
- 检索覆盖:venue 与库的选择会影响命中;灰文献/非英文覆盖有限。

---

## 9. 下一步 (Next)

1. 锁定 scope 决策(感官域、模态、时间窗、venue 清单)。
2. 起草双库检索式(三组关键词)+ pilot search。
3. 建 charting 模板表(对应第 5 节字段)。
4. 决定 push 范围(本 proposal / 整个 version2 / git 清理)。

*v0.1 · 2026-06-04 · 对应"perception × neuro scoping review"立项*
