---
layout: post
title: Neural Network Ensembles in London and Representing Collaborative Interaction
categories:
- essay
tags:
- AI
- RNN
- music
- iPad
- Neural Network
- Deep Learning
- conference
status: publish
type: post
published: true
meta: {}
---

I recently had the chance to present a paper about my "Neural iPad Ensemble" at the Audio Mostly conference in London. The 
[paper](http://static1.squarespace.com/static/500baf96c4aa540325612fa5/500bb0b2e4b042ea6e35b13f/599db35cebbd1aff902d035b/1503507296722/AM2017-deep-models-for-ensemble-performance-author-version.pdf), discusses how machine learning can help to model and create free-improvised music on new interfaces, where the rules of music theory may not fit. I described the Recurrent Neural Network (RNN) design that I used to produce an AI iPad ensemble that responds to a "lead" human performer. In the demonstration session, I set up the iPads and RNN and had lots of fun jamming with the conference attendees.

![]({{ site.baseurl }}/assets/squarespaceblog/2017-09-12-neuralnetensemble-paper-1.jpg)
![]({{ site.baseurl }}/assets/squarespaceblog/2017-09-12-neuralnetensemble-paper-2.jpg)

Many of those at the conference were very curious about making music with AI systems and the practical implications of using deep learning in concert. Some had appealing, enigmatic, and sometimes confused, assumptions about musical AI. For example, I was often asked whether I could recognise personalities of the performers in the output. This isn't possible in my RNN, because, like in all machine learning systems, the output reflects only the training data, and not the context that we humans see around it.

A limitation of my system is that it learns musical interactions as sequences of high-level gestures. These measurements are made once every second on the raw touchscreen data and describe it as, for examples, "fast taps", or "small swirls". In the performance system, a synthesiser replays chunks of performances that correspond to the desired gestures. This simplification makes it easier to design the neural network, but mean that the RNN isn't trained on the low-level data that we might consider to contain the nuanced "personality" of a performance.

Another easily confused point of my system is that the human performer isn't really the "leader". In the interest of making the most of a limited data set, every performer in every example is permuted as the "leader" and each of the three "ensemble" performers. In fact, few (if any) performances in the corpus had a leader at all. In my system, the human performer is really just one of four equal performers, so it's unreasonable to expect that you could "control" the RNN performers by performing in a certain way, or doing something unexpected.

A practical issue with performance with the neural iPad ensemble is starting and stopping the music! In a human ensemble, the performers use cues like counting in, an audible breath, or a look, to bring in the ensemble and to signal the end of an improvisation. With my RNN ensemble, cues have no effect; sometimes the group starts playing, sometimes it doesn't. Just when you think the performance might be over, the group starts up again without you! Thinking about the training data, this behaviour makes sense. Each training example is 120 seconds long -- too short to capture the long-term curve of a performance, including starting and ending. The examples do contain plenty of instances where one performer plays alone, or three play while one lays out, so there's precedence in the data for completely ignoring the "leader" starting and stopping!

As with many AI systems, these limitations reveal that humans are so good at combining different datasources and contexts that we forget that we're doing it. A truly "natural" iPad ensemble might have to be trained on much more than just high-level gestures in order to keep up with "obvious" musical cues and reproduce musical personalities.

While this system has limitations, it is still fun to play with  and useful as a reflection on "creative" AI. Of course, there's many ways to improve it, one of the most important would be to train the RNN on the lowest level data available; in this case, the raw touch event data from the iPad screens. A promising way to approach this is with Mixture Density RNNs (more on that later). I'm looking forward to more chances to perform with and talk about Musical AI soon!
