---
layout: post
title: "Embodied Predictive Musical Instrument (EMPI)"
date: 2020-04-01
tags:
- research
- machine-learning
- neural-networks
- music
- music technology
- raspberry-pi
- performance
description: "The EMPI is a minimal electronic musical instrument for experimenting with predictive interaction, featuring a single physical input lever, a matching physical output, and on-device ML on a Raspberry Pi."
image: /assets/images/performing/empi-desk.jpg
---

The EMPI is a minimal electronic musical instrument for experimenting with predictive interaction techniques. It includes a single physical input — a lever — and a matching physical output, a built-in speaker, and a Raspberry Pi for sound synthesis and machine learning computations.

![The EMPI, a small white box with a screen and two control arms.]({{site.baseurl}}/assets/images/performing/empi-desk.jpg)

{% include youtubePlayer.html id="tvgqxmHr9wU" %}

The instrument is designed to be as simple as possible while still enabling meaningful exploration of how predictive ML models can interact with human performers. The matched input and output design allows direct comparison between what a performer plays and what the instrument predicts.

The EMPI was described in a paper in *Frontiers in Artificial Intelligence*:

    @article{Martin2020,
      author = {Martin, Charles Patrick and Torresen, Jim},
      title = {Understanding Musical Predictions with an Embodied Interface for Musical Machine Learning},
      journal = {Frontiers in Artificial Intelligence},
      year = {2020},
      doi = {10.3389/frai.2020.00006},
      url = {https://doi.org/10.3389/frai.2020.00006}
    }

_edit_:

I later spoke about EMPI at NIME2022 workshops with the talk [slides here](https://cpmpercussion.github.io/creative-prediction/presentations/2022-NIME-embedding-embodied-music-generation/#/title)
