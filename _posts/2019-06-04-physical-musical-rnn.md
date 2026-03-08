---
layout: post
title: "Physical Musical RNN"
date: 2019-06-04
tags:
- research
- machine-learning
- neural-networks
- nime
- raspberry-pi
- music
description: "A physically encapsulated musical neural network: a standalone box running a melody-generating recurrent neural network on a Raspberry Pi, with knobs to control tempo, model, and sampling diversity."
image: /assets/images/performing/physical-musical-rnn.jpg
---

What happens if we make a music-generating neural network physically portable?

This is the question that I explored with Torgrim Næss in his master project throughout 2018 and 2019. This project explored our shared interests of deep learning and embedded hardware to go from a "what if" question, to a physical prototype that help us unpack the user experience (or musician experience!) of musical RNNs.

The Physical Musical RNN is a self-contained musical neural network in a small box. Inside is a Raspberry Pi running a melody-generating recurrent neural network that continually composes music. Five knobs let you adjust the sound, tempo, the ML model in use, and the "randomness" of the chosen samples to guide the music-making process.

![The physical musical RNN, a black box with a small screen and five knobs.]({{site.baseurl}}/assets/images/performing/physical-musical-rnn.jpg)

The melody RNN used in this project draws inspiration from popular CharRNN designs. RNNs like this are fun to build and (relatively) fast to train.

{% include youtubePlayer.html id="2RDVyOTRAj4" %}

This project was developed as a master's thesis by Torgrim Næss at the Robotics and Intelligent Systems group, University of Oslo supervised by Charles Martin. A paper reporting on our results was presented at the International Conference on New Interfaces for Musical Expression (NIME) 2019 in Porto Alegre, Brazil.

    @inproceedings{Naess2019,
      author = {Næss, Torgrim Rudland and Martin, Charles Patrick},
      title = {A Physical Intelligent Instrument using Recurrent Neural Networks},
      pages = {79--82},
      booktitle = {Proceedings of the International Conference on New Interfaces for Musical Expression},
      editor = {Queiroz, Marcelo and Sedó, Anna Xambó},
      year = {2019},
      month = jun,
      publisher = {UFRGS},
      address = {Porto Alegre, Brazil},
      issn = {2220-4806},
      url = {http://www.nime.org/proceedings/2019/nime2019_paper016.pdf}
    }


