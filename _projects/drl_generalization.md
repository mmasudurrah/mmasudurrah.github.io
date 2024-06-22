---
layout: page
title: Generalization in Deep RL
description: Improving Generalization in Deep Reinforcement Learning
img: assets/img/thinker_overview.png
importance: 1
category: DeepRL
related_publications: true
---

I address the issue of distribution shift in the deployed environment by developing policy optimization algorithms that improve the generalization capabilities of the agent. I employ style transfer-based techniques based on generative modeling to increase the diversity of observations in a trajectory, thus enhancing the generalization ability of the learned policy {% cite rahman2022bootstrap %}. 


<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/thinker_overview.png" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

My approach focuses on altering the visual style of observations while preserving their essential meaning. Consequently, the adapted trajectories resemble those that might be encountered in test environments, better preparing the agent for new situations. The human capacity for counterfactual reasoning inspires the design of my method—asking, "What if the background color of the image observation was red instead of blue?" This augmented, diverse data is then utilized for policy training. Experimental results show that my method achieves superior generalization capability on the standard generalization benchmark, outperforming baseline algorithms and several data augmentation techniques. 

{% raw %}


{% endraw %}
