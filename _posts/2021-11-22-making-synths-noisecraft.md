---
layout: post
title: Building Synths in NoiseCraft
author: Charles Martin
date: 2021-11-22
---

## Building Synths in NoiseCraft

> A synthesis tutorial by Charles Martin, 2021 ([charlesmartin.com.au](https://charlesmartin.com.au))

[NoiseCraft](https://noisecraft.app/) is a website that lets you build your own synthesiser by connecting together modules that create or modify electronic sounds.

In this tutorial you'll follow simple plans to create different electronic sounds and then use your knowledge to create a synthesiser.

The goals of the tutorial are:

1. Experiment with the fundamental parts of a synthesiser
2. Experience how these parts connect to make different sounds
3. Create a synthesiser and a short composition using it

## Task 0: Opening up NoiseCraft

- Get on to a laptop or desktop computer and open up a web browser.
- Type `https://noisecraft.app/` in the location bar and press `Enter`

You'll see **NoiseCraft** website. It's just a big empty space! That's right, **you** have to create the synthesiser here, but that's great because when **you create something** you understand it.

Let's notice a few things:

- The word "Play" is written in the top right corner. If you click "Play", then your synthesiser will make sound (when you've built it), a "Stop" will appear and you can click that to stop the sound.

It's **always** important to know how to turn an electronic instrument _off_ if you make a sound that's too loud or that you don't like.

- Click the empty workspace. A "Create Node" menu will appear with different boxes and word.

In NoiseCraft, a **node** is a building block of a synthesiser. You'll create your synth by creating **nodes** and joining them together.

- Click "AudiOut" in the "Create Node" menu, a little box with "AudioOut" on it will appear. Try dragging it around the workspace.

The **AudioOut** node is connected to your computer's speakers. Any sound you send to it will come out of your computer! (Once you click "Play"...)

Now we're ready to make some sound!

## Task 1: Sound Generators and Outputs

Synthesisers create complex sounds by combining and modifying simple _tone generators_. Let's create some different tone generators and see what kind of sounds they make.

**Before starting**: Turn the volume of your computer **all the way down**, if you're using headphones take them out/off. 

**Warning**: These experiments can create _VERY LOUD SOUNDS_. Be **very careful** with sound when experimenting with synthesisers! Only put your earphones on when you know the volume is at a good level.

Create these nodes:

- AudioOut (if you haven't got one already)
- Sine
- Const

Connect them together:

- Connect the `out` of the Sine node to the `left` input of AudioOut. 
- Connect the Const node to the `freq`  input of the Sine node.

Most nodes have connection points on their left and right sides. The left-side points are _inputs_ and the right-side ones are _outputs_

So far, so good but where is the sound? First we have to set the sine node to play a sound we can hear. 

- Click the "0" in the const node.
- Type "440"
- press Enter

Still no sound? Click "Play" and **slowly** turn your volume up a **little bit**. If you are using ear/headphones, put them near your ears before putting them all the way on to check that it's not too loud.

Now you should hear a nice smooth _sine tone_! Ooooooooooooo.

> Now try changing the frequency: type a different number into the const. What effect does this have on the sound?

Let's try some _other_ tone generators. The sine tone is a pure, smooth, sound, but these other generators have different timbres:

- Tri
- Saw
- Pulse
- Noise (this one doesn't have a `freq` input!)

> Can you describe the sound of these tone generators?

## Task 2: Changing Pitch and Volume

So far we've just made a sound constantly plays at *maximum volume**. Let's turn it down!

Create these nodes:

- Mul
- Knob

Disconnect any tone generators from the AudioOut then connect

- a tone generator node to the `in0` of the Mul node
- the Knob to the `in1` of the Mul node
- the `out` of the AudioOut to one (or both) of the inputs of the AudioOut node.

Press play and adjust the Knob to turn up the volume!

> "Mul" stands for "multiply", but why do we multiply things together to change the volume? (think about what happens when you multiply a number by zero...)

Now let's change pitch:

- Disconnect the Const from your tone generator.
- Create another Knob
- Connect the output of the Knob to the `freq` of the tone generator.
- Double click the knob (a little menu appears) and change `maxVal` to 1000.

Now you can turn the knob to select a frequency or pitch. 

> Can you work out the frequency of particular notes on your instrument or a piano?

## Task 3 - Playing Notes

Create **MidiIn** node: this lets you play your synthesiser with the keyboard of your computer. 

- Connect the `freq` output from the MidiIn node to the freq input of your tone generator (instead of the frequency Knob)
- press the letters "a" to "l" on your keyboard to play some notes!


## Task 4 - SEE the sound 

Create a **Scope** node. This visualises the signal of any output.

- connect the `out` of a tone generator to the input of the Scope.
- press some letters and you'll see the sound waves visualised in the Scope

The Scope is probably showing a very messy visualisation right now. Try connecting a _very low frequency_ tone to the Scope and you should be able to see more detail (e.g., 5Hz). If you try to visualise a very low frequency can you see why the tones have their names?

## Task 5 - Shaping Notes.

So far our notes have a kind of boring _shape_. That is, they are either **on** (playing) or **off**. Think about the _shape_ of sounds produced by other instruments, they might start quietly, get louder, and fade away over time.

The _shape_ of a note is called the _envelope_. It's the chunk of time that a note lives in with changes in volume and timbre of a sound over that time.

![We can change the amplitude over the [envelope](https://cs.anu.edu.au/courses/comp2300/lectures/digital-synthesis/#/amplitude-envelope) to give a note a sonic “shape”.](https://cs.anu.edu.au/courses/comp2300/assets/lectures/synth/envelope-sound.png)

So now we are going to create an envelope generator (EG) for our synth in NoiseCraft.

NoiseCraft has an EG node called **ADSR**. This creates envelope shapes in a particular 4-stage envelope which is popular for synthesisers:

![[ADSR](https://cs.anu.edu.au/courses/comp2300/lectures/digital-synthesis/#/adsr-envelope) stands for "attack", "decay", "sustain", "release". These are the four phases of a pitched note.](https://cs.anu.edu.au/courses/comp2300/assets/lectures/synth/adsr.png)

Create an **ADSR** node. An EG also creates signals but instead of listening to it, we use it to control other nodes. 

- Hook up the output of the ADSR node to the volume control **Mul** node of your synth.
- Hook up the `gate` input of the ADSR node to the `gate` output of your MidiIn** node
- Create four Knobs and hook them up to the `att`, `dec`, `sus`, and `real` inputs of the ADSR node.

Adjust the knobs: try setting attack to 0.2, decay to 0.4, sustain to 0.5 and release to 0.8.

Now if you play your synth with the keyboard you'll notice that it take a little bit of time for the notes to fade in when you press down a key, and to fade away when you lift your finger from the keyboard.

What kind of envelopes can you create with this setup? Can you mimic an acoustic instrument that you play?

## Task 6 - Additive Synthesis

So far we have only used a single simple tone generator to create sounds. These sound cool, but we haven't had any control over _timbre_, or sound colour, of the synthesiser except to change the basic waveform. 

Think: What does _timbre_ mean to you? How do you control timbre on your instrument?

In general, synthesisers use more complex techniques to control _timbre_ and create all kinds of interesting sounds. One simple way to do this is to take more than one tone generator and _add the sounds together_. This is called "additive synthesis".

- make another tone generator node (of the same or different type as one you already are using)
- create an **Add** node.
- hook up the outputs of both of your tone generators to the inputs of the **Add** node
- hook up the output of the **Add** node to the volume control/EG in your synth.

Now we need to control the frequency of our second tone generator.

- connect the `freq` output of the MidiIn node to the `freq` in of your second tone generator.
- Play some notes!

Now, this may sound a _bit_ different, but not very much so. This is because both tone generators are set to exactly the same frequency. Let's change that.

- Create a **Mul** node and a **Const** node. 
- Use these to multiply the `freq` output of the MidiIn node before sending it to your second tone generator.

Try some different numbers for multiplying the tone generators. Try some integers (e.g., 2, 3, 4) and some numbers with a decimal point (e.g., 1.4). 

What do these different additive sounds sound like? 

Can you create a perfect fifth between your tone generators?

One cool sound is to set the second tone generator very slightly out of tune with the first, e.g., set the Const node to `1.01`. Try it!

If you create a couple of tone generators, you can still add them together, but you might have to introduce some volume controls to mix their volumes together. Usually we would set the _lower_ tones to have a higher volume and the _higher_ tones are a bit quieter.

## Task 7 - Comparing to a famous synthesiser.

So what have we learned so far? Are we making a synth yet?

Let's compare our knowledge to the [Moog Minimoog Model D](https://www.moogmusic.com/products/minimoog-model-d), a very famous synth from the 1970s.

In fact, the Minimoog was so successful that it's design influenced many other synthesisers and there are recreations of the Minimoog in software and hardware (there's a [Behringer Model-D](https://www.bettermusic.com.au/behringer-model-d) over at Better Music if you want to have a look).

Find a picture of the Minimoog control panel and take a second to look carefully. There are a _lot_ of knobs, but your synth probably has a lot at this point to so that's nothing to be afraid of.

The Minimoog control panel is divided into sections from left to right:

- At the far left, there's a Controllers section which adjusts the input from a keyboard, similarly to your MidiIn node.

- The next section is the Oscillator Bank. An "oscillator" is just another name for a "tone generator".

- The Minimoog has three oscillators. You might be able to see a knob for setting the waveform shape of each one and a knob for setting the octave. Some synthesisers measure octaves in "feet" (as in the unit of length)---this is related to the measurements of organ pipes (believe it or not!) which get lower as they get longer. There are _two_ knobs for detuning the second and third oscillators against the first.

- Next we have a "mixer" section--just like your additive synth. There's also a mixer for "noise" and the signal from an external input.

- The next section is complicated with two parts stacked up. Looking at the bottom one first, this is called "Loudness Contour", which we call "Envelope Generator". It has three familiar labels: attack, decay, and sustain.

- The section above that is a _filter_ section, which has it's _own_ separate envelope. This is incredibly important, as it gives us a way to shape timbre over time, but we'll get to filters in the next task.

- The last section just has a power switch and a main volume knob.

So you now should have an idea of what MOST of the knobs on the Minimoog might do. Not so complicated after all huh?

## Task 8 - Filter

Have you noticed that some of the sounds from the tone generators are quite harsh? This is particularly the case for the _pulse_ and _sawtooth_ tones. These tone generators don't sounds like they are going to be very useful. Luckily, we have a sound design tool that can help control a harsh timbre and give us extra possible sound colours: a filter! Let's add one to our synth.

- make a **Filter** node and place it in between the tone generators and ADSR section in your synth signal chain.
- Make two knobs and connect one to the `cutoff` input and one to the `reso` input.
- Turn the `cutoff` knob to 1 and the `reso` knob to 0.

(NB: In the above, the _exact_ connections to make are left out, you should connect the `in` and `out` connectors so that the synth sound goes _through_ the filter).

Play some sounds on your synth and (simultaneously) try turning the `cutoff` knob down to 0. What difference does it make?

Turn the `reso` knob up to 0.8 and try the same thing. What happens now?

The _filter_ in NoiseCraft is actually a low-pass filter (LPF), it filters out higher frequency sound and lets lower frequency sound pass through[^A low-pass filter is one of the most used types of filters in electronic music. If someone says a synth has a "filter", it's probably a resonant LPF just like this one.]. In practice, it lets the _fundamental_ frequency through and removes some of the _overtones_. 

The `cutoff` knob controls the frequency where the filter "cuts off" higher sounds. The `reso` (resonance) knob emphasises the sound at the `cutoff` frequency. If you turn the resonance up quite high, you start to hear a kind of "ringing" as you move the cutoff frequency up and down.

> A low-pass filter is lot like the sound you get while singing and putting your hand over your mouth. Try it and see if you can get a similar effect to "cutoff" and "reso" by shaping you hand and mouth in different ways.

Well now you can tame those harsh synth sounds with a filter. To take your filtering a step further, we can change the `cutoff` frequency over time using an envelope generator.

- Make a new **ADSR** node, just like the one you made for volume and connect it to the `cutoff` input of your **Filter**.
- Connect the filter ADSR generator's `gate` input to the same `gate` output of your **MidiIn** or **MonoSeq** node that you are using for controlling pitch and rhythm.

Experiment with different envelope shapes for your filter. What sounds good to you?

One last thing: A low-pass filter _removes_ sound, so we often call synthesisers that use filters as their main way to shape sound _subtractive_ synths.

## Task 9 - Sequencer

Playing notes with the computer or MIDI keyboard with **MidiIn** in fun, but it's a slow way to compose a song. Many synthesisers are used with a _sequencer_ [^In fact, most synthesisers have some kind of sequencer built-in.]that can play back phrases of notes in a loop (repeated over and over) this lets musicians compose parts to songs, or create loop-based electronic  music.

NoiseCraft has a sequencer called **MonoSeq** that you can use to compose phrases. Let's try it out.

- Create a **MonoSeq** node and a **Clock** node.
- Connect the `freq` out of the **MonoSeq** to `freq` input of your tone generator(s) and the `gate` output to your envelope generator(s).
- Connect the **Clock**'s output to the `clock` input on the **MonoSeq**.

Now that everything is hooked up, press play and you'll hear... nothing! You need to enter in a sequence first. The **MonoSeq** node has a nice red grid that represents a musical phrase. Each column is a 16th note and each row represents a different pitch. Enter some notes and create a great melody!

Here's a few things to try:

- change tempo by adjusting your **Clock** node.
- change the scale or root pitch of your **MonoSeq** object
- experiment to figure out what the buttons on the **MonoSeq** do

## Tast 10: Compose some synth music

Now you have all the knowledge you need to create a short synthesiser composition. For this task you have to:

- create a synthesiser using knowledge from the earlier tasks. Your synthesiser should have at least two tone generators, a filter, and an envelope, but can have more.
- create at least one sequencer with a sequence containing your composition.
- include some "live" elements to your composition by planning to turn some knobs, or change your sequence(s) during your performance.
- perform your composition for the class.

When composing with synthesisers keep in mind that the sequence is only _one part_ of your composition. The timbre of your synthesiser can also be composed (we call this "sound design") and can be changed over time during your composition. Genres like techno are _mainly_ about changes in _timbre_ and _texture_ rather than melody.



## Finding out more

Well now you know a _lot_ about how a typical synthesiser works, and further, you know how to create one[^Pretty rad huh? How many other musical instruments do you know how to build?].

Having created all the synths in this tutorial, you might like to use the "Browse" feature in NoiseCraft to look at synthesisers that other people have created. Some of these are quite complicated, but they use all the same building blocks that we have discussed so you will be able to look at how the nodes are connected together and see how they work!

## Extra: Glossary

There are many technical terms in used in electronic music and sometimes multiple words for the same thing (sometimes different manufacturers use different terms for historical reasons). Here's a list of typical translations from the terminology used above to other terms that you might see.

- Tone Generator: Oscillator, Voltage Controlled Oscillator, VCO
- ADSR: Envelope Generator, EG, Slope Generator, Attack/Decay
- LFO: Low Frequency Oscillator
- LPF: Low-pass filter
- BPF: Band-pass filter
- HPF: High-pass filter

Music _does_ tend to have a lot of overlapping technical terms. Can you think of any other musical concepts that have multiple names? (Think about how you describe _fast_ in music, and the name for a note that goes for one beat of a bar).
