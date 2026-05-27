# Wearable AI Accessibility Scoping Review 会议版研究地图

> 用途：这份文件用于和医学 / 健康领域合作者、HCI / CS 合作者快速对齐项目范围、研究问题、检索关键词、数据提取方向和下一步分工。  
> 项目核心：把健康、康复、神经多样性领域中关于认知、感官、运动、情绪与环境支持的方法，系统映射到 Wearable AI / HCI / UI/UX Accessibility 的设计原则中，最终提出面向 Wearable Intelligence 的新 accessibility principles。

---

## 1. 一句话项目定位

当 AI 从屏幕里的软件进入眼镜、耳机、手表、身体传感器、AR/XR 和日常环境时，accessibility 不再只是“让界面可读、可点击、可理解”，而是要让不同认知、感官、运动和神经特征的人，能够安全、可控、低负担地参与一个由身体、环境、AI 推理和反馈组成的交互循环。

**建议英文核心表述：**

> Wearable intelligence requires a new accessibility paradigm because it makes cognition, perception, bodily action, environmental context, and AI inference part of the interface itself.

---

## 2. 我们到底要做什么

这是一个 **scoping review**，不是临床疗效系统综述，也不是单纯的 HCI guideline paper。

我们要 map 三件事：

1. **医学 / 健康 / 康复 / 神经多样性领域**  
   不同人群有哪些认知、感官、运动、情绪、环境相关 access needs？这些 needs 在临床、康复、教育、occupational therapy、assistive technology 中通常怎么被支持？

2. **CS / HCI / Accessibility / XR / Wearable Computing 领域**  
   这些 needs 在人机交互里已经被怎么翻译成设计方法、系统功能、交互技术或 evaluation criteria？

3. **Wearable AI 新原则**  
   当系统能感知 gaze、motion、physiology、location、context，并用 AI 推断注意力、疲劳、压力、意图或认知状态时，传统 UI/UX accessibility 需要被怎样扩展？

---

## 3. 最终想产出的东西

### 3.1 Access Need Taxonomy

一套跨医学和 HCI 的 access needs 分类，不只按诊断分类，而是按交互障碍分类：

- cognitive needs：attention, memory, executive function, cognitive load, comprehension, task sequencing
- sensory needs：sound sensitivity, light sensitivity, haptic sensitivity, sensory overload, flicker, motion sensitivity
- motor needs：gesture difficulty, fatigue, tremor, posture, reach, balance, repetitive movement burden
- perceptual needs：low vision, blindness, hearing differences, spatial awareness, object recognition
- emotional / social needs：anxiety, uncertainty, overwhelm, stigma, social discomfort, predictability
- environmental needs：noise, lighting, crowding, public space, outdoor context, movement, safety
- AI-mediated needs：privacy, transparency, misclassification, user control, override, autonomy, non-pathologizing inference

### 3.2 Health-to-HCI Translation Map

把医学 / 康复领域的方法翻译成人机交互设计语言。

| 医学 / 健康发现 | 常见支持方式 | HCI / CS 翻译 | Wearable AI 设计原则 |
|---|---|---|---|
| sensory overload | sensory modulation, predictable feedback | adjustable audio / visual / haptic intensity | Sensory Modulation |
| ADHD attention difficulty | external structure, reminders, task chunking | context-aware prompts, interruption control | Attention Respect |
| executive function difficulty | step-by-step guidance, planning aid | cognitive scaffolding, visible task state | Cognitive Legibility |
| autism sensory sensitivity | environmental adjustment, sensory profile | personalized feedback profiles | Sensory Modulation |
| low vision | contrast, magnification, audio support | adaptive overlays, spatial audio, object recognition | Contextual Perceivability |
| hearing differences | captions, visual substitution | directional captions, haptic alerts | Multimodal Substitution |
| motor fatigue | reduced repetition, rest breaks | low-effort gestures, alternative input modes | Body-Capability-Aware Operability |
| anxiety / uncertainty | predictability, control, preparation | transparent AI feedback, preview before action | Adaptive Transparency |
| AI misreads user state | clinical context, human interpretation | correctable inference, user override | Inference Accountability |

### 3.3 CAWI Framework

暂定框架名：

**CAWI: Cognitive Accessibility for Wearable Intelligence**

初步原则：

1. **Contextual Perceivability**  
   信息在真实环境变化中仍然可感知，例如光线、噪音、移动、遮挡、公共空间。

2. **Sensory Modulation**  
   用户可以调节声音、颜色、亮度、震动、动画、频次、强度和反馈通道。

3. **Cognitive Legibility**  
   AI 提示、任务状态、下一步动作和错误恢复路径必须认知上可理解、可承受。

4. **Body-Capability-Aware Operability**  
   交互不能默认用户有稳定的手、眼、颈部、姿态、平衡或长时间动作能力。

5. **Attention Respect**  
   系统不能随意抢占注意力；提示、提醒、警报需要考虑时机、安全、频率和认知负担。

6. **Adaptive Transparency**  
   系统自适应了什么、为什么适应、如何关闭或修改，用户应该知道并能控制。

7. **Inference Accountability**  
   如果 AI 推断用户的注意力、疲劳、压力、情绪、意图或能力，就必须允许误判、纠正、退出，并避免把神经多样性行为病理化。

---

## 4. 推荐研究问题

### RQ1: Health / Neurodiversity Access Needs

健康、康复、神经多样性和 assistive technology 文献中，哪些 cognitive, sensory, motor, perceptual, emotional, environmental access needs 与 wearable intelligence 相关？

### RQ2: Support Strategies

针对这些 needs，医学、康复、教育、occupational therapy、digital health 和 assistive technology 文献提出过哪些 intervention, accommodation, adaptation 或 support strategies？

### RQ3: HCI / CS Translation

HCI, XR, wearable computing, accessible computing 和 human-AI interaction 文献如何把这些 needs 转化为 design principles, interaction techniques, guidelines 或 system features？

### RQ4: New Principles for Wearable AI

当 wearable AI 可以感知环境、身体、gaze、physiology，并推断 cognition / attention / intent 时，UI/UX accessibility 需要新增或改写哪些原则？

---

## 5. PCC 范围定义

### Population / Participants

不要只按 diagnosis 组织最终结果，但检索时可以使用 diagnosis 作为入口。

重点包括：

- autistic people / autism spectrum
- ADHD
- dyslexia
- dyspraxia / developmental coordination disorder
- sensory processing differences
- executive function differences
- cognitive impairment
- anxiety / stress-sensitive users
- low vision / blindness
- hearing differences
- photosensitivity
- vestibular sensitivity / motion sensitivity
- aging users
- motor fatigue
- tremor
- upper-limb limitation
- mobility constraints
- neurodivergent users broadly
- disabled users with cognitive, sensory, motor, perceptual, or wearable access needs

### Concept

核心概念：

**cognitive accessibility and neurodiverse access strategies for wearable intelligence**

子概念：

- cognitive accessibility
- sensory accessibility
- motor accessibility
- perceptual accessibility
- environmental accessibility
- adaptive / AI-mediated accessibility
- ethical accessibility

### Context

重点场景：

- wearable AI / wearable intelligence
- smart glasses / AR glasses
- head-mounted displays
- XR / AR / VR / MR
- wearable sensors
- eye-tracking wearables
- physiological sensing
- context-aware AI
- mobile assistive systems
- digital health systems with embodied or wearable relevance
- assistive technology relevant to everyday interaction

---

## 6. 研究方向地图

### Direction A: Neurodiversity and Sensory Regulation

要问：

- neurodivergent users 在声音、颜色、光线、震动、动画、频次、突发提示上有哪些 sensitivity？
- 哪些调节方式被医学、OT、教育或 assistive technology 使用？
- wearable AI 如何避免 sensory overload？

关键词：

- neurodiversity, neurodivergent, autism, autistic, ADHD
- sensory processing, sensory sensitivity, sensory overload
- sensory modulation, sensory regulation, sensory profile
- sound sensitivity, light sensitivity, tactile sensitivity, haptic sensitivity
- visual clutter, flicker, flashing, motion sensitivity
- assistive technology, digital health, wearable, mobile intervention

### Direction B: Attention, Executive Function, and Cognitive Scaffolding

要问：

- ADHD、autism、cognitive impairment、aging 等人群在 attention, memory, sequencing, planning 上有哪些支持需求？
- reminder、task chunking、step-by-step prompt、external structure 怎么转成 wearable AI 提示？
- AI assistant 的提醒频率和时机如何避免增加 cognitive load？

关键词：

- attention, executive function, working memory, memory support
- cognitive load, mental workload, confusion, comprehension
- task sequencing, task management, planning support
- cognitive scaffolding, prompting, reminders, external structure
- ADHD, autism, cognitive impairment, mild cognitive impairment, aging
- context-aware prompts, adaptive assistance, interruption management

### Direction C: Motor Accessibility and Fatigue

要问：

- wearable / AR / smart glasses 是否默认了过高的 gesture ability？
- 手势、头部动作、眼动、长时间佩戴是否造成 fatigue？
- PT / OT 中的 fatigue management、reduced repetition、alternative movement 怎么翻译成 interaction design？

关键词：

- motor accessibility, motor impairment, motor fatigue
- gesture interaction, gesture fatigue, mid-air gestures
- upper-limb fatigue, reach, tremor, posture, balance
- alternative input, switch access, voice input, gaze input
- wearable interaction, smart glasses, AR interaction
- fatigue management, rest breaks, occupational therapy

### Direction D: Perceptual and Environmental Accessibility

要问：

- 真实环境中的光线、噪音、拥挤、移动和空间复杂度如何影响 wearable AI？
- low vision / blindness / hearing differences 的支持方式如何转成 spatial audio、caption、object recognition、AR overlay？
- 环境感知 AI 是否会制造新的误导或依赖？

关键词：

- low vision, blindness, visual impairment
- deaf, hard of hearing, hearing impairment
- spatial awareness, object recognition, navigation support
- environmental awareness, environmental adaptation
- spatial audio, captions, directional captions, haptic alerts
- outdoor lighting, noise, public space, crowding
- AR overlay, smart glasses, assistive wearable

### Direction E: AI Inference, Personalization, and Ethics

要问：

- wearable AI 如何推断 attention、fatigue、stress、intent、cognitive load？
- gaze、heart rate、skin conductance、EEG、pupil dilation 等信号是否可靠？
- 如果 AI 误判 neurodivergent 行为，会不会造成 stigma、loss of autonomy 或 harmful adaptation？

关键词：

- human-AI interaction, AI accessibility, adaptive AI
- cognitive state inference, attention inference, intent recognition
- physiological sensing, biosignals, heart rate, skin conductance
- eye tracking, gaze tracking, pupil dilation
- personalization, adaptive interface, context-aware AI
- explainability, transparency, user control, override
- privacy, consent, fairness, misclassification, autonomy
- non-pathologizing design, disability justice, neurodiversity

### Direction F: Existing Accessibility Principles and Their Limits

要问：

- WCAG / mobile accessibility / inclusive design 已经提供了哪些原则？
- 哪些原则可以继承，哪些必须转化？
- screen-based accessibility 到 wearable intelligence 的核心断裂在哪里？

关键词：

- web accessibility, WCAG, mobile accessibility
- cognitive accessibility, digital accessibility
- inclusive design, universal design, accessible computing
- XR accessibility, AR accessibility, VR accessibility
- accessibility guideline, framework, taxonomy, design principle
- wearable accessibility, embodied interaction, human-centered AI

---

## 7. 检索策略：建议分层搜索

不要一开始用一个超长 search string。建议按层检索，每层负责一个文献区域。

### Layer 1: Health / Neurodiversity / Support Needs

```text
(neurodiversity OR neurodivergent OR autism OR autistic OR ADHD OR dyslexia OR dyspraxia OR "developmental coordination disorder" OR "cognitive impairment" OR "sensory processing" OR "sensory sensitivity" OR "executive function")
AND
(accessibility OR accommodation OR intervention OR support OR "assistive technology" OR "self-regulation" OR "sensory modulation" OR "cognitive support" OR "attention support")
AND
(wearable OR "mobile health" OR mHealth OR "digital health" OR "assistive device" OR "smart glasses" OR "augmented reality" OR "virtual reality" OR "extended reality")
```

### Layer 2: Sensory Modulation / Sound / Color / Frequency

```text
("sensory overload" OR "sensory modulation" OR "sensory processing" OR "sensory sensitivity" OR "sensory regulation")
AND
(autism OR autistic OR neurodivergent OR ADHD OR anxiety)
AND
(sound OR audio OR color OR light OR brightness OR haptic OR vibration OR flicker OR flashing OR frequency OR intensity)
AND
("assistive technology" OR digital OR wearable OR mobile OR "augmented reality" OR "virtual reality")
```

### Layer 3: Wearable / Gaze / Physiological Sensing

```text
("wearable technology" OR wearable OR "smart glasses" OR "AR glasses" OR "head-mounted display" OR "body-worn sensor" OR "eye tracking" OR gaze OR "physiological sensing" OR "context-aware")
AND
("cognitive load" OR attention OR confusion OR fatigue OR overload OR "mental workload" OR "sensory overload" OR "executive function")
AND
(accessibility OR neurodiversity OR disability OR "assistive technology" OR adaptation OR personalization)
```

### Layer 4: HCI / XR / Accessibility Principles

```text
(accessibility OR "accessible computing" OR "inclusive design" OR "universal design" OR "cognitive accessibility")
AND
("human-computer interaction" OR HCI OR "augmented reality" OR "virtual reality" OR XR OR "wearable interaction" OR "human-AI interaction")
AND
(guideline OR framework OR principle OR taxonomy OR "design implication" OR "design recommendation")
```

### Layer 5: AI Accessibility / Human-AI Interaction

```text
("artificial intelligence" OR AI OR "machine learning" OR "adaptive system" OR "context-aware AI" OR "generative AI" OR "human-AI interaction")
AND
(accessibility OR disability OR neurodiversity OR "cognitive accessibility")
AND
(explainability OR transparency OR fairness OR personalization OR autonomy OR "user control" OR privacy OR misclassification)
```

---

## 8. 数据库建议

### Health / Medicine / Rehabilitation

- PubMed / MEDLINE
- PsycINFO
- CINAHL
- Embase
- Scopus
- Web of Science

### HCI / CS / Engineering

- ACM Digital Library
- IEEE Xplore
- SpringerLink
- ScienceDirect
- JMIR

### Standards / Grey Literature

用于建立背景，不作为主要证据来源：

- W3C WCAG
- W3C XR Accessibility User Requirements
- WHO assistive technology resources
- Apple / Microsoft / Google accessibility and inclusive design guidance
- NICE / NHS / CDC resources when relevant

---

## 9. Inclusion / Exclusion Criteria

### Include

纳入文献需要至少满足一个 access need 条件和一个 context 条件。

Access need 条件：

- cognitive accessibility
- sensory accessibility
- motor accessibility
- perceptual accessibility
- neurodiversity
- assistive technology
- health-based support strategy
- rehabilitation / occupational therapy strategy
- cognitive scaffolding
- sensory modulation
- accessibility design principle
- XR / wearable accessibility
- AI-mediated accessibility

Context 条件：

- wearable systems
- smart glasses / AR / VR / XR
- mobile or embodied support
- assistive technology
- digital health
- HCI accessibility
- human-AI interaction
- context-aware systems
- gaze / eye tracking
- physiological sensing
- body-based interaction

### Exclude

排除：

- 只讲医学诊断、没有 support / accessibility / technology implication 的文献
- 只讲算法性能、没有 human access / disability / design implication 的文献
- 只讲 general AI ethics、没有 disability / accessibility relevance 的文献
- 只讲 general web accessibility、没有 cognitive / neurodiverse / wearable / XR / AI relevance 的文献
- 只讲 VR sickness、但不涉及 access needs、sensory sensitivity 或 design principle 的文献
- 无全文、重复、非人类研究、纯观点且无框架的文章

---

## 10. 数据提取表应该记录什么

### Bibliographic Metadata

- Paper_ID
- Title
- Authors
- Year
- Venue_Journal
- DOI_URL
- Database
- Search_Layer
- Paper_Type
- Field
- Study_Method
- Sample_Size
- Participant_Group
- Technology_Context

### Access Need Codes

- Cognitive_Need
- Sensory_Need
- Motor_Need
- Perceptual_Need
- Emotional_Need
- Environmental_Need
- AI_Specific_Need
- User_Group
- Access_Barrier

### Support Strategy Codes

- Sensory_Modulation
- Multimodal_Substitution
- Cognitive_Scaffolding
- Attention_Management
- Motor_Accommodation
- Personalization
- Context_Adaptation
- Human_In_The_Loop
- Explainability_Control
- Safety_Strategy

### HCI Translation Codes

- HCI_Principle
- Interaction_Modality
- Wearable_Relevance
- XR_Relevance
- AI_Relevance
- Everyday_Context_Relevance
- Design_Implication
- Evaluation_Method
- Evidence_Strength
- Limitation

### CAWI Mapping Codes

- Loop_Component
- CAWI_Principle
- Health_Finding
- HCI_Translation
- Wearable_Intelligence_Implication
- Quote_or_Evidence
- Notes

---

## 11. 今天和医学生讨论时最重要的问题

### 11.1 关于医学 / 健康范围

1. 哪些 diagnosis / user groups 最适合作为检索入口？  
   例如 autism, ADHD, dyslexia, cognitive impairment, anxiety, sensory processing differences, low vision, hearing differences, vestibular sensitivity。

2. 哪些健康领域术语比 HCI 术语更标准？  
   例如 sensory modulation, self-regulation, occupational therapy, executive function, cognitive rehabilitation。

3. “声音、颜色、频率、频次、震动、光线”等调节，在医学文献里通常属于哪些概念？  
   可能是 sensory modulation, environmental adaptation, sensory regulation, stimulus control, sensory diet。

4. 哪些 clinical / rehab support strategies 可以被翻译成 wearable AI design features？

5. 有没有需要避免的病理化语言？  
   例如不要把 neurodivergent behavior 直接描述成 deficit，而要描述为 access needs, support needs, sensory/cognitive differences。

### 11.2 关于 HCI / CS 范围

1. 我们是否把 XR / smart glasses 纳入 wearable intelligence 的主要邻近领域？

2. AI 部分是否聚焦在 personalization, adaptation, inference, explainability, user control，而不是泛泛讨论 AI ethics？

3. 最终 principle 是要像 WCAG 那样抽象，还是更像 HCI design implications 那样具体？

4. 哪些 wearable interaction modalities 必须覆盖？  
   建议至少包括 gaze, voice, gesture, haptic, audio, visual overlay, physiological sensing。

5. evaluation 要不要单独作为一个结果维度？  
   例如 lab study, field study, participatory design, clinical trial, usability study, qualitative interview。

---

## 12. 推荐会议议程

### 0-10 min: 项目共同目标

- 这不是单纯做 neurodiversity review。
- 也不是单纯做 wearable device review。
- 目标是把医学支持策略翻译成 Wearable AI accessibility principles。

### 10-25 min: 医学范围确认

- 哪些人群纳入？
- 哪些病症 / 状态作为 search terms？
- 哪些支持方法是医学上合理的？
- 哪些术语要避免？

### 25-40 min: HCI / CS 范围确认

- wearable intelligence 的边界是什么？
- smart glasses, XR, mobile assistive tech 是否都纳入？
- AI inference / personalization / adaptive systems 的边界是什么？

### 40-55 min: Search Strategy

- 确认数据库。
- 确认 5 个 search layers。
- 每层先做 pilot search，避免过宽或过窄。

### 55-70 min: Data Extraction and Division of Labor

- 医学生负责 health / clinical / rehab coding 的定义。
- HCI 研究者负责 interaction modality / design implication / wearable relevance。
- 两边共同决定 CAWI principle mapping。

---

## 13. 建议分工

| 任务 | 医学 / 健康合作者 | HCI / CS 合作者 | 共同决定 |
|---|---|---|---|
| Population terms | 主负责 | 辅助 | 最终纳入人群 |
| Health support strategies | 主负责 | 翻译到设计 | taxonomy |
| HCI / wearable terms | 辅助 | 主负责 | wearable intelligence 边界 |
| Screening criteria | 共同 | 共同 | include / exclude rules |
| Data extraction codebook | health codes | HCI / AI codes | CAWI mapping |
| Final principles | medical grounding | design formulation | CAWI framework |

---

## 14. 初步 manuscript 结构

1. Introduction  
   说明 AI 从 screen-based interaction 进入 wearable / embodied / context-aware interaction，导致 accessibility 范式变化。

2. Background  
   分三块：digital accessibility, health / neurodiversity support, wearable intelligence。

3. Methods  
   PRISMA-ScR, JBI PCC, databases, search strategy, inclusion / exclusion, screening, data extraction, synthesis。

4. Results I: Access Needs  
   cognitive, sensory, motor, perceptual, emotional, environmental, AI-mediated needs。

5. Results II: Support Strategies  
   sensory modulation, cognitive scaffolding, attention support, motor accommodation, environmental adaptation, multimodal substitution, personalization。

6. Results III: HCI Translation  
   已有 HCI / XR / wearable / AI accessibility 如何处理这些 needs。

7. Discussion  
   哪些 accessibility principles 可以继承，哪些必须转化，哪些需要新增。

8. CAWI Framework  
   提出 7 个 wearable intelligence accessibility principles。

9. Limitations  
   文献语言、学科偏差、AI 快速发展、clinical categories 与 lived experience 的差距等。

10. Conclusion  
   强调未来 accessibility 要处理 embodied, adaptive, gaze-aware, inference-mediated human-AI loops。

---

## 15. 立即下一步

1. 今天会议确认 scope：人群、健康术语、HCI 边界、AI 边界。
2. 把这份 brief 转成 3-5 页 protocol。
3. 建立 Zotero / Rayyan / spreadsheet workflow。
4. 用 5 个 search layers 做 pilot search。
5. 每层先抽 20-50 篇，看结果是否太宽或太窄。
6. 建立 seed bibliography。
7. 修订 inclusion / exclusion criteria。
8. 建立 data extraction template。
9. 开始 title / abstract screening。
10. 根据前 100-300 篇结果修订 CAWI 初版 taxonomy。

---

## 16. 今天可以直接说给合作者听的版本

我们想做的不是单纯总结“有哪些 wearable accessibility 研究”，而是做一个跨医学和 HCI 的 scoping review。医学这边会提供关于 neurodiversity、sensory processing、executive function、motor fatigue、anxiety、low vision、hearing differences 等方面的 access needs 和 support strategies；HCI 这边会把这些策略翻译成 wearable AI 可以实现或必须遵守的 design principles。最终我们希望提出一个新的 accessibility framework，用来指导 smart glasses、wearable sensors、AR/XR、context-aware AI assistant 等系统，尤其关注声音、颜色、频率、震动、提示时机、认知负担、身体疲劳、AI 误判、用户控制和非病理化设计。

---

## 17. 本项目的判断标准

一篇文献越符合下面条件，越可能是核心文献：

- 它不是只讲 diagnosis，而是讲 support / accommodation / intervention / accessibility。
- 它能说明某类 user need 如何影响 interaction。
- 它能提供 sound, color, light, haptic, frequency, prompt, attention, fatigue, environment 等具体调节策略。
- 它能被翻译到 wearable, XR, smart glasses, physiological sensing, context-aware AI 或 human-AI interaction。
- 它能帮助我们提出新的 accessibility principle，而不只是重复已有 WCAG 原则。

