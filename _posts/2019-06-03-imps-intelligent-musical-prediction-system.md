---
layout: post
title: "Intelligent Musical Prediction System (IMPS)"
date: 2019-06-03
tags:
- research
- machine-learning
- neural-networks
- nime
- open-source
- music
description: "IMPS connects musicians and interface developers with deep neural networks via OSC, enabling real-time musical prediction and performance without requiring large datasets or specialist hardware."
image: /assets/images/performing/2019-laptop-setup.jpg
---

The Intelligent Musical Prediction System (IMPS) is a system for connecting musicians and interface developers with deep neural networks. IMPS connects with any musical interface or software using Open Sound Control (OSC) and helps users to record a dataset, train a neural network, and interact with it in real-time performance.

![A laptop and MIDI interface setup for an IMPS performance in a concert hall.]({{site.baseurl}}/assets/images/performing/2019-laptop-setup.jpg)

{% include youtubePlayer.html id="Kdmhrp2dfHw" %}

Rather than requiring large datasets or a dedicated GPU workstation, IMPS is designed to let musicians record their own gestural data, train a small mixture density recurrent neural network, and start using it as soon as possible. The system works with however many dimensions of data you need and predicts future events in absolute time. It connects easily to environments such as Max, Pd, and Processing, and is practical to run on a Raspberry Pi.

IMPS was presented at the [International Conference on New Interfaces for Musical Expression (NIME) 2019](https://www.ufrgs.br/nime2019/) in Porto Alegre, Brazil.

The source code is available on [GitHub](https://github.com/cpmpercussion/imps).

    @inproceedings{Martin2019,
      author = {Martin, Charles Patrick and Torresen, Jim},
      title = {An Interactive Musical Prediction System with Mixture Density Recurrent Neural Networks},
      pages = {260--265},
      booktitle = {Proceedings of the International Conference on New Interfaces for Musical Expression},
      editor = {Queiroz, Marcelo and Sedó, Anna Xambó},
      year = {2019},
      month = jun,
      publisher = {UFRGS},
      address = {Porto Alegre, Brazil},
      issn = {2220-4806},
      url = {http://www.nime.org/proceedings/2019/nime2019_paper050.pdf}
    }


