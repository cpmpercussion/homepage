---
layout: post
title: 'NIME2015: Tracking an iPad Ensemble with Gesture Classification and Transition
  Matrices'
categories: []
tags:
- NIME
- Poster
- Conference
- Research
- iPad Ensemble
- Gesture Classification
- Transition Matrices
status: publish
type: post
published: true
meta:
  _thumbnail_id: '874'
---

I've just gotten back from NIME2015 in Baton Rouge where I presented a poster about my performance tracking system for iPad ensembles. Great to catch up with new and old NIMErs! The paper is 
[available here](https://nime2015.lsu.edu/proceedings/242/index.html) and here's the text of the poster:

## Metatone Classifier

We have designed a server-based agent called Metatone Classifier that tracks musical interaction on touch screen apps and makes calculated adjustments to the performers’ interfaces. Our agent interacts with an iPad ensemble performing on apps that respond by updating their user interface.

The aim of our system is to present an "interface-free interface" to the performers where their touch-gestures during an improvisation or composed work are used to adjust pitches, effects, and sonic material. We have developed several iPad apps that interact with our agent and used them in ensemble performances with two to seven performers.

During a performance, our agent observes touch-screen interactions and classifies them as a sequence of gestural states. It estimates the occurrence of new ideas across the ensemble by calculating a measure, flux, on the transition matrix of these gesture states.

## System Design

![The system layout of a Metatone Classifier and iPad Ensemble performance.]({{ site.baseurl }}/squarespace_images/static_500baf96c4aa540325612fa5_500bb0b2e4b042ea6e35b13f_55738061e4b048703924e357_1433632870929_Figure1-SystemDiagram.jpg) The system layout of a Metatone Classifier and iPad Ensemble performance. 
  
Metatone Classifier consists of a Python application which runs on a
laptop computer or on a remote server. During performances, the
ensemble's iPad apps connect to the server over a Wi-Fi network using
Bonjour. Once connected the iPad apps send logs of each touch event to
the agent using the OSC message format. The agent analyses the
performances of all connected iPads and returns information once per
second.

Two kinds of information are returned to the performers’ iPads: a
classification of the performers’ recent touches into one of nine
gesture classes, and whether a "new idea" has been detected in the
ensemble. Gesture classification is performed using a Random Forest
classifier. Identifying new-ideas in the performance involves
calculating a matrix of the performers’ recent transitions between
gestures classes and applying a matrix measure, flux, to these
transition matrices.

We have evaluated the time-complexity of Metatone Classifier tracking
from zero to four performers playing simultaneously. The mean time to
complete an analysis had a significant (p < 0.001) linear relationship
with the number of performers so we were able to estimate that an
ensemble of 25 iPads could be an upper bound for the present system to
perform an analysis each second.
  
![The time-complexity of running our classification system increased linearly with the number of players. We benchmarked the software using  from 0 to 4 simultaneous iPad performers and would expect our current software to run with up to around 25 iPads.]({{ site.baseurl }}/squarespace_images/static_500baf96c4aa540325612fa5_500bb0b2e4b042ea6e35b13f_557381e0e4b0c5ac0274d014_1433633250551__img.jpg) The time-complexity of running our classification system increased linearly with the number of players. We benchmarked the software using  from 0 to 4 simultaneous iPad performers and would expect our current software to run with up to around 25 iPads. 

## Touch Gestures and Gesture Classifier
       
![The gesture classifications and new idea messages sent during a performance. Each line represents a different performer.]({{ site.baseurl }}/squarespace_images/static_500baf96c4aa540325612fa5_500bb0b2e4b042ea6e35b13f_557380d3e4b017c5045587be_1433632984962__img.jpg) The gesture classifications and new idea messages sent during a performance. Each line represents a different performer.  

Metatone Classifier uses a vocabulary of nine continuous, percussive touch gestures that were identified in a previous qualitative study of iPad improvisations by percussionists. Descriptive statistics are calculated from a sliding five-second window of each performer's touch data and classified using a Random Forest classifier.

Two prototype versions of the classifier were trained using examples of each gesture from a studio performance but the current version uses gestures captured in a formal procedure. An evaluation using ten applications of stratified 10-fold cross validation was performed on each of these classifiers. The classifier that was trained using formally collected data had the highest accuracy (Mean = 0.973 S.D. = 0.022) and the effect of formal data-collection on accuracy was found to be significant through a one-way ANOVA procedure (F(2,297) = 31.7, p < 0.001).
  
![Ensemble Metatone performing on iPads as a septet.]({{ site.baseurl }}/squarespace_images/static_500baf96c4aa540325612fa5_500bb0b2e4b042ea6e35b13f_55738112e4b0976301e04db0_1433633050076__img.jpg) Ensemble Metatone performing on iPads as a septet. 

![The cross-validation accuracy of three data sets for our Gesture Classifier. The formal procedure had a significantly higher accuracy despite having a similar number of samples as other methods.]({{ site.baseurl }}/squarespace_images/static_500baf96c4aa540325612fa5_500bb0b2e4b042ea6e35b13f_55738183e4b008893bda704f_1433633157916__img.jpg) The cross-validation accuracy of three data sets for our Gesture Classifier. The formal procedure had a significantly higher accuracy despite having a similar number of samples as other methods. 

### Gesture Classes:

* n: None
* ft: Fast Taps
* st: Slow Taps
* fs: Fast Swipes
* fsa: Accelerating Swipes
* vss: Very Slow Swirls
* bs: Big Swirls
* ss: Small Swirls
* c: Combinations

## Transition Matrices and Flux (and New Ideas)

![The ANU New Music Ensemble performing with Metatone Classifier and PhaseRings (Photo: Chloë Hobbs).]({{ site.baseurl }}/squarespace_images/static_500baf96c4aa540325612fa5_500bb0b2e4b042ea6e35b13f_5573824de4b008083663ce5d_1433633364226__img.jpg) The ANU New Music Ensemble performing with Metatone Classifier and PhaseRings (Photo: Chloë Hobbs). 

A transition matrix of all performers’ touch interactions is used to summarise the behaviour of the whole ensemble and identify moments of peak gestural change. Each musicians’ gesture activity over a performance can be represented as a sequence of gestural states, and a transition matrix can be calculated as for a first order Markov chain. The transition matrix of the whole ensemble is the average of each performer's transition matrix.
       
![A gesture transition matrix for a 15-second window represented as a heat map. Higher values on the diagonal indicate static gestural activity while off-diagonal indicates gestural movement in the ensemble. Our flux measure exposes this as a single value between 0 and 1.]({{ site.baseurl }}/squarespace_images/static_500baf96c4aa540325612fa5_500bb0b2e4b042ea6e35b13f_55738283e4b0601c9cccc82d_1433633415277__img.jpg) A gesture transition matrix for a 15-second window represented as a heat map. Higher values on the diagonal indicate static gestural activity while off-diagonal indicates gestural movement in the ensemble. Our flux measure exposes this as a single value between 0 and 1.

![The definition of our flux matrix measure. The value of flux(P) is in the interval [0,1], where 0 represents completely static ensemble activity and 1 represents maximum gestural change.]({{ site.baseurl }}/squarespace_images/static_500baf96c4aa540325612fa5_500bb0b2e4b042ea6e35b13f_55739f49e4b0fff565084b7c_1433640783562__img.jpg) The definition of our flux matrix measure. The value of flux(P) is in the interval [0,1], where 0 represents completely static ensemble activity and 1 represents maximum gestural change.

Our agent calculates the ensemble transition matrix over 15 second windows to examine how transition activity changes throughout the performance. We use a matrix measure called "flux" to compare this activity. Flux is a measure of how frequently performers change gesture over this window and returns a value in the range [0,1]. When a flux reading exceeds the previous window by a certain threshold, a "new-idea" event is sent to the performers' iPads.

## PhaseRings
       
![PhaseRings - an annular interface that for ensemble performances mediated by Metatone Classifier. PhaseRings is available for free in the App Store: metatone.net/phaserings]({{ site.baseurl }}/squarespace_images/static_500baf96c4aa540325612fa5_500bb0b2e4b042ea6e35b13f_5573a0dae4b0cd726654e0e1_1433641188232_Figure6-PhaseRingsScreen.png) PhaseRings - an annular interface that for ensemble performances mediated by Metatone Classifier. PhaseRings is available for free in the App Store: metatone.net/phaserings 

PhaseRings is one of our iPad apps designed to interact with Metatone Classifier in ensemble performances. The app consists of an annular interface for performing with percussive samples and pure synthesis sounds. The concentric rings represent different pitches of a single sound source which are selected randomly from a scale.

Tapping a ring will activate a note with a natural decay while swirling on a ring will create a sustained sound. Each player has different pitches chosen from one of a sequence of scales which advance for all performers when a new-idea message is sent to the ensemble or a performer activates a UI element.

As the performers explore different touch gestures, they are rewarded with the opportunity to perform new melodic material with access to new notes and experience a sense of cohesive harmonic progression.
