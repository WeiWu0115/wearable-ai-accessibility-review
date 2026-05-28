# Medical Coauthor Interview Coding Memo

Date: 2026-05-28  
Source files: `Shaw.m4a`, `Shaw2.m4a`, `Shaw3.m4a`  
Transcript: `combined_raw_transcript.md`

> Publication note: This memo is shared as project working material for collaborator review. The transcript is automatic and should not be treated as polished quotation data.

---

## 1. Bottom Line

The conversation is very helpful for the current scoping review plan.

The most useful contribution is not a list of diagnoses. It is a medical scaffold for thinking about wearable AI accessibility as an intervention into a sensory pathway:

**stimulus -> receptor -> signal/transduction -> neural pathway -> processing -> interpretation/action -> support/treatment**

This gives the review a stronger health-side grounding than simply saying "neurodivergent users may have sensory overload." It helps define what wearable AI may be doing:

- sensing external stimuli for the user;
- modifying stimulus intensity or channel;
- supporting perception when thresholds differ;
- reducing overload when thresholds are low;
- compensating when signals are missed;
- helping diagnosis/assessment by making access barriers observable;
- supporting treatment/accommodation by adjusting context or feedback.

The conversation supports revising the project from:

> wearable AI accessibility for neurodiversity

to a more precise formulation:

> wearable AI accessibility as context-aware support for heterogeneous sensory thresholds, receptor/pathway differences, perceptual processing, and downstream cognitive/action consequences.

---

## 2. High-Level Codes

| Code | What It Means | Evidence From Conversation | Usefulness for Review |
|---|---|---|---|
| C1. Medical framing: physiology vs pathology | First understand normal sensory function, then pathological or atypical cases. | Coauthor distinguishes normal physiology, pathology, diagnosis, and treatment. | Helps structure background and inclusion criteria. |
| C2. Sensory pathway as system architecture | Sensory access can be understood as receptor, transmission, processing, and output. | Repeated analogy between neural pathway and computer/signal processing. | Directly strengthens CAWI loop. |
| C3. Diagnosis as debugging | Clinical diagnosis identifies where the pathway/problem occurs. | "diagnose" compared to finding bugs; treatment compared to fixing/debugging. | Useful metaphor for mapping medical reasoning to HCI evaluation. |
| C4. Receptor as key concept | "Sensory" is too broad; medical framing needs receptor / sensory receptor / pathway. | Clarifies receptor is not simply eye/nose/mouth but functionally signal-receiving cells/structures. | Add keywords and coding fields. |
| C5. Threshold and sensitivity | Different people have different thresholds and sensitivities. | Discussion of threshold, action potential, sensitivity, lower/higher thresholds. | Strong support for personalization and sensory profiles. |
| C6. No one-size-fits-all | Protocol/guideline cannot become complete DIY for every body. | Coauthor explicitly rejects "one solution for all." | Helps frame principles as adaptable, not universal fixed values. |
| C7. Modality-specific pathways | Olfactory, auditory, visual, tactile/cold/pain/vibration pathways differ. | Examples of olfactory receptor neurons, hair cells, photoreceptors, skin receptors. | Search strategy should include modality-specific terms. |
| C8. Somatosensory expansion | Touch, cold/thermal, pain, vibration, texture, proprioception/deep sensation matter. | Shaw3 discusses skin receptors and spinal pathways. | Current plan under-specifies somatosensory access. |
| C9. Action/reflex boundary | Some pathways lead to perception only; others involve reflex/action/effector. | Distinction between smelling and reflex withdrawal. | Helps define current scope and future work boundary. |
| C10. Wearable AI as support/intervention | Wearable AI can help sense, diagnose, or treat/support. | Coauthor describes wearable AI as helping diagnose/treat or adjust what body cannot regulate. | Helps justify health-to-HCI translation. |
| C11. Dynamic regulation | Human systems adapt; overload and sensitivity are dynamic, not static labels. | Discussion of fatigue, arousal, stimulation, adaptation, autism/fridge sound example. | Supports context-aware adaptation and longitudinal personalization. |
| C12. Term ambiguity | Medical terms may differ by history and discipline. | Hair cells can function as receptors but are named differently. | Search must include both function terms and anatomical terms. |

---

## 3. What This Adds to the Existing Plan

### 3.1 It Strengthens the Conceptual Scaffold

Current CAWI loop:

`Environment -> Perception -> Cognition -> Action -> Feedback -> Adaptation -> Inference`

Medical coauthor suggests a more biologically grounded layer underneath:

`Stimulus -> Receptor -> Signal/transduction -> Pathway -> Processing -> Interpretation/action`

Recommended synthesis:

| CAWI Component | Medical Scaffold | Design Question |
|---|---|---|
| Environment | Stimulus source | What sensory stimulus is present: light, sound, vibration, cold, texture, motion, smell? |
| Perception | Receptor / sensory threshold | Can the user detect it, tolerate it, or are they overloaded by it? |
| Cognition | Processing / interpretation | Does the signal become meaningful, confusing, fatiguing, or misclassified? |
| Action | Effector / reflex / motor response | Does the system require bodily action, or does it trigger stress/reflex/fatigue? |
| Feedback | Artificial stimulus | Is the wearable adding sound, light, haptic, visual overlay, or other stimulation? |
| Adaptation | External regulation | Is the system helping tune what the body cannot regulate alone? |
| Inference | Diagnosis/debugging logic | Where does the system infer the problem is, and can that inference be wrong? |

### 3.2 It Clarifies the Scope Boundary

The review should not claim to cover the entire neural pathway or all treatment.

Better scope:

> This review focuses on wearable AI as an accessibility layer around sensory reception, stimulus modulation, and user-facing support. Full neural pathway modeling, central processing, reflex arcs, and clinical diagnosis/treatment mechanisms are acknowledged as adjacent or future work unless directly connected to HCI, assistive technology, or wearable design.

This is useful because the coauthor repeatedly notes that a full pathway includes more than sensing: receptor, central processing, effector/action, and diagnosis/treatment.

### 3.3 It Adds a Medical-to-HCI Translation Logic

The strongest translation logic from the meeting:

| Medical Concept | HCI / Wearable AI Translation |
|---|---|
| receptor | sensor/input point or human sensory entry point |
| threshold | minimum/maximum comfortable stimulus level |
| sensitivity | individual response curve to stimulus intensity |
| action potential | threshold-triggered response, useful as an analogy for state changes |
| fatigue/adaptation | cumulative stimulation can change response over time |
| sensory overload | signal/stimulus exceeds tolerance or processing capacity |
| missed signal / low registration | user does not detect or register stimulus |
| pathway component | possible site where support or failure occurs |
| diagnosis | locating where the access breakdown happens |
| treatment | intervention, support, accommodation, or regulation |

---

## 4. Recommended Changes to Current Search Strategy

### Add or Strengthen Keywords

#### Core Medical / Physiology Terms

- sensory receptor
- receptor
- sensory pathway
- neural pathway
- afferent pathway
- sensory transduction
- sensory threshold
- stimulus threshold
- sensory responsiveness
- sensory sensitivity
- sensory adaptation
- habituation
- sensory gating
- signal processing

#### Modality-Specific Terms

- olfactory receptor neuron
- olfactory pathway
- hair cell
- mechanoreceptor
- auditory pathway
- photoreceptor
- visual pathway
- somatosensory
- tactile perception
- thermoreceptor
- cold receptor
- nociception
- pain perception
- vibration perception
- proprioception
- vestibular sensitivity

#### Wearable/HCI Translation Terms

- adjustable feedback intensity
- sensory profile
- low stimulation mode
- stimulus intensity
- visual density
- visual crowding
- haptic intensity
- notification frequency
- multimodal feedback
- context-aware adaptation

### Add a New Search Layer

**Layer 0 or Layer 1A: Sensory Physiology and Receptor/Pathway Foundations**

Purpose: capture foundational medical literature that explains sensory thresholds, receptors, sensory pathways, and modality-specific sensory mechanisms.

Draft query:

```text
("sensory receptor" OR receptor OR "sensory pathway" OR "neural pathway" OR "sensory transduction" OR "sensory threshold" OR "stimulus threshold" OR "sensory responsiveness" OR "sensory adaptation" OR habituation OR "sensory gating")
AND
("sensory sensitivity" OR "sensory overload" OR neurodivergent OR autism OR ADHD OR "sensory processing")
AND
(vision OR auditory OR olfactory OR tactile OR somatosensory OR vestibular OR pain OR vibration OR proprioception)
```

This layer should be used selectively. It can easily become too broad, so it should be piloted and probably used for conceptual grounding rather than full exhaustive inclusion.

---

## 5. Recommended Changes to Data Extraction / Coding

Add these fields to the extraction template:

| New Field | Description |
|---|---|
| Sensory_Modality | visual, auditory, olfactory, tactile, thermal, pain, vibration, proprioceptive, vestibular, multimodal |
| Stimulus_Type | light, flicker, sound, vibration, pressure, temperature, texture, smell, movement, spatial clutter |
| Human_Pathway_Component | receptor, transduction, pathway/transmission, central processing, interpretation, effector/action |
| Threshold_Type | low threshold, high threshold, variable threshold, unknown |
| Response_Profile | overload, avoidance, seeking, low registration, fatigue, adaptation, habituation, arousal |
| Support_Target | reduce stimulus, amplify stimulus, substitute modality, filter signal, scaffold attention, support action, support diagnosis |
| HCI_Adjustable_Parameter | intensity, frequency, timing, density, modality, predictability, duration, location/context |
| Evidence_Role | conceptual foundation, health support evidence, HCI design evidence, wearable system evidence |

---

## 6. Implications for CAWI Principles

### Contextual Perceivability

Strengthened by the idea that perception depends on stimulus pathway and context. Real-world light, noise, tactile input, and environmental density are not neutral; they change how signals are received and processed.

### Sensory Modulation

Strongly supported. The coauthor repeatedly confirms that thresholds and sensitivities differ across people and modalities. Design should support adjustable intensity, frequency, channel, and density.

### Cognitive Legibility

Supported indirectly. If perception is not simply stimulus detection but includes processing and interpretation, then wearable AI should make feedback cognitively interpretable, not merely perceivable.

### Body-Capability-Aware Operability

Strengthened by the effector/reflex/action discussion. Some access issues involve not only sensing but also action response, fatigue, and motor output.

### Attention Respect

Still important, but the interview suggests reframing it as attention/arousal/state-dependent modulation. Prompt timing should consider user state and cumulative stimulation.

### Adaptive Transparency

Strengthened by the "not DIY / no one-size-fits-all" point. Adaptation must be adjustable and explicit because the system cannot assume a universal threshold.

### Inference Accountability

Strengthened by the diagnosis/debugging analogy. If wearable AI tries to infer where the user's access breakdown is, the inference must be contestable because diagnosis itself is uncertain and sometimes approximate.

---

## 7. What Is Helpful vs. Not Helpful

### Directly Helpful

- Sensory pathway / receptor framing.
- Threshold and sensitivity language.
- Physiological vs pathological distinction.
- Diagnosis as locating failure point.
- Treatment as support/intervention.
- Modality-specific models: olfactory, auditory, visual, tactile/somatosensory.
- Dynamic regulation: sensitivity, fatigue, adaptation, overload.
- Strong caution against one-size-fits-all design.

### Helpful as Future Work / Boundary

- Full reflex arc modeling.
- Effector/action pathways.
- Central processing and whether the brain correctly interprets signals.
- Taste pathway as underdeveloped or uncertain.
- Molecular/pathway-level biomedical mechanisms.

### Risky or Needs Verification

- Some medical examples are informal and should not be quoted directly.
- Some terms in the Whisper transcript are misrecognized.
- Do not cite the conversation as evidence in the paper unless coauthor agrees.
- Use this as conceptual feedback and search-term generation, then cite published medical literature.

---

## 8. Action Items for the Project

1. Add a private note that the medical scaffold is:
   `stimulus -> receptor -> pathway -> processing -> interpretation/action -> support`.

2. Revise the search protocol to include:
   - receptor;
   - sensory threshold;
   - sensory pathway;
   - sensory transduction;
   - sensory adaptation / habituation;
   - somatosensory, thermoreceptor, nociception, vibration, proprioception.

3. Add data extraction fields for:
   - modality;
   - pathway component;
   - threshold type;
   - response profile;
   - HCI adjustable parameter.

4. Reframe review contribution:
   from "neurodiversity and wearable AI accessibility"
   to "health-grounded sensory/cognitive accessibility for wearable AI, based on heterogeneous thresholds and context-dependent sensory pathways."

5. Keep the current CAWI framework, but add an underlying "sensory pathway scaffold" in the methods/synthesis memo.

6. Ask coauthor for formal references on:
   - sensory receptors;
   - sensory thresholds;
   - sensory transduction;
   - sensory adaptation / habituation;
   - sensory processing in autism and ADHD;
   - somatosensory pathways;
   - photosensitive epilepsy / flicker sensitivity;
   - sensory over-responsivity / under-responsivity.

---

## 9. Suggested Next Version Name

If this feedback is incorporated into the public project later:

`v0.3-medical-pathway-scaffold-2026-05-28`

Do not publish the raw transcript unless explicitly approved.

