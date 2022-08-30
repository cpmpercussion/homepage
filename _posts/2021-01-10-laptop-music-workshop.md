---
layout: post
title: Laptop Music Coding with Gibber
date: 2021-01-10
categories:
    - workshop
    - class
tags:
    - gibber
    - computer-music
---

This is a _workshop_ designed for students who have never done any coding before to start by making some computer music! Here's the description:

> In this session you’ll try out some of the tools used in the [ANU Laptop Ensemble](https://comp.anu.edu.au/courses/laptop-ensemble) for making music with code and have a computer music jam with a group! We'll learn a bit about digital synthesis and algorithmic composition and how students in our laptop ensemble create new musical instruments using computing and creative skills.

(_updated: 6/7/2022_)

#  Making your Laptop into a Musical Instrument

{:.info-box}

Welcome to our Laptop Music workshop! In this session we will create some music with computers using a _live coding_ language called [gibber](https://gibber.cc). All you will need is a **computer**, a **web browser** (Chrome is preferred), and some **headphones**!

## Before we start

Here's the three things you'll need:

- **computer**: any normal laptop/desktop will be work fine, if you're on-campus the computer labs are already full of computers :-)

- **web browser**: musical websites tend to work best in **Chrome**, **Firefox**, and **Safari** in that order. If you're a fan of freedom, you might like to try [**Chromium**](https://www.chromium.org/), the free and open source version of Google's Chrome browser (Chromium and Firefox are available in the ANU labs). Unfortunately Gibber doesn't seem to work well on an iPad, and I haven't tried on a Chromebook yet.

- **headphones**: this is just to avoid annoying your neighbours but also music tends to sound _better_ with headphones. Note that we can't provide these in our labs, so **please bring some** with a normal headphone plug.

## Getting started with Gibber

If you're reading this, you're probably on a computer and have a browser window open -- that's an excellent start already!

Open a new tab or window and head over to [gibber.cc](https://gibber.cc). You'll see a stylish looking dark, artistic website. Click the link that says "playground". 

The first thing to do is to click anywhere in the main code window. The text will disappear and some example code will appear instead. Select all that code and delete it (just hit backspace); it's nice to start from a clean slate!

During this tutorial we're going to enter some code in this editing window, then **execute** it to make a sound. Let's start by typing in one simple line of code:
```
Synth().notef(440)
```
**Executing** this line of code means asking the computer to actually **do** what it says. In this case, it means "make a synth(esiser), and play a note at a frequency of 440 Hertz".

Use the arrow keys to place your cursor anywhere on the line with `Synth().notef(440)`, then hold the `Shift` key on your keyboard and press the `Enter` key to evaluate that line. You should hear a slightly annoying squawk!

You can keep holding `Shift` and tapping `Enter` to play lots of 440Hz notes! Yay music!

At this point you can play whatever note you want by entering in the correct
frequency. But perhaps this seems inconvenient; you might like to define notes
closer to how we read and write music. You actually have two options for
creating a sound:

```
Synth().notef(440)
Synth().note(0)
```
If you play each of these lines, you might notice that they are making the same
sound! That's ok, it's meant to happen. The second line is written slightly
differently (can you see how?) and it is defining a pitch as a note in a scale.
Try changing it to `Synth().note(1)` and play it again. Now it's different!

{:.info-box}
Gibber understands _scale degrees_ as the main way of representing pitches in sequences. A scale is a selection of pitches (usually 7 out of the 12 we usually have available in western music) that sound "good" together. Instead of writing "C" we could say "degree 0 of a C major scale". Gibber has lots of scales built-in (see the Scales tutorial in Gibber's menu), but you can get started by just using low numbers (e.g., 0-7) in your sequences. 


Before we move on, let's make some more notes. We can change the pitch (frequency) of the note by changing the number in between the parentheses. For example: `Synth().notef(567)` will produce a note at 567Hz. Try it out.

- If you press `Ctrl+Enter` (the control key and enter), instead of `Shift+Enter`, what happens?
- If Gibber is ever too loud or playing sounds you don't want, you can stop **everything** by hold the `Ctrl` key and press the full stop key (`.`).
- By the way, from now on we'll write the keyboard commands as `Ctrl+Enter` and `Ctrl+.`.


## Exercise 1: Make a note

So far we've made "sounds", but not exactly "music"

To play a song, we need multiple notes in a sequence, not just one at a time.

If you try executing `Synth()` you might find that it doesn't actually do anything. We have to make a synth, and then give it a note to play:
```
s = Synth()
s.note(0)
```
Try executing each line of code in succession. You should hear a sound start and then stop---that's a note! You can play it again by just executing the second line.

So what's going on here? Why do we need two lines of code? The first line of code creates a `Synth` which doesn't do anything until we ask it to play a note. Since we want to play lots of notes, we are going to keep this particular `Synth` around, so we will assign it to a variable called `s`.

The line of code `s = Synth()` creates a `Synth` and then saves it to `s` so we can use it multiple times.

The next line of code `s.note(0)` asks the Synth represented by `s` to play a note. The "dot" in between `s` and `note` is often used in programming to ask something to perform a certain action. 

You might notice there is a particular scale attached to the numbers. You can change the scale to the very familiar C major scale by running these lines of code:
```
Theory.root = 'c4'
Theory.mode = 'ionian'
```
And then running some more `s.note(0)` lines with different numbers.

{:.info-box}
If you want to learn more about Gibber after this tutorial, you can look select some example compositions from the drop down menu next to "gibber" in the top left, or click the "reference" link at the top right to read the documentation. 

Let's try a few experiments:

- Can you play a short tune by setting up some "note" commands, and executing them in order?
- If you happen to press `Ctrl-.` in between executing note commands, what happens?

## Exercise 2: Play a tune

Let's play a melody, or a **sequence** of notes:
```
s = Synth()
s.note.seq([0, 1, 2, 3, 4, 5], 1/4)
```
Execute these two lines of code and you should be able to hear a sequence of six notes.

Gibber's synth objects have a built-in sequencer, in this case, we're sequencing the `note` command, so we've put a `seq` command after that, and then the parameters of our sequence inside the parentheses. The parameters have two parts"
```
s.note.seq(
    [0, 1, 2, 3, 4, 5], // a list of pitches
    1/4 // a duration - one quarter of a bar (or a quarter note or crotchet).
)
```
You might be able to hear that the sequence is going through the list of pitches over and over again, and that the duration of each note is the same. In fact, you should also be able to see it becuase Gibber highlights your code to show you what's going on! So far so good!

It might seem strange that the sequence loops over and over instead of playing just once. Gibber is designed to create electronic music which is often based on _looping sequences_. So the idea that a sequence of notes loops (by default) is build deeply into it.

Let's try a few sequence experiments:

- try changing the duration from `1/4` to `1/8` or `1/16` and execute the sequence line again. What happens?

- try replacing the duration with a _list_ of durations (e.g, `[1/4, 1/8]`). What happens when the lists of durations and pitches are the different length?

- can you figure out a sequence to play a tune you know?

{:.info-box}
A few **sequence tips**: you can stop the sequence by executing `s.stop()`. Gibber has a built in metronome to keep everything in time (have a look at the animation in the top left corner), if you want a sequence to start right at the start of the next bar, use `Ctrl+Enter` to execute it (this works for executing any other command as well)

One more sequence trick before moving on! Let's try a _randomised_ sequence instead of going through the list of pitches in order by adding `.rnd()` to the list:
```
s.note.seq([0, 1, 2, 3, 4, 5].rnd(),1/4)
```
We can do this for the duration as well:
```
s.note.seq([0, 1, 2, 3, 4, 5], [1/4,1/8].rnd())
```

## Exercise 3: Groove with drums

Let's try some sequences with some of Gibber's drum synths. Here's a kick:
```
k = Kick()
k.notef.seq(75, 1/4)
```
You might notice that there's a very simple sequence here---just one pitch (75Hz) and a duration value---kick patterns can be simple!

And some hi-hats:
```
h = Hat()
h.trigger.seq(0.4,1/16)
```
Note that we are using `trigger.seq` with the hats, not `note.seq`. "Trigger" is useful when you don't want to change the pitch, the "0.4" in that code refers to the volume (between 0 and 1).


There's another (maybe simpler) way of make a drum pattern in Gibber:
```
d = Drums()
d.tidal('kd sd kd sd')
```
This synth includes four drum sounds: kick: `kd`, snare: `sd`, closed hat: `ch`, and open hat: `oh`.

This uses a style of pattern notation called `tidal` (after another live coding system, [tidal cycles](https://tidalcycles.org/)). You can easy make interestign patterns in a tidal sequence. E.g., to repeat a note two times, just add `*2` after it. So to do "we will rock you" you write:
```
d.tidal('kd sd kd*2 sd')
```
To play two sounds together, you put them in square brackets with a comma in between, e.g.: `[kd, ch]`. So we could have a complete beat like this:
```
d.tidal('[kd, ch] ch [sd, ch] ch [kd, ch] ch [sd, ch] oh')
```

- Try out some different combinations of repeated and simultaneous notes in a drum pattern.

- Try the `EDrums()` kit as well---these work the same way, but sound like a drum machine. You also get two extra sounds: clap `cp` and cowbell `cb`.


{:.info-box}
The `Drums` synth plays back sound files (samples). So it is actually a bit different than the `Kick` and `Hat` instruments we used above. Have a look in the [reference](https://gibber.cc/playground/docs/index.html#instruments-drums) to see how this works.

## Exercise 4: Time for techno

It's been said that the minimum you need to make techno is [drums, bass, a lead synth, and freaky noises](https://youtu.be/4jCCzpWBsFs?t=160). So let's get those things and make some [EDM](https://en.wikipedia.org/wiki/Electronic_dance_music).

We've already got drums, and your `Synth` sequences from Exercise 2 can be the lead, so let's get a bass sound:
```
b = FM('bass')
b.note.seq(-7, 1/16)
```
This code uses the `FM` synth, a classic synthesis design and a preset to make a nice bassy sound. Done!

Well, let's make that bass a _little_ bit interesting. The FM synth has a parameter called _index_ which we can sequence to change it's tone:
```
b.index.seq([2,3,4,5,6],1/16)
```
Now that sounds cool! Some things to try:

- Set up drums, bass, and lead parts playing a pattern together. Use `Ctrl+Enter` to make sure your sequences all line up.

- Once you have some patterns running, start making small changes to the sequences and executing them again---Now you're live coding!

- Try using `Rndi` in a note sequence to generate pitches randomly, e.g., `Rndi(0,7)` will generate random scale degrees from 0 to 7.

- Rather than setting the durations manually, try using the `Euclid` function. This generates [Euclidean rhythms](http://cgm.cs.mcgill.ca/~godfried/publications/banff.pdf)---even spacing of pulses in a bar that are algorithmically guaranteed to sound cool! You use this function with two numbers, e.g., `Euclid(3,8)` will generate three notes in a bar evenly divided into 8 parts.

Combining the last two ideas, you could set up a sequence like this:
```
s.note.seq(Rndi(0,7), Euclid(7,16))
```

- What about the freaky noises? Maybe you could try another synth from the [Gibber manual](https://gibber.cc/playground/docs/index.html#instruments).

## Here's one I made earlier

Well, here's some techno I made a bit earlier. You could try this as a starting point for your own work or just look to see how some other modulations might work! (There's a few things below that aren't covered above!)

```
Clock.bpm = 120
Theory.root = 'c4'
Theory.mode = 'aeolian'

s = Synth("bleep").fx.add(Reverb())
s.note.seq(sine(btof(7.6),7,0), Euclid(5,16))

s.stop()

k = Kick()
k.notef.seq(70, 1/4)

k.stop()

h = Hat()
h.trigger.seq(sine(3,0.6,0.05), [1/16,1/8].rnd())
h.tune.seq(Rndf(0.5,0.7), 1/16)

h.stop()

c = Clave().fx.add(Reverb())
c.trigger.seq(sine(0.2,.1,.4), Euclid(6,16))
c.note.seq(sine(5.01,4,5), Euclid(6,16))

c.stop()

cl = Clap().fx.add(Reverb())
cl.trigger.seq(0.6,1,0,1/4)

b = FM('bass')
b.note.seq(-7,1/16)
b.index.seq([2,3,4,5,6],1/16)
```

{:.info}
One last key command: `Alt-Enter` will execute _multiple_ lines of code at once as long as they don't have empty lines in between. This can be handy for triggering a couple of musical actions to start at the same time.

## This is just the start!

There's a lot to learn about Gibber, synthesis, live coding, music tech, and computing! Don't worry if this seems overwhelming. A good start for today is to make some sounds and try changing them a bit in Gibber!

{% comment %}
// Comment from Charlie about how to make random pattern filter work with durations

syn = Synth('square.perc')
  
syn.note.seq( [0,1,2,3], ptrn=[1/4,1/8,1/16] )

ptrn.addFilter( (args, __ptrn) => {
  args[2] = Math.floor( Math.random() * __ptrn.values.length )
  args[0] = Clock.time(__ptrn.values[ args[2] ])
  
  return args
})

{% endcomment %}
