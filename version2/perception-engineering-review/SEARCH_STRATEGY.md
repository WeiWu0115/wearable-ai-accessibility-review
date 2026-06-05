# 检索策略 · 对称双臂 (Search Strategy)

> Perceptual Engineering Scoping Review · v1 · 2026-06-05
> 配套:`PROPOSAL.md`(立项)· `SCOPE.md`(scope 决策)· 交互版见 `perception_review_scope.html#search`
> 方法:PRISMA-ScR · Arksey & O'Malley 五阶段 · **对称双臂**(每个领域专家在自己臂当 1st reviewer、在对方臂当 2nd reviewer)· Covidence 两遍筛(标题摘要 → 全文)+ 第三 reviewer 解冲突 → 两臂最终 corpus **相互 map**

**时间窗(两臂共用):2013–2025**
- 医学侧:DSM-5(2013)统一为单一 ASD、改维度化严重程度分级、**首次将「感觉异常」列为核心特征**;2003 前研究多被推翻 → 自然排除。
- HCI 侧:~2015 可穿戴 / 泛在计算与生物信息成为 daily device。

---

## 臂 A · HCI 感知工程

**库:** ACM DL + IEEE Xplore(+ Scopus 跨学科补全 / snowballing)
**venue:** CHI · UIST · TEI · DIS · CHI EA · Augmented Humans · IMWUT/UbiComp · ISS · MobileHCI;IEEE: World Haptics · ToH · IEEE VR
**式:** `A` AND `B` AND(`C` 或 venue 限定),English,2013–2025

```
A — 感知 / 感官目标:
(perception OR perceptual OR sensory OR multisensory OR cross-modal OR
 propriocept* OR vestibular OR haptic OR tactile OR thermal OR
 olfact* OR smell OR gustat* OR taste OR interocept* OR "sensory substitution")
AND
B — 作用 / 工程化("act on" 动词,排掉纯展示):
(stimulat* OR "electrical muscle stimulation" OR EMS OR "galvanic vestibular" OR GVS OR
 electrotactile OR "electro-tactile" OR actuat* OR augment* OR substitut* OR
 illusion OR "pseudo-haptic" OR modulat* OR "sensory feedback" OR biofeedback OR
 "perceptual engineering")
AND
C — HCI 语境(用 venue 限定可省略):
(HCI OR "human-computer interaction" OR interface OR wearable OR
 "interaction design" OR "user experience" OR on-body OR "augmented human")
```

**reviewer:** HCI = 1st(检索 + 建库),医学生 = 2nd。
**筛选期排除(Covidence,非检索词):** 仅作 **evaluation** 手段者 → 排(技术须作为 **intervention**);纯信息展示 UI;纯 read-out / 控制型 BCI;二次综述;非英文。

---

## 臂 B · 临床(autism 诊断与治疗)

**库:** PubMed(+ Scopus),基于 `ADSR2` MeSH,2013–2025
**式:** `P` AND `通路概念(四层 OR)` AND `诊断/治疗`

```
P — autism 人群(所有式都 AND 上):
("Autism Spectrum Disorder"[Mesh] OR autis*[tiab] OR ASD[tiab] OR Asperger*[tiab] OR neurodivers*[tiab])
AND
通路概念(四层任一,OR 合并;可加其他通路):
  受器: (electroretinog* OR ERG OR "auditory brainstem response" OR ABR OR tactile OR somatosensory OR "tactile defensiveness")
  门控: ("sensory gating" OR GABA OR thalam* OR "excitatory inhibitory" OR "sensory over-responsivity")
  整合: (multisensory OR "temporal binding window" OR audiovisual OR crossmodal OR postural)
  情感: (insula* OR amygdala OR interocept* OR "heart rate variability" OR "sensory sensitivity")
AND
诊断 / 治疗:
(diagnos* OR "DSM-5" OR assessment OR treatment OR intervention OR therap* OR rehabilitation)
```

**reviewer:** 医学生 = 1st(检索 + 建库),HCI = 2nd。
**说明:** 四层是**主通路**;autism 复杂,**可能并存其他通路**,可加行扩展。各层可分别检索,或如上 OR 合并成一条广检。
**筛选期排除:** 非 autism 条件的临床假体(人工耳蜗 / 视网膜假体 / TENS)→ 仅 Background / Future Work,不进搜索。

---

## 合流 · Map

两臂各产出最终 corpus → 沿**四阶段神经通路(受器 → 门控 → 整合 → 情感)**把两套 paper **相互 map**:把臂 A 的 HCI 工作对位到臂 B 的医学通路 / 断点,即最终 charting 表。

**charting 字段:** title / authors / year / venue / 技术 / 模态 / 目标层 / 神经调用类型·承重 / augment-substitute-regulate / 目标人群 / 扩散定位 / 关键发现。

---

## 务实提醒

- 先在 ACM DL 跑 **pilot**(取前 ~20% 读),按命中率收紧臂 A 的 B 组(`augment*`/`modulat*` 会带进太多无关 UI,靠 venue + 标题/摘要筛兜底)。
- 目标 corpus 体量对标 Rao 的 ~192。
- 自评 / 量表是 **proxy**(非特异:焦虑 / 抑郁均可致心率·呼吸变化;autism 还有 baseline drift):合理但不应**单独**为神经机制 claim 背书 → 编码 RQ4 时记录验证方式。

*v1 · 2026-06-05*
