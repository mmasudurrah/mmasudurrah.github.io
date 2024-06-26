---
layout: page
title: Teleoperated Robotic Surgery
description: Semi-autonomous Telesurgery.
img: assets/img/forward_framework.png
importance: 1
category: Robotic Surgery
related_publications: true
---

I have developed a semi-autonomous teleoperated robotic surgery system {% cite rahman2021sartres %}, {% cite gonzalez2021deserts %}  that can operate with up to 5 seconds of delay with high efficiency (Figure 2). A key challenge was the scarcity of diverse training data for learning algorithms {% cite rahman2021sequential %}. To address this, I created the DESK (Dexterous Surgical Skills) dataset {% cite madapana2019desk %}, {% cite gonzalez2021dexterous %}, which collects robotic surgical skills from various platforms. This dataset facilitates knowledge transfer across different domains, particularly where data is scarce. 


<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/forward_framework.png" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>


My approach enables surgeons to execute procedures remotely by translating their high-level commands into robotic actions. The system breaks down complex surgeries into smaller automated segments, known as “surgemes”, improving operation efficiency even with limited data availability. It has achieved an 87% success rate in peg transfer tasks, outperforming standard teleoperation even with substantial communication delays of 5 seconds, compared to standard teleoperation systems, which can fail with delays as short as 300 millisecond. However, these systems must operate reliably in unpredictable conditions, such as disaster zones, where they may encounter novel scenarios. 
{% raw %}


{% endraw %}
