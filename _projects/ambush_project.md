---
layout: page
title: Surgical Decision-Making in Burn Diagnosis
description: Burn Depth Prediction.
img: assets/img/ambush_overview.png
importance: 1
category: Robotic Surgery
related_publications: false
---

Accurate assessment of burn depth is crucial for determining appropriate treatment and predicting the likelihood of pathological scarring. Traditional methods often rely on subjective judgments and invasive procedures, necessitating more reliable, objective, and non-invasive approaches. Accurately prioritizing which burn wounds require surgical intervention is vital but challenging. This difficulty arises primarily from the complexity of assessing burn depth based solely on visual information, a task that challenges even experienced burn surgeons. The assessment of burn depth is a critical factor in predicting pathological scarring, a common consequence of burn injuries, and remains an unresolved clinical issue.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/ambush_overview.png" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
This study aims to address the challenge of accurately assessing burn depth in clinical settings, which is crucial for effective treatment planning and the prediction of pathological scarring. It introduces and evaluates an AI framework (Figure 1) based on a vision-language model (GPT-4) for the explainable zero-shot prediction of burn depth using multimodal harmonic ultrasound imaging, offering a more reliable, objective, and non-invasive alternative to traditional methods. A  comprehensive evaluation of the proposed AI framework is presented, comparing its performance in predicting burn depth against traditional assessment methods. The study utilized a diverse dataset of ultrasound images from clinical settings, featuring various types of burn injuries. The proposed AI model takes input from TDI ultrasound images and predicts the necessity of surgery based on the depth of the burn wound.

This study included 30 patients, where the main outcomes measured were the accuracy, reliability, and explainability of the vision-language model in predicting the necessity of surgical intervention for burn wounds. The proposed AI method achieves superior performance compared to traditional methods, with a high accuracy rate of 95% in predicting the need for surgical intervention in burn cases. 

In contrast, the traditional method of predicting burn depth from visual RGB burn images has an accuracy of 70-80% for burn experts (60% for non-experts). Thus, the proposed method achieves super-human performance, demonstrating the importance of TDI imaging for burn prediction with the proposed AI framework. Its explainability feature additionally enhances its clinical utility, allowing practitioners to understand the rationale behind each prediction.

The proposed method represents a significant advancement in the non-invasive, accurate, and explainable assessment of burn depth. By integrating artificial intelligence into clinical settings, the model offers a promising tool for improving treatment strategies and patient outcomes, marking a substantial improvement over existing assessment techniques.

{% raw %}


{% endraw %}
