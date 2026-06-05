# 臂 A · Pilot 检索方案 + 预期命中量

> Perceptual Engineering Scoping Review · v1 · 2026-06-05
> 配套:`SEARCH_STRATEGY.md`(检索式)· 数据提取(charting)在 Covidence 单独进行
> ⚠️ 下表数字是**量级估算**(基于领域与 venue 经验),非实库计数。**跑 pilot 后用真实 n 替换。**

---

## 1. 目标漏斗(对标 Rao 5,548 → 192)

| 阶段 | 估计 n(ACM DL + IEEE + Scopus,2013–2025) | 说明 |
|---|---|---|
| Identification(A AND B AND C) | **~3,000–7,000** | B 组 `augment*`/`modulat*`/`stimulat*` 偏宽,会灌入大量无关 |
| 去重后 | ~2,500–5,500 | Covidence 自动去重 |
| 标题+摘要筛 | → **~400–700** | 应用「作用于知觉≠展示信息」「intervention≠evaluation」 |
| 全文筛 | → **~150–250** | 最终 corpus(目标体量 ≈ Rao 的 192) |

> 若 Identification 远超 7,000 → B 组过宽,按 §3 收紧;若全文 < 100 → A/B 漏检或排除过严,放宽或补 venue 手检。

---

## 2. 预期纳入量 · 按模态(供时间线图 + 总量 sanity)

| 模态 / 子领域 | 预估纳入 | 起爆期(时间线预期) |
|---|---|---|
| EMS(Lopes/Baudisch 谱系等) | ~40–70 | ~2013 起爆 |
| 振触 / 力反馈 / 超声触觉(限「错觉/替代/调制」) | ~30–60 | 持续 |
| pseudo-haptic / 触觉错觉 | ~25–45 | 2013+ |
| 热 / 温度(Peltier、热致幻) | ~25–45 | 2010s 后段 |
| 嗅觉显示 | ~30–55 | 2010s 后段回潮 |
| 味觉 / 电味(Ranasinghe、Brooks) | ~15–30 | 2016+ |
| GVS / 前庭 | ~12–25 | 散布 |
| sensory substitution(HCI) | ~20–40 | 持续 |
| 内感受 / 生理反馈界面 | ~10–25 | ~2018+ 最新 |
| **合计(去重叠后)** | **~150–250** | 越往内部越新 → 印证「钻向内感受」叙事 |

> 这张表本身就是**时间线 signature 图**的预期形状;真实计数填入后即可画 v0。

---

## 3. Pilot 流程(先只跑 ACM DL)

1. 在 **ACM DL** 跑 `A AND B AND C`(2013–2025)→ 记 **n_total**(预估 ACM 子集 ~800–2,000)。
2. 按相关性/时间取**前 ~20%** 读标题+摘要 → 标注是否真属 perceptual engineering(作用于知觉)。
3. 算 **precision = 命中 / 已读**:
   - precision ≥ ~25% → 检索式 OK,直接全量上 IEEE + Scopus。
   - precision ~15–25% → 收紧 B(见 §3 narrow 变体)。
   - precision < ~15% → B 过宽,换 narrow 变体 + 强制 venue 限定。
4. 记录**漏检线索**:读到的好文里有哪些关键词 A/B 没覆盖 → 补词(如 `redirected walking`、`affective haptics`)。
5. 把 pilot 子集的 ~10–20 篇在 Covidence 试提取,验证字段顺手度。

---

## 4. B 组宽/窄变体(按 pilot precision 切换)

**Broad(当前默认,召回优先):** 保留 `actuat* OR augment* OR modulat* OR stimulat*`。
**Narrow(精确优先,去掉泛词,靠特异术语 + venue 兜):**
```
("electrical muscle stimulation" OR EMS OR "galvanic vestibular" OR GVS OR
 electrotactile OR "electro-tactile" OR "electrical stimulation" OR
 "pseudo-haptic" OR illusion OR "sensory substitution" OR
 "thermal feedback" OR "olfactory display" OR "taste interface" OR
 "perceptual engineering" OR "sensory feedback" OR biofeedback)
```
> 经验:`augment*`/`modulat*` 是噪声主源(UI「augment reality/认知」、信号「modulation」)。先 narrow 提精度,再视召回回补。

---

## 5. 要记录的数(回填本文件)

| 项 | 值 |
|---|---|
| ACM DL n_total | ____ |
| 已读(前20%) | ____ |
| 命中 | ____ |
| precision | ____ % |
| 选用 B 变体 | broad / narrow |
| 补充关键词 | ____ |
| 决定 | 全量上 IEEE+Scopus / 再调 |

*v1 · 2026-06-05 · 数字为估算,待 pilot 实测替换*
