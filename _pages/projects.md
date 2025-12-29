---
layout: page
title: Research
permalink: /projects/
description: 
nav: true
nav_order: 3
display_categories: [Deep RL, Robotic Surgery]
horizontal: false
---
### Research Vision

Most artificial intelligence systems are designed and evaluated under static assumptions: fixed data distributions, stable environments, and well-specified objectives. In real-world deployment, these assumptions rarely hold. Environments change, objectives are ambiguous, and constraints emerge only after systems are in use. In high-stakes settings, such failures are not merely inconvenient—they can lead to unsafe or irreversible outcomes.

My research centers on **adaptive intelligence**: the ability of learning systems to maintain meaningful, reliable behavior when environments, objectives, or constraints change. I study adaptation as a systems-level property rather than a training-time performance metric, with an emphasis on principled reinforcement learning grounded in real-world failure modes, often informed by close interaction with domain experts and collaborators.

---

### Research Themes

#### 1. Learning and Generalization Under Change

Reinforcement learning provides a natural framework for adaptive decision-making, but standard RL methods often fail to generalize when assumptions about stationarity, reward fidelity, or representation break. A central theme of my work is understanding **why generalization collapses under non-stationarity**, even when policies perform well during training.

I study structural causes of failure in learning systems, including instability in representations, sensitivity of optimization dynamics, and reward drift under environmental change. My work develops principled methods that improve stability and transfer by treating generalization as a property of the learning problem itself, rather than as a consequence of policy capacity or data scale.

This line of research contributes algorithmic insights and diagnostic tools for reinforcement learning systems deployed beyond controlled benchmarks.

---

#### 2. Semantic Representations and Reward as Inferred Intent

In many real-world settings, objectives are inherently underspecified. Reward functions act as proxies for intent, but these proxies often degrade as context evolves. My research treats **reward and representation as interfaces that must remain meaningful under change**, rather than as fixed ground truth.

I explore semantic state representations—including language and vision-language abstractions—that preserve task-relevant meaning across environments while abstracting away low-level variability. In parallel, I study reward modeling as a problem of **intent inference**, where systems must reason about goals and constraints rather than optimize brittle scalar signals.

This perspective reframes reward design as a central object of study and provides a foundation for more reliable adaptation in dynamic, high-stakes environments.

---

#### 3. Reasoning Under Ambiguity and Limited Data

In high-stakes domains such as healthcare, learning systems must operate under limited data, partial observability, and ambiguous supervision. In these settings, unconstrained optimization is often unacceptable.

My work integrates structured reasoning with learning to constrain adaptation under uncertainty. I develop systems that generate and verify hypotheses, incorporate domain constraints, and provide interpretable decision processes. These approaches allow learning systems to act reliably even when feedback is sparse or objectives are ill-defined.

In medical decision-making applications, this integration of reasoning and perception has enabled accurate, interpretable systems validated in real clinical contexts.

---

#### 4. Embodied Adaptive Systems as a Reality Check

Simulation and benchmark environments often hide the consequences of broken assumptions. Embodied systems do not. Physical interaction introduces non-stationary dynamics, sensing noise, delays, and irreversible outcomes that expose brittle learning assumptions immediately.

My research in embodied robotics—particularly in shared autonomy and teleoperation—uses physical deployment as a **truth test** for adaptive intelligence. I develop semantic action abstractions, delay-tolerant control frameworks, and real-world datasets to evaluate which learning and reasoning methods survive deployment.

This work grounds theoretical and algorithmic insights in reality and feeds back into the design of more robust adaptive systems.

---

### Integration and Future Directions

Together, these research directions form a unified program that integrates learning, reasoning, and embodiment to study adaptive intelligence in high-stakes environments. This work naturally benefits from interdisciplinary interaction, and I am interested in continuing to engage with collaborators across machine learning, robotics, and applied domains where real-world constraints shape intelligent behavior.
