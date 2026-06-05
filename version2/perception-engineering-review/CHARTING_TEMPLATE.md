# Charting 模板 + Codebook (Data Extraction)

> Perceptual Engineering Scoping Review · v1 · 2026-06-05
> 配套:`SEARCH_STRATEGY.md` · `PROPOSAL.md`(RQ 定义)· 可导入文件 `charting_template.csv`
> 用法:每篇纳入文献一行。**编码字段尽量用下方 codebook 的受值**(多选用 `;` 分隔);自由文本字段照实写。Arm A/B 共用同一张表,用 `arm` 列区分。

---

## 字段表(列 ↔ RQ ↔ 取值)

| # | 字段 (CSV 列名) | RQ | 类型 | 取值 / Codebook |
|---|---|---|---|---|
| 1 | `id` | — | 文本 | 唯一编号(如 A001 / B001) |
| 2 | `arm` | — | 单选 | `A-HCI` / `B-Clinical` |
| 3 | `title` | — | 文本 | 标题 |
| 4 | `authors` | — | 文本 | 第一作者 et al. |
| 5 | `year` | — | 数字 | 2013–2025 |
| 6 | `venue` | — | 文本 | CHI / UIST / ToH / PubMed 期刊… |
| 7 | `doi` | — | 文本 | DOI / 链接 |
| 8 | `modality` | RQ1 | 多选 | `vision` `auditory` `tactile` `thermal` `pain` `proprioceptive` `vestibular` `interoceptive` `olfactory` `gustatory` `multisensory` |
| 9 | `layer` | RQ1 | 多选 | `receptor` `gating` `integration` `affective` `other-pathway`(主通路外,注明) |
| 10 | `actuation` | RQ2 | 多选 | `EMS` `GVS` `electrotactile` `electric-taste` `tDCS/tACS` `vibrotactile` `force-feedback` `ultrasound-haptic` `pseudo-haptic` `thermal` `olfactory-display` `gustatory` `optical` `acoustic` `sensory-substitution` `physiological-feedback` |
| 11 | `action_type` | RQ2 | 单选 | `augment` / `substitute` / `attenuate` / `calibrate` |
| 12 | `form_factor` | RQ3 | 文本 | 设备 / 形态(如 wristband, glasses, mouthpiece) |
| 13 | `body_relation` | RQ3 | 单选 | `on-body` / `in-body` / `around-body` |
| 14 | `neuro_use` | RQ4 | 单选 | `motivation` / `mechanism` / `evaluation` / `inspiration` / `absent` |
| 15 | `neuro_loadbearing` | RQ4 | 单选 | `surface`(表层引用) / `load-bearing`(承重) |
| 16 | `validation` | RQ4 | 单选 | `objective/biosensor` / `behavioral-task` / `self-report-only` / `mixed` / `none` |
| 17 | `ethics_addressed` | RQ4 | 单选 | `yes` / `partial` / `no`(是否核算后果/可逆性/body-schema 等) |
| 18 | `population` | RQ5 | 单选 | `clinical/disability-specific` / `general/augmentation` / `both` |
| 19 | `perc_diversity_centered` | RQ5 | 单选 | `yes` / `no` |
| 20 | `generalization_claim` | RQ5 | 单选 | `yes`(声称/想象向主流 everyday 扩散) / `no` |
| 21 | `accessibility_lineage` | RQ5 | 单选 | `yes`(援引 universal/inclusive/ability-based design 脉络) / `no` |
| 22 | `sentence_template` | 综合 | 文本 | 见下方句式模板,逐篇实例化 |
| 23 | `key_finding` | 综合 | 文本 | 一句话关键发现 |
| 24 | `include_intervention` | 筛选 | 单选 | `intervention`(纳入) / `evaluation-only`(排除) / `excluded-other`(注明原因) |
| 25 | `reviewer` | — | 文本 | 1st / 2nd / 冲突解决者 |
| 26 | `notes` | — | 文本 | 备注(其他通路、争议、待核) |

---

## 句式模板(填 `sentence_template` 列)

> *[actuation] is used to **[augment / substitute / attenuate / calibrate]** [modality] by acting on **[layer]**, grounded in [neuro construct], for **[population]**.*

---

## CSV 表头(复制进 Excel / Covidence)

```
id,arm,title,authors,year,venue,doi,modality,layer,actuation,action_type,form_factor,body_relation,neuro_use,neuro_loadbearing,validation,ethics_addressed,population,perc_diversity_centered,generalization_claim,accessibility_lineage,sentence_template,key_finding,include_intervention,reviewer,notes
```

## 示例行(illustrative,EMS 谱系)

| 字段 | 值 |
|---|---|
| id | A001 |
| arm | A-HCI |
| modality | proprioceptive;tactile |
| layer | receptor;gating |
| actuation | EMS |
| action_type | substitute |
| body_relation | on-body |
| neuro_use | mechanism |
| neuro_loadbearing | load-bearing |
| validation | objective/biosensor |
| ethics_addressed | partial |
| population | general/augmentation |
| perc_diversity_centered | no |
| generalization_claim | yes |
| accessibility_lineage | no |
| sentence_template | EMS is used to **substitute** motor/proprioceptive control by acting on the **receptor–gating** segment, grounded in motor-unit recruitment, for **general/augmentation** users. |
| include_intervention | intervention |

---

## 编码注意(对接会议口径)

- **`include_intervention`**:技术须作为 **intervention**;仅作 **evaluation 手段** 的排除。
- **`layer` = other-pathway**:四层是主通路,autism 复杂、可能并存其他通路 → 落在主通路外的机制标 `other-pathway` 并在 `notes` 注明,不强塞。
- **`validation` / `neuro_loadbearing`**:自评 / 量表是 **proxy**(非特异 + autism baseline drift)——合理但单独背书神经机制 claim 即记为 `self-report-only` + `surface`,这是 **neural veneer** 的判据。
- **`ethics_addressed`**:是否核算对神经通路干预的后果(如 body-schema 改写后的可逆性、幻肢风险)。
- 两臂最终用 `layer` 列把 Arm A 的 HCI 工作与 Arm B 的医学通路/断点 **相互 map**。

*v1 · 2026-06-05*
