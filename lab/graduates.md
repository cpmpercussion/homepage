---
layout: page
title: charleslab graduates
permalink: /lab/grads/
---

Here's some links to research produced by my graduate students. 

If you'd like to work on something like this, get in touch through [ANU](https://comp.anu.edu.au/people/charles-martin/), or on [Twitter](https://twitter.com/cpmpercussion)!

### [Feiyue Tao: Multi-View Web Interfaces in Augmented Reality](http://hdl.handle.net/1885/271412)

The emergence of augmented reality (AR) is reshaping how people can observe and interact with their physical world and digital content. Virtual instructions provided by see-through AR can greatly enhance the efficiency and accuracy of physical tasks, but the cost of content authoring in previous research calls for more utilization of legacy information in AR. Web information is a great source hosting a wide range of legacy and instructional resources, yet current web browsing experience in AR headsets has not exploited the advantage of 3D immersive space mixing the real and virtual environments. Instead of creating new AR content or transforming from legacy resources, this research investigates how to better present web interfaces in AR headsets, especially in a physical task instruction context. A new approach multi-view AR web interfaces is proposed, which suggests separating web components into multiple panels that can be freely arranged in the user's surrounding 3D space. The separation and arrangement would allow more flexible combination of web content from multiple sources and with other AR applications in the user's field of view.

#### BibTeX

```
@mastersthesis{1885-271412,
	author = {Tao, Feiyue},
	title = {Multi-View Web Interfaces in Augmented Reality},
	year = {2022},
	address = {Canberra, Australia},
	doi = {10.25911/5FRG-J326},
	url = {http://hdl.handle.net/1885/271412}
}
```

### [Yichen Wang: ]()

### [Xinlei Niu: Acoustic Scene Classification with Attention-based Neural Networks](http://hdl.handle.net/1885/270565)

Auditory information provides great help to human beings to recognize their surroundings and positions. However, the sound we perceived in the environment is often a mixture of many sounds that happened at the same time. Therefore, developing a system to automatically extract information from unprocessed audio provides a huge potential for human beings. For example, it can be utilized by automatic diving, multimedia searching, robots, etc. In this study, we proposed two Attention-based Neural Network models to achieve automatic acoustic scene classification systems. Both two models are powerful in extracting information on audio spectrograms and classifying them into their corresponding scene labels. We applied two acoustic scene datasets to verify our model and got the best accuracies which are 15.7% and 8.0% higher than their CNN baselines.

#### BibTeX:

```
@mastersthesis{Niu:2021,
	author = {Niu, Xinlei},
	title = {},
	year = {2021},
	address = {Canberra, Australia},
	doi = {10.25911/DR3N-7M40},
	url = {http://hdl.handle.net/1885/270565}
}
```


### [Torgrim Næss: A Physical Intelligent Instrument using Recurrent Neural Networks](https://www.duo.uio.no/bitstream/handle/10852/70773/1/naess_master.pdf)

#### Abstract:

Composing and playing music generally requires knowledge of music theory and exercise in instrument training. While traditional musical instruments often require years of arduous practice to master, intelligent musical systems can provide an easier introduction into music creation for novice users. This thesis describes the design and implementation of a novel intelligent instrument for interactive generation of music with recurrent neural networks, allowing users with little to no musical experience to explore musical ideas.

Even though using neural networks for music composition is not a new concept, most previous work in this field does not ordinarily support user interaction, and is often dependent on general-purpose computers or expensive setups to implement. The proposed instrument is self-contained, running an RNN-based generative music model on a Raspberry Pi single-board computer for continuous generation of monophonic melodies that are sonified using a built-in speaker. It supports real-time interaction where the user can modify the generated music by adjusting a set of high-level parameters: sampling temperature (diversity), tempo, volume, instrument sound selection, and generative model selection.

A user study with twelve participants was conducted to see the impact the different high-level parameter controls can have on a participant’s perceived feeling of control over the musical output from the instrument, and to evaluate the generative models trained on different datasets in terms of musical quality. The numerical ratings and open-ended answers were analyzed both quantitatively and qualitatively. The results show that the perceived feeling of control over the music was quite high, and the high-level parameter controls allowed participants to creatively engage with the instrument in the music-making process.

N.B.: This thesis resulted in a [NIME publication!](http://www.nime.org/proceedings/2019/nime2019_paper016.pdf).

#### BibTex:

    @mastersthesis{Naess:2019,
        Author = {Næss, Torgrim Rudland},
        Title = {A Physical Intelligent Instrument using Recurrent Neural Networks},
        School = {University of Oslo},
        Year = {2019},
        Address = {Oslo, Norway},
        URL = {http://urn.nb.no/URN:NBN:no-73901},
    }

### [Viktoria Røsjø: Variational Autoencoders with Mixture Density Networks for Sequence Prediction in Algorithmic Composition - A Musical World Model](https://www.duo.uio.no/bitstream/handle/10852/67479/1/Variational_Autoencoders_for_Algorithmic_Composition.pdf)

#### Abstract:

Does music contain a hierarchical component which is relevant when teaching a machine learning model to create music? And, can a machine learning model learn long term structure in music, based on its own perception of data?

In 2014, Diedrik P. Kingma and Max Welling presented a novel technique in generative modelling, called the Variational Autoencoder (VAE). The method presented a technique for learning intractable data distributions, and at the same time representing the data in a compressed latent space. From this latent space, it was possible to sample new datapoints, with similar features as those from the true data set. This method was quickly adopted for modelling real valued data, with both a fixed dimensionality, and in sequences. Through the course of 2017 and 2018, Google Brain released two variational autoencoders for sequential data: SketchRNN for sketch drawings, and MusicVAE for symbolic generation of music. These models inspire the variational autoencoder framework used in this thesis. The MusicVAE has a hierarchical element to assist in creation of music: a recurrent neural network function as a composer to manage the structural development of melodies. Their studies showed that the hierarchical component helped create more probable musical compositions than the formal VAE. MusicVAE is taken as a starting point for this thesis; however, rather than the recurrent neural network, a new architecture for generating high-level structure in music is introduced, using a mixture density network.

The Mixture Density Network, a network that can predict multi-valued output, was developed in 1994 by Christopher M. Bishop. The model can utilize any kind of network to condition the probability distributions. In 2018, David Ha and Ju ̈rgen Schmidhuber used a recurrent mixture density network (MDRNN) for predicting latent vectors in a reinforcement learning model. This has inspired the idea of replacing the recurrent composer from the MusicVAE with a MDRNN. This thesis introduces this novel architecture, in which musical compositions are guided by generating sequences of vectors from a VAE’s compressed latent space. This is a novel architecture, in which compositions of music is guided by learned sequences of latent vectors. The model is named Mixture Composer Variational Autoencoder, or MCVAE.
Evaluation of the models showed that a difference in the models was noticeable. An evaluation with human annotators shows that music that has been composed by the MCVAE has noticeably better musical qualities than music generated from the formal VAE. Another evaluation, using a 5-gram model show that music made with guidance from the MDN creates melodies which are a lot more probable than music made without guidance.

#### BibTex:

    @mastersthesis{Rosjo:2019aa,
        Author = {Viktoria Røsjø},
        Title = {Variational Autoencoders with Mixture Density Networks for Sequence Prediction in Algorithmic Composition - A Musical World Model},
        School = {University of Oslo},
        Year = {2019},
        Address = {Oslo, Norway},
        URL = {http://urn.nb.no/URN:NBN:no-70656},
    }


### [Benedikte Wallace: Predictive songwriting with concatenative accompaniment](http://folk.uio.no/charlepm/student_theses/Wallace-Predictive_Songwriting_with_Concatenative_Accompaniment.pdf)

#### Abstract:

Musicians often use tools such as loop-pedals and multitrack recorders to assist in improvisation and songwriting. While these devices are useful in creating new compositions from scratch, they do not contribute to the composition directly. In recent years, new musical instruments, interfaces and controllers using machine learning algorithms to create new sounds, generate accompaniment or construct novel compositions, have become available for both professional musicians and novices to enjoy. This thesis describes the design, implementation and evaluation of a system for predictive songwriting and improvisation using concatenative accompaniment which has been given the nickname PSCA. In its most simple form, the PSCA functions as an audio looper for vocal improvisation, but the system also utilises machine learning approaches to predict suitable harmonies to accompany the playback loop. Two machine learning algorithms were compared and implemented into the PSCA to facilitate harmony prediction: the hidden Markov model (HMM) and the Bidirectional Long Short-Term Memory (BLSTM). The HMM and BLSTM algorithms are trained on a dataset of lead sheets in order to learn the relationship between the notes in a melody and the chord which accompanies it as well as learning dependencies between chords to model chord progressions. In quantitative testing, the BLSTM model was found to be able to learn the harmony prediction task more effectively than the HMM model, this was also supported by a qualitative analysis of musicians using the PSCA system. The system proposed in this thesis provides a novel approach in which these two machine learning models are compared with regards to prediction accuracy on the dataset as well as the perceived musicality of each model when used for harmony prediction in the PSCA. This approach results in a system which can contribute to the improvisation and songwriting process by adding harmonies to the audio loop on-the-fly.

#### BibTex

    @mastersthesis{Wallace:2018aa,
        Author = {Benedikte Wallace},
        Title = {Predictive songwriting with concatenative accompaniment},
        School = {University of Oslo},
        Year = {2018},
        Address = {Oslo, Norway},
        URL = {http://urn.nb.no/URN:NBN:no-65381},
    }

### [Henrik Brustad: Digital Audio Generation with Neural Networks](http://urn.nb.no/URN:NBN:no-66304)

#### Abstract

In this thesis I explore three different techniques for generating digital audio using neural networks. All three techniques use different network structures and architectures suitable for generating sequential data. Operating at the sample level requires each technique to model dependencies across large time lags in order to generate realistic audio. This is a hard task for even the most sophisticated techniques.
To gain an understanding of how each technique works I have implemented two neural networks of different structures based on the same architecture, as well as familiarized myself with an implementation of a network using an architecture not commonly used to model sequential data.
To compare each technique I have trained each model on a dataset containing a large number of classical piano pieces. Each model is evaluated in terms of the audio quality and musicality of their generated audio.
Results suggest that each model could be used in applications using short amounts of digital audio. It is unclear, however, if these techniques are able to generate arbitrary music with high level structures, while containing the small details necessary to generate realistic sounds.

#### BibTex

    @mastersthesis{Brustad:2018aa,
        Author = {Henrik Granheim Brustad},
        Title = {Digital Audio Generation with Neural Networks},
        School = {University of Oslo},
        Year = {2018},
        URL = {http://urn.nb.no/URN:NBN:no-66304},
    }

