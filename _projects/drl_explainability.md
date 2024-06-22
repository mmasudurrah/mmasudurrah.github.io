---
layout: page
title: Vision-Language Model in Deep RL
description: Improving Explainability in Deep Reinforcement Learning
img: assets/img/language_state.png
importance: 1
category: DeepRL
related_publications: true
---

I focus on decision-making derived from language descriptions of visuals (e.g., images). The method is to first compress the visual information (i.e., pixels) into natural language and use this language as state information to learn policy with reinforcement learning {% cite rahman2024natural %}. This approach has several advantages. For instance, the language representation is inherently interpretable, providing a more accurate indication of what the agent understands from the visual scene. In this setup, the agent can learn from a natural language description of the image. This approach provides multiple benefits. Primarily, the representation is easily interpretable by humans, unlike raw pixel data from the image. Moreover, it paves the way for harnessing the immense processing power of large language models (LLMs) to handle natural language state information. For instance, unnecessary features, such as color information, can be filtered out by directing the LLM to ignore them (e.g., prompt: rewrite the description excluding color information).


<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/language_state.png" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

The results indicated that policies trained using natural language descriptions of images exhibited superior generalization compared to those trained directly from images. Moreover, our language-based state representation is inherently interpretable compared to directly learning from pixels, indicating a strong use case for language-based state representation.

{% raw %}


{% endraw %}
