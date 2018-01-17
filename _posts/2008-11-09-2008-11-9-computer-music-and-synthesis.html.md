---
layout: post
title: Computer Music and Synthesis
categories: []
tags:
- computer music
- supercollider
status: publish
type: post
published: true
meta: {}
---

In order to gain a fundamental knowledge of synthesis as a base for my research I chose to work from the textbook Computer Music using SuperCollider 3 by David Cottle. SuperCollider (or SC) is a program which aims to be a general tool for creating music on computer. It is extremely powerful and has a flexible and deep interface which makes it perfect for learning general techniques of synthesis. The following report explains some of the fundamental methods of synthesis and demonstrates how they can be implemented in SuperCollider.

The interface of SuperCollider is a programming language and the act of creating music with SuperCollider means programming SuperCollider’s internal system to create, modify and combine streams of audio data which are then sent to the computer’s sound card and, finally, one or more speakers. Although daunting for beginning users, text based programming languages are incredibly flexible as well as efficient and fast for a skilled user.

The tools that SuperCollider provides for synthesis are audio objects like the sine oscillator (producing a pure sine tone), noise generators that produce rich waveforms, control objects that can change parameters of these audio objects over time and objects like frequency filters and resonators which can be used to sculpt interesting sounds. In this report we will demonstrate using actual SuperCollider code with an audio example corresponding to each code example We first look at the general code for creating an object.

### Example 1.

    ObjectName(setting1, setting2, setting3, …);

So, objects are created by stating their name followed by a list of settings (Each setting is either a number or the name of some other object. Our first real example is a sine oscillator:

### Example 2.

    SinOsc.ar(440, 0, 0.5, 0);

The list of values for SinOsc.ar objects is (frequency, phase, volume, add).  So this sine oscillator will oscillate at 440Hz and have a volume of 0.5 (volume is normally a number from 0 to 1 where 0 is silence and 1 is very loud). This sine oscillator has ‘phase’ and ‘add’ set to zero, phase defines the starting point of the oscillation and ‘add’ can shift the oscillation from being between +1 and -1 to, for example 11 and 9 (with an ‘add’ of 10), this parameter is not used for creating sine tones but for using sine oscillations for other purposes. 

To have the sine tone played through the computers sound card we need to add a little bit more code:

### Example 3.

    { SinOsc.ar(440, 0, 0.5, 0) }.play;

[listen - mp3](http://www.epmartin.com/cpm/CMS-1108/CMS-eg03.mp3)Here the parenthesis encapsulate a section of code, and “play” is an instruction that tells SuperCollider to connect this sine oscillator to the first output channel of the computer.

## Additive Synthesis

The aim of additive synthesis is to create interesting sounds by playing different sine tones.  A simple example of additive synthesis is as follows:

### Example 4.

    {SinOsc.ar(440,0,0.5) + SinOsc.ar(880,0,0.3)}.play

[listen - mp3](http://www.epmartin.com/cpm/CMS-1108/CMS-eg04.mp3)This example plays the summed sound of two sine tones, the first at 440Hz and the second at 880Hz. By playing these two A’s an octave apart we start to hear a rich sound, reminiscent of real instruments where the sound contains overtones from the harmonic series.

It is a fact that any periodic waveform (that is, any waveform that we would hear as a tone) can be represented as the sum of sine waves. This field, Fourier analysis, was initiated by the great mathematician Joseph Fourier around 1820 in his study of the propagation of heat. As it turns out, the mathematical rules which can describe sound wave are common to all waves (i.e. periodic functions). Studies of light, radio communications, heat, sound and many other physical examples are all fundamentally related.

Fourier analysis means that, theoretically, the sound of any instrument could be precisely replicated as the sum of sine waves. The first practical problem is that real instruments don’t have exactly the same sound each time they are played and that their sound includes a non-periodic element (for example the contact noise of a mallet striking a marimba bar).  The second practical problem is that the Fourier series for a waveform may be infinitely long, so the entire series could not be played back on any conventional synthesiser or computer.

Despite these drawbacks, additive synthesis can produce beautiful sounds. Because SuperCollider is a programming language it is easy to generate a series of sine tones with frequencies based on the harmonic series, producing a rich tone or frequencies chosen arbitrarily, producing sounds that could be dark and cymbal-like or bright and clashing.

As examples of additive synthesis, we first give the sum of 10 tones of the harmonic series starting at 440Hz.

### Example 5.

    ({
    var fundamental;
    fundamental = 440;
    Mix.new(
    Array.fill(
    10, {arg counter;
    SinOsc.ar(
    freq: fundamental * (counter + 1),
    mul: 1/(counter + 2)
    )}
    )
    )
    }.play
    )

[listen - mp3](http://www.epmartin.com/cpm/CMS-1108/CMS-eg05.mp3)Now a sum of tones not necessarily in the harmonic series. This code uses random numbers to choose each subsequent frequency.

### Example 6.

    ({
    var fundamental;
    fundamental = 110;
    Mix.new(
    Array.fill(
    5, {arg counter;
    SinOsc.ar(
    freq: fundamental * rrand(0.0, 2.0) * (counter + 1),
    mul: 1/(counter + 3))}
    )
    )
    }.play
    )

[listen - mp3](http://www.epmartin.com/cpm/CMS-1108/CMS-eg06.mp3)The traditional drawback of additive synthesis has been that it can require a large number of oscillators – one for the fundamental and each overtone. Affordable analogue synthesisers generally only have about three oscillators but the two examples I just presented used 10 and 5 sine oscillators respectively. SuperCollider and other computer music systems make additive synthesis with a large number of oscillators (hundreds or thousands) achievable, but this is still a processor-intensive way of producing sounds. The other two paradigms of synthesis, subtractive and modulation were initially developed as ways of producing rich sounds without vast numbers of oscillators. In the world of computer music this means that they use the computer’s processor more efficiently.

## Subtractive Synthesis

In additive synthesis we create a rich sound by summing many simple sound sources. Subtractive synthesis is the inverse process. We start with a complex sound and make it simpler by removing or deemphasising bands of frequencies. The richest possible sound source is white noise, this means a waveform that is defined by a random function that produces equal power in all frequencies. The Fourier series of white noise is an infinite series of sine functions of equal amplitude, one for each frequency. There are other complex sound sources used for subtractive synthesis. Pink noise, with power equalised over each octave rather than each frequency, is also very useful.

To cut down a waveform in SuperCollider we use objects that filter out certain bands of frequencies and resonate particular frequencies that we want to emphasise. The following code uses a low pass filter to cut frequencies higher than 440Hz  in a pink noise source. The parameters of this filter also emphasise 440Hz in the waveform which generates a recognisable tone.

### Example 7.

    {RLPF.ar(PinkNoise.ar,440,0.01)}.play

[listen - mp3](http://www.epmartin.com/cpm/CMS-1108/CMS-eg07.mp3)A related strategy is to resonate certain frequencies of the source sound without necessarily cutting anything. The following example uses the same pink noise source but uses the Klank object to amplify a number of frequencies.

### Example 8.

    { Klank.ar(
    `[[220, 657, 893, 1211], nil, [1, 1, 1, 1]],
    PinkNoise.ar(0.01)
    )}.play;

[listen - mp3](http://www.epmartin.com/cpm/CMS-1108/CMS-eg08.mp3)The parameters of the Klank object define the resonating frequencies, their relative amplitudes, decay times and the source to be resonated. The decay times don’t make sense when the source is a constant sound, but when the source is a percussive sound, different decays and amplitudes determine how strongly we hear each resonated frequency.

## Control of Parameters

The most interesting aspect of computer music and synthesis is controlling the parameters of sounds that we create. Just as on a traditional instrument we control pitch, dynamic and timbre we do the same on computer based instruments. Electronic music pioneers used mechanical and electronic devices to automatically control their instruments and create new sounds. We can use SuperCollider in the same way. For example:

### Example 9.

    {SinOsc.ar(SinOsc.ar(3, 0, 50, 440), 0, 0.5, 0)}.play;

[listen - mp3](http://www.epmartin.com/cpm/CMS-1108/CMS-eg09.mp3)

### Example 10.

    {SinOsc.ar(880, 0, SinOsc.ar(1, 0, 0.15, 0.5), 0)}.play;

[listen - mp3](http://www.epmartin.com/cpm/CMS-1108/CMS-eg10.mp3)In each piece of code there are two SinOsc.ar objects, but only one is being played through the soundcard as a tone, the other is being interpreted as a changing number, controlling a parameter of the other sine oscillator. In the first example, the second SinOsc.ar object is in the frequency position for the main oscillator, which creates an oscillating pitch or vibrato effect. The second example has the SinOsc.ar object in the volume position giving an oscillating volume or tremolo effect.
Each of these control oscillators has appropriate settings for their purpose. Both have very low frequency, 3Hz and 1Hz, so even if they were played through a speaker we wouldn't hear them as tones. Both have strange values for their volume and offset (these parameters are called mul and add in SuperCollider), the first has a mul of 50 and an add of 440, this means that it starts at 440, then oscillates up to 440 + 50 = 490 and back down to 440 – 50 = 390.

Another reason to automatically control these instruments is to dynamically adjust volume over time, to cut sounds into notes. Generally, we create a separate object called an envelope which listens for a trigger, perhaps from pressing a key on a MIDI controller or clicking the mouse button. The envelope might then create a note by turning up the volume of a tone quickly and then turning it down slowly until it reaches zero. This kind of envelope would be the analogue of a percussion-type sound where notes reach their loudest point quickly and have a slow, uncontrolled decay. The following example implements this idea:

### Example 11.

    ({
    var trig, envel;
    trig = Impulse.kr(0.5);
    envel = EnvGen.kr(Env.perc(0.1, 1), gate: trig);
    SinOsc.ar([440,440], mul: envel)
    }.play)

[listen - mp3](http://www.epmartin.com/cpm/CMS-1108/CMS-eg11.mp3)This example requires some explaining. The first line “({“ and the last line “}.play)” just encapsulate and play a block of code through the computer’s sound card. The line starting with “var” sets up some variable to have the names “trig” and “envel”, variables are just named objects, giving them names means that we can use them again and again without typing out the whole object definition.

The next two lines begin with the names of our two variables and an “=” symbol. These lines are defining what the variables are. “trig” is defined to be an object called Impulse which is going to create a trigger for our envelope, this Impulse object has a frequency of 0.5Hz, so it creates an impulse every two seconds. “envel” is defined to be an envelope, this is a bit complicated. It’s actually defined to be an EnvGen object which links a type of envelope with a trigger. The type of envelope is Env.perc which is a percussive envelope, the two settings for Env.perc are attack time and decay time which are set to 0.1s and 1s respectively. The trigger for our evelope is going to be the variable “trig”.

The next line sets up a sine wave oscillator at 440Hz, notice the the mul, or volume, is set to the variable “envel”, that is, the value of an envelope is a number that can be interpreted as a volume. The next example uses an envelope with the Klank object that we saw in a previous example. Instead of having the Klank source as constant pink noise, an envelope listens to an Impulse object as the trigger and turns up the volume on the pink noise for only 0.01 seconds at each trigger. Since the decay on the Klank object is long, we end up with the chime like sound of the resonating frequencies.

### Example 12.

    ({
    var att, burstLength, trig, burstEnv, burst;
    att = 0.0001;
    burstLength = 0.01;
    trig = Impulse.kr(1);
    burstEnv = Env.perc(att, burstLength);
    burst = PinkNoise.ar(EnvGen.kr(burstEnv, gate: trig) * 0.7);
    Klank.ar(`[[220, 657, 893, 1211], nil, [0.8, 0.7, 0.6, 0.5]], burst)*0.3
    }.play)

[listen - mp3](http://www.epmartin.com/cpm/CMS-1108/CMS-eg12.mp3)

## Modulation Synthesis

In the previous section we considered the idea that the frequency and amplitude of a sine tone could be modulated by another sine oscillator.

### Example 13.

    {SinOsc.ar(SinOsc.ar(3, 0, 50, 440), 0, 0.5, 0)}.play;

### Example 14.

    {SinOsc.ar(880, 0, SinOsc.ar(1, 0, 0.15, 0.5), 0)}.play;

In these examples we gave the modulating oscillator a low frequency, 3Hz and 1Hz respectively.  However, if we set the modulating oscillator to an audible frequency, the result is that we hear the basic sine tone as well as other extra frequencies.

### Example 15.

    {SinOsc.ar(SinOsc.ar(440,0,50,440), 0, 0.5, 0)}.play;

[listen - mp3](http://www.epmartin.com/cpm/CMS-1108/CMS-eg15.mp3)

### Example 16.

    {SinOsc.ar(880, 0, SinOsc.ar(440, mul:0.5), 0)}.play;

[listen - mp3](http://www.epmartin.com/cpm/CMS-1108/CMS-eg16.mp3)These extra frequencies, called sidebands are the frequencies that would have to be summed together to produce the same waveform using additive synthesis. Although it seems like the sidebands could be unwanted, the concepts of frequency modulation and amplitude modulation, or FM and AM, are used constantly in electronics and in music synthesis.

The sidebands that occur in frequency and amplitude modulation, as well as phase modulation, depend on the frequency of the original wave, or carrier wave, and the frequency and depth of the modulation. For AM it’s easy, the sidebands are the sum and difference of the carrier frequency and the frequency of the modulating wave. For FM, the sidebands are the sum and differences of multiples of the modulation frequency with the carrier frequency. The exact number of sidebands depends on the depth of the modulation, or how far the modulating oscillator varies the frequency, this number is usually called the index of the modulation.

Phase modulation, where the phase of the carrier wave is changed, sounds quite similar to frequency modulation and the sidebands are calculated in the same way. In SuperCollider, the PMOsc object is a pair of sine oscillators that are set up for phase modulation. The first three settings for this object are the carrier frequency, modulator frequency and index. In the following example, the Line object is used to vary the index from 0 to 100 over 8 seconds. This illustrates how the number of sidebands alter the timbre of the sound.

### Example 17.

    ({PMOsc.ar(
    440,
    660,
    Line.ar(0,100,8),
    0,
    0.1
    )}.play)

[listen - mp3](http://www.epmartin.com/cpm/CMS-1108/CMS-eg17.mp3)As with all periodic waveforms, the modulated waves can be replicated using a summed series of sine waves, one for the fundamental and each sideband. Modulation synthesis is mainly useful because of its efficiency, only two oscillators are required to produce rich sounds that could require hundreds of oscillators in additive synthesis.

## Conclusion

The objects mentioned in this report are a small selection of those available in SuperCollider. Additionally, although additive, subtractive and modulation synthesis are core methods for creating sounds in computer music, the real musicality in synthesis is in choosing appropriate methods and controlled settings to generate compelling sounds and then composing the sounds into interesting music.
A pdf version of this report is available 
[here](http://www.epmartin.com/cpm/CMS-1108/CMS-CharlesMartin-1108.pdf) and the code example are 
[here](http://www.epmartin.com/cpm/CMS-1108/CMS-SCexamples.rtf).
