---
layout: page
title: Robust Policy Optimization (RPO)
description: Improving Sample Efficiency in Deep Reinforcement Learning
img: assets/img/rpo_overview.png
importance: 1
category: Deep RL
related_publications: false
---

For sample efficiency, I develop a novel approach to policy gradient-based reinforcement learning with continuous action spaces. Traditional policy gradient methods, while stable and effective, often suffer from reduced exploration due to collapsed entropy, leading to sub-optimal policy learning. Furthermore, deep RL exhibits a primacy bias, where agents overly rely on earlier interactions and neglect later ones. 


<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/rpo_overview.png" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

To address these challenges, our Robust Policy Optimization (RPO) method injects a state-independent variance into the policy's actions, enhancing policy entropy and maintaining stochasticity throughout training. This is achieved by adding a random perturbation to the mean action value, resulting in a Perturbed Gaussian distribution that encourages exploration. Theoretical analysis confirms that this perturbation maintains unbiased gradient estimation in the policy gradient framework. Empirical evaluations across various environments demonstrate RPO's superior performance over baseline Proximal Policy Optimization (PPO). Furthermore, RPO outperforms methods utilizing entropy regularization and data augmentation, highlighting its effectiveness in fostering exploration and improving overall performance.

{% raw %}


{% endraw %}
