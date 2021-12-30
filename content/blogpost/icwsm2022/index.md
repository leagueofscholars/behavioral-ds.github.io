---
title: "Slipping to the Extreme: A Mixed-Method to Explain How Extreme Opinions Infiltrate Online Discussions"
authors:
  - Quyu Kong
  - Marian-Andrei Rizoiu
date: "2021-12-13"
output: html_document
categories: [Research]
image:
  placement: 1
  focal_point: "Center"
  preview_only: true
summary: "ICWSM 2022 paper: \"Slipping to the Extreme: A Mixed-Method to Explain How Extreme Opinions Infiltrate Online Discussions\" "
---

In our [recent paper](https://arxiv.org/pdf/2109.00302.pdf) accepted at ICWSM 2022, we propose a complete solution to accelerate the qualitative analysis of problematic online speech — with a specific focus on opinions emerging from online communities — by leveraging machine learning algorithms.

In 2020, the COVID-19 pandemic alerted the world to complex issues that arise from social media platforms circulating user-generated misinformation, hate speech, and conspiracy theories. There are several primary types of quantitative methods for addressing problematic information, including large-scale monitoring of social media datasets, understanding platforms, users, and networks contributing to the "infodemic", and predicting future pathways of information spreading.
These studies provide valuable insights into understanding
how problematic information spreads and detecting which sources are reshared frequently and by which accounts. However, these approaches often have less to say about why certain opinions and views gain traction with vulnerable groups and online communities. Qualitative research methods are well placed to address this gap. They provide rich, contextual insights into the social beliefs, values, and practices of online communities, which shape how information is shared and how opinions are formed.
Nevertheless, a common criticism of qualitative research is that the in-depth knowledge comes at the expense of generating insights of limited representativeness and weak robustness of the findings. Therefore, there is a gap between the depth of insight gained from ethnographic and qualitative approaches and the breadth of knowledge gained from computational methods from data science.

This work aims to fill this gap by proposing a mixed-method approach that brings together qualitative insights, large-scale data collection, and human-in-the-loop machine learning approaches. We apply our method to map both in-depth and in-breadth the problematic information around four topics: *2019-20 Australian bushfire season*, *Climate change*, *COVID-19*, and *Vaccination* on three social media platforms (Facebook, Twitter and Youtube).

## The Proposed Pipeline

![The pipeline of machine learning accelerated qualitative research where the human-in-the-loop machine learning algorithms are employed for dataset augmentation.](fig1.png)

We present a complete solution that bridges and facilitates both qualitative and quantitative analysis for studying problematic online speech.
The pipeline consists of three components:
  - **Deep qualitative study**: we build a platform based on an open-source tool, *Wikibase*, where qualitative and quantitative analysis is conducted. It enables constructing an ontology of problematic online speech by performing the qualitative study, which labels data by topics and builds the vocabulary of opinions simultaneously.
  - **Unlabeled data collection**: we then collect large-scale raw data using the uncovered vocabulary from the deep qualitative study.
  - **Dataset augmentation**: we employ machine learning algorithms to augment the data labeling process with a human-in-the-loop setting. By adopting the state-of-the-art text classification algorithm, RoBERTa, we first train the classifiers to identify problematic speech on postings annotated by the qualitative researchers. Next, we deploy three strategies to select unlabeled data. The active learning strategy selects the data for which the classifiers are most uncertain. The top-confidence strategy selects data that classifiers are most certain about. The third strategy — the random strategy — randomly samples from unlabeled data. The qualitative researchers then label the sampled data, we introduce the newly labeled data in the ontology, and repeat the procedure iteratively until the predictive performance converges.

## Applying the Qualitative Mapping

We employ the obtained augmented labeled set to analyze the dynamics of problematic opinions at scale. We machine-label the opinions in a large set of postings spanning over a long time period which allows us to apply the qualitative-defined coding schema to a significantly larger sample of postings, therefore reducing the unavoidable selection bias of the deep qualitative study. It also offers a critical tool for analyzing co-occurred opinions which help identify central opinions. It is common when postings express multiple opinions.

We explore central opinions by building an opinion co-occurrence network in the online conversation of the topic **2019-20 Australian bushfire season**. In the network, nodes are the opinions captured during the bushfire conversation, while edges are present when both opinions are detected in the same postings. The node
degree of a given opinion node represents the number of opinions co-occurred with it. The edges are weighted by the number of postings in which their connected node opinions co-occurred.

The following plot presents the daily proportions of weights of each edge among all edges between September 2019 and January 2020. We show six edges (i.e., opinion pairs) to represent three types of temporal dynamics:
  - A continuous and relatively strong association between prevalent opinions — "Climate change crisis isn’t real" and "Climate change is a UN hoax", which not notably is a conspiracy theory.
  - Associations with declining relative frequencies — "Greta Thunberg should not have a platform or influence as a climate..." and "Women and girls don’t deserve a voice in the public sphere".
  - Rising associations such as "bushfires and climate change not related" and "bushfires were caused by random arsonists"; and also the conspiracy theory associations between "United Nations is corrupt" and "United Nations want to be the global ruling government".
![Daily proportions of edge weights of six selected co-occurred opinions pairs.](fig2.png)

In the following plot, we map the co-occurrence network from posts published over 14 days in late September 2019, i.e., the period when the betweenness for conspiracy opinions is at peak. This figure explains the ambivalent network role that conspiracy opinions can play: we first note a conspiracy opinion with relatively high degree and frequency — "Climate change is a UN hoax" —, while we also observe the presence of low degree but high betweenness conspiracy opinions at the periphery of the network — "Bushfires linked to secret elites’ secret technology (chemtrails, HAARP, HSRN, geoengineering)", "bushfires deliberately lit to promote a climate change agenda" and "Australia should not be a member of the United Nations".

![A visualization of the co-occurrence network in late September 2020 — node sizes and colors indicate the degrees and betweenness values](featured.png)