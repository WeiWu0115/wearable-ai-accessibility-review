# 检索策略 · 对称双臂 (Search Strategy)

> Perceptual Engineering Scoping Review · v1 · 2026-06-05
> 配套:`PROPOSAL.md`(立项)· `SCOPE.md`(scope 决策)· 交互版见 `perception_review_scope.html#search`
> 方法:PRISMA-ScR · Arksey & O'Malley 五阶段 · **对称双臂**(每个领域专家在自己臂当 1st reviewer、在对方臂当 2nd reviewer)· Covidence 两遍筛(标题摘要 → 全文)+ 第三 reviewer 解冲突 → 两臂最终 corpus **相互 map**

**时间窗(两臂共用):2013–2025**
- 医学侧:DSM-5(2013)统一为单一 ASD、改维度化严重程度分级、**首次将「感觉异常」列为核心特征**;2003 前研究多被推翻 → 自然排除。
- HCI 侧:~2015 可穿戴 / 泛在计算与生物信息成为 daily device。

---

## 臂 A · HCI 感知工程  (HCI researcher 版 · 2026-06-05)

**库:** ACM DL + IEEE Xplore(+ Scopus 跨学科补全 / snowballing)
**venue:** CHI · UIST · TEI · DIS · CHI EA · Augmented Humans · IMWUT/UbiComp · ISS · MobileHCI;IEEE: World Haptics · ToH · IEEE VR
**reviewer:** HCI = 1st(检索 + 建库),医学生 = 2nd · English · 2013–2025
**式:** `A` AND `B` AND `C`(收敛后的单一版,取代早先 A1/A2 两变体)。

```
A — 感知 / 感官目标:
(
  perception OR perceptual OR sensory OR multisensory OR "multi-sensory"
  OR crossmodal OR "cross-modal" OR multimodal OR "multi-modal"
  OR propriocept* OR vestibular OR haptic OR tactile OR thermal
  OR olfact* OR smell OR gustat* OR taste OR interocept*
  OR "sensory substitution" OR "sensory augmentation" OR "sensory modulation"
)
AND
B — 作用 / 工程化:
(
  stimulat* OR "electrical muscle stimulation" OR EMS
  OR "galvanic vestibular stimulation" OR "galvanic vestibular" OR GVS
  OR electrotactile OR "electro-tactile"
  OR actuat* OR actuator*
  OR augment* OR substitut* OR modulat* OR regulat*
  OR illusion OR "pseudo-haptic" OR pseudohaptic
  OR "sensory feedback" OR "perceptual feedback"
  OR biofeedback OR neurofeedback
  OR "perceptual engineering"
)
AND
C — HCI 语境:
(
  HCI OR "human-computer interaction"
  OR interface* OR wearable* OR "wearable computing"
  OR "interaction design" OR "interactive system*" OR "user interface*"
  OR "user experience" OR UX
  OR on-body OR "on body"
  OR "augmented human" OR "human augmentation"
)
```

**注:** 臂 A **纳入嗅 / 味**(感知工程嗅味子领域活跃 —— 与臂 B 相反)。若 B 组 `augment*`/`modulat*`/`regulat*` 召回噪声大,可退回具名技术子集(EMS/GVS/electrotactile/pseudo-haptic/illusion/"sensory substitution"…)提精度。
**筛选期排除(Covidence,非检索词):** 仅作 **evaluation** 手段者 → 排(技术须作为 **intervention**);纯信息展示 UI;纯 read-out / 控制型 BCI;二次综述;非英文。

---

## 臂 B · 临床(autism 诊断与治疗)  (医生版 · 2026-06-05)

**库:** PubMed(+ Scopus),基于 `ADSR2` MeSH · 2013–2025
**reviewer:** 医学生 = 1st(检索 + 建库),HCI = 2nd
**式:** `P` AND `(感觉域块 OR …)` AND `诊断/治疗`,**按 7 个感觉域分块**(可分别跑或 OR 合并)。
> 医生版(会上);她在具体检索时会按命中调整。**注:四阶段神经通路(受器→门控→整合→情感)是 *coding / 合流* 的脚手架;搜索本身按 *感觉域* 组织。**

```
P — autism 人群(每条都 AND 上):
("Autism Spectrum Disorder"[Mesh] OR autis*[tiab] OR ASD[tiab] OR "Asperger*"[tiab] OR neurodivers*[tiab])

AND 以下感觉域(任一;可分别跑或 OR 合并):
① 视觉: ("Electroretinography"[Mesh] OR electroretinog*[tiab] OR ERG[tiab] OR "Retina"[Mesh] OR retina*[tiab] OR photoreceptor*[tiab] OR "Visual Perception"[Mesh] OR "visual processing"[tiab])
② 听觉: ("Evoked Potentials, Auditory, Brain Stem"[Mesh] OR "auditory brainstem response"[tiab] OR ABR[tiab] OR "otoacoustic emission*"[tiab] OR cochlea*[tiab] OR "Hearing Loss"[Mesh] OR audiomet*[tiab] OR "Auditory Perception"[Mesh])
③ 触压觉(含振动/纹理): ("Touch"[Mesh] OR "Touch Perception"[Mesh] OR tactile[tiab] OR somatosensory[tiab] OR "tactile defensiveness"[tiab] OR vibrotactile[tiab] OR vibration[tiab] OR "texture perception"[tiab] OR mechanoreceptor*[tiab] OR Shank3[tiab] OR Mecp2[tiab] OR Fmr1[tiab])
④ 痛温觉: ("Pain"[Mesh] OR "Pain Perception"[Mesh] OR "Pain Threshold"[Mesh] OR nocicept*[tiab] OR "pain sensitivity"[tiab] OR "quantitative sensory testing"[tiab] OR QST[tiab] OR "Thermoreceptors"[Mesh] OR "thermal perception"[tiab] OR "temperature perception"[tiab] OR allodynia[tiab] OR hyperalgesia[tiab])
⑤ 本体觉: ("Proprioception"[Mesh] OR propriocept*[tiab] OR kinesth*[tiab] OR "Muscle Spindles"[Mesh] OR sensorimotor[tiab] OR "motor control"[tiab])
⑥ 前庭觉: ("Vestibule, Labyrinth"[Mesh] OR vestibul*[tiab] OR "Postural Balance"[Mesh] OR postural[tiab] OR balance[tiab] OR "Vestibular Function Tests"[Mesh] OR otolith*[tiab] OR "semicircular canal*"[tiab])
⑦ 内感受: ("Interoception"[Mesh] OR interocept*[tiab] OR "Autonomic Nervous System"[Mesh] OR "heart rate variability"[tiab] OR "Heart Rate"[Mesh] OR "Galvanic Skin Response"[Mesh] OR electroderm*[tiab] OR "heartbeat tracking"[tiab] OR "respiratory sinus arrhythmia"[tiab])

AND 诊断 / 治疗:
(diagnos* OR "DSM-5" OR assessment OR treatment OR intervention OR therap* OR rehabilitation)
```

**默认排除(留作记录,不跑):** 嗅 / 味化学感官 —— `("Olfactory Perception"[Mesh] OR olfact*[tiab] OR smell[tiab] OR "Taste Perception"[Mesh] OR gustat*[tiab] OR taste[tiab] OR chemosens*[tiab])`;仅当综述触及进食 / 营养时再启用。(注:臂 A 反而纳入嗅 / 味。)
**筛选期排除:** 非 autism 条件的临床假体(人工耳蜗 / 视网膜假体 / TENS)→ 仅 Background / Future Work,不进搜索。

---

## 合流 · Map

两臂各产出最终 corpus → 沿**四阶段神经通路(受器 → 门控 → 整合 → 情感)**把两套 paper **相互 map**:把臂 A 的 HCI 工作对位到臂 B 的医学通路 / 断点。

**数据提取(charting):** 在 Covidence 单独进行,字段在 Covidence 配置;不在本仓库维护。

---

## 务实提醒

- 先在 ACM DL 跑 **pilot**(取前 ~20% 读):若 A/B 的 `augment*`/`modulat*`/`regulat*` 召回噪声大,退回具名技术子集提精度,靠 venue + 标题/摘要筛兜底。
- 目标 corpus 体量对标 Rao 的 ~192。
- 自评 / 量表是 **proxy**(非特异:焦虑 / 抑郁均可致心率·呼吸变化;autism 还有 baseline drift):合理但不应**单独**为神经机制 claim 背书 → 编码 RQ4 时记录验证方式。
- 两位专家均表示**具体检索时会再微调**;本文件为会上(2026-06-05)定稿版。

*v3 · 2026-06-05 · 臂 A = HCI researcher 收敛 A/B/C;臂 B = 医生 7 感觉域*
