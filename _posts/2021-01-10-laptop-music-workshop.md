---
layout: post
title: Laptop Music Coding Workshop
date: 2021-01-10
---

This is a _workshop_ designed for students visiting the Australian National University in January 2021!

## Intro

In this session you’ll try out some of the tools used in the ANU Laptop Ensemble for making music with code and have a computer music jam with a group! We'll learn a bit about digital synthesis and algorithmic composition and how students in our laptop ensemble create new musical instruments using computing and creative skills.

# Making your Laptop into a Musical Instrument

{:.info-box}

Welcome to our Laptop Music workshop! In this session we will create some music with computers using a _live coding_ language called [gibber](https://gibber.cc). All you will need is a **computer**, a **web browser** (Chrome, Firefox or Safari are preferred), and some **headphones**!

## Before we start

This workshop has two versions: on-campus at the Australian National University in our School of Computing labs, and remote, through a Zoom session.

Here's the three things you'll need:

- **computer**: any normal laptop/desktop will be work fine, if you're on-campus the computer labs are already full of computers :-)

- **web browser**: musical websites tend to work best in **Chrome**, **Firefox**, and **Safari** in that order. If you're a fan of freedom, you might like to try [**Chromium**](https://www.chromium.org/), the free and open source version of Google's Chrome browser (Chromium and Firefox are available in the ANU labs). Unfortunately Gibber doesn't seem to work well on an iPad, and I haven't tried on a Chromebook yet.

- **headphones**: this is just to avoid annoying your neighbours but also music tends to sound _better_ with headphones. Note that we can't provide these in our labs, so **please bring some** with a normal headphone plug.

## Getting started with Gibber

If you're reading this, you're probably on a computer and have a browser window open -- that's an excellent start already!

Open a new tab or window and head over to [gibber.cc](https://gibber.cc). You'll see a stylish looking black screen with a couple of frames.

The first thing to do is click the "close welcome" button in the right hand frame. Then you'll get a code editing frame with some example code in it already. Select all that code and delete it (just hit backspace); it's nice to start from a clean slate!

During this tutorial we're going to enter some code in this editing window, then **execute** it to make a sound. Let's start by typing in one simple line of code:
```
Sine()
```
**Executing** this line of code means asking the computer to actually **do** what it says. In this case, it means "play a [sine tone](https://en.wikipedia.org/wiki/Sine_wave) at a (default) frequency of 440 Hertz".

Use the arrow keys to place your cursor anywhere on the line with `Sine()`, then hold the `Ctrl` key on your keyboard and press the `Enter` key to evaluate that line. You should hear a smooth (but slightly annoying) sound.

To **stop** playing the sine tone, hold the `Ctrl` key and press the full stop key (`.`). That's how you stop all sounds in Gibber.

By the way, from now on we'll write those keyboard commands as `Ctrl+Enter` and `Ctrl+.`.

{:.info-box}
Just a quick note before we go too much further, if you want to learn more about Gibber after this tutorial, you can look under the "tutorials" option in the left-hand browser pane. You can also look at the Gibber [manual](https://bigbadotis.gitbooks.io/gibber-user-manual/content/).
If you end up wanting to save your work in Gibber, you can either copy you code into a document (or email it yourself), or make a user account at [gibber.cc](https://gibber.cc) and then you'll be able to save code and access it under the browser pane.

Before we move on, let's make some more sine tones. We can change the pitch (frequency) of the sine tone by adding a number in between the parentheses. For example: `Sine(567)` will produce a sine tone at 567Hz. Try a few experiments with sine tones:

- If you execute a `Sine()` command, change the frequency in that line of code, and execute it again, what happens?
- If you have multiple sine tones playing and you hit `Ctrl+.`, what happens?

## Exercise 1: Make a note

So far we've made "sounds", but not exactly "music"

Our sine tones played forever, but musical _notes_ tend to start, go for certain amount of time, and then stop (i.e., they have a **duration**).

We can make some notes in Gibber, but not with the `Sine` command. This time let's try the `Synth` command.

If you try executing `Synth()` you might find that it doesn't actually do anything. We have to make a synth, and then give it a note to play:
```
s = Synth()
s.note('c4')
```
Try executing each line of code in succession. You should hear a sound start and then stop---that's a note! You can play it again by just executing the second line (and there's no need to hit `Ctrl+.` this time).

You can try putting other pitch names into the `s.note()` line to play different pitches. You can use the musical note names, e.g., `d`, `g`, `a#` (a sharp), and `eb` (e flat). The number represents the [octave](https://en.wikipedia.org/wiki/Octave) of the note, so `c5` is one octave above `c4`.

So what's going on here? Why do we need two lines of code? The first line of code creates a `Synth` which doesn't do anything until we ask it to play a note. Since we want to play lots of notes, we are going to keep this particular `Synth` around, so we will assign it to a variable called `s`.

The line of code `s = Synth()` creates a `Synth` and then saves it to `s` so we can use it multiple times.

The next line of code `s.note('c4')` asks the Synth represented by `s` to play a note. The "dot" in between `s` and `note` is often used in programming to ask something to perform a certain action. 

{:.info-box}
You can also send note commands with frequencies instead of note names, e.g., `s.note('660')`

Let's try a few experiments:

- Can you play a short tune by setting up some "note" commands, and executing them in order?
- If you happen to press `Ctrl-.` in between executing note commands, what happens?

## Exercise 2: Play a tune

Let's play a melody, or a **sequence** of notes:
```
s = Synth()
s.note.seq(['a3','b3','c3','d3','e3','g3'],1/4)
```
Execute these two lines of code and you should be able to hear a sequence of six notes.

Gibber's synth objects have a built-in sequencer, in this case, we're sequencing the `note` command, so we've put a `seq` command after that, and then the parameters of our sequence inside the parentheses. The parameters have two parts"
```
s.note.seq(
    ['a3','b3','c3','d3','e3','g3'], // a list of pitches
    1/4 // a duration - one quarter of a bar (or a quarter note or crotchet).
)
```
You might be able to hear that the sequence is going through the list of pitches over and over again, and that the duration of each note is the same. So far so good!

Let's try a few sequence experiments:

- try changing the duration from `1/4` to `1/8` or `1/16` and execute the sequence line again. What happens?

- try replacing the duration with a _list_ of durations (e.g, `[1/4, 1/8]`). What happens when the lists of durations and pitches are the different length?

- can you figure out a sequence to play a tune you know?

{:.info-box}
A few sequence tips: you can stop the sequence by executing `s.note.seq.stop()`. Gibber has a built in metronome to keep everything in time (have a look at the animation in the top left corner), if you want a sequence to start right at the start of the next bar, use `Shift+Ctrl+Enter` to execute it (this works for executing any other command as well)

One more sequence trick before moving on! Let's try a _randomised_ sequence instead of going through the list of pitches in order by adding `.rnd()` to the list:
```
s.note.seq(['a3','b3','c3','d3','e3','g3'].rnd(),1/4)
```
We can do this for the duration as well:
```
s.note.seq(['a3','b3','c3','d3','e3','g3'],[1/4,1/8].rnd())
```

## Exercise 3: Groove with drums

Let's try some sequences with some of Gibber's drum synths. Here's a kick:
```
k = Kick()
k.note.seq(90, 1/4)
```
You might notice that there's a very simple sequence here---just one pitch and duration value---kick patterns can be simple!

And some hi-hats:
```
h = Hat()
h.note.seq(Rndi(1000,5000),1/16)
```
This sequence has a different way of achieving a randomised sound. The `Rndi` command generates a random number between 1000 and 5000, which gives us a continuously changing pitch for the hats.

There's another (maybe simpler) way of make a drum pattern in Gibber:
```
d = Drums('x*o*x*o-')
```
This synth includes four drum sounds (kick, snare, closed hat, open hat) and you can define a little sequence using the letters `x`, `o`, `*`, and `-`.

{:.info-box}
The `Drums` synth plays back recordings of  is actually a bit different than the `Kick` and `Hat`

Have a look in the [reference](https://gibber.cc/docs/index.html#audio-drums-percussion) to see how this works.

## Exercise 4: Time for techno

It's been said that the minimum you need to make techno is [drums, bass, a lead synth, and freaky noises](https://youtu.be/4jCCzpWBsFs?t=160). So let's get those things and make some [EDM](https://en.wikipedia.org/wiki/Electronic_dance_music).

We've already got drums, and your `Synth` sequences from Exercise 2 can be the lead, so let's get a bass sound:
```
b = FM('bass')
b.note.seq('c2', 1/16)
```
This code uses the `FM` synth, a classic synthesis design and a preset to make a nice bassy sound. Done!

Well, let's make that bass a _little_ bit interesting. The FM synth has a parameter called _index_ which we can sequence to change it's tone:
```
b.index.seq([2,3,4,5,6],1/16)
```
Now that sounds cool! Some things to try:

- Set up drums, bass, and lead parts playing a pattern together. You might want to use `Shift+Ctrl+Enter` to make sure your sequences all line up.

- Once you have some patterns running, start making small changes to the sequences and executing them again---Now you're live coding!

- Try changing your sequences from named pitches to _scale degrees_ (see info box below) by putting some low numbers (e.g., 0-7) in a sequence instead of the pitch names. This can make it a lot easier to create patterns that sound nice together.

- What about the freaky noises? Maybe you could try another synth from the [Gibber manual](https://bigbadotis.gitbooks.io/gibber-user-manual/content/chapters/audio_synthesizers.html)

{:.info}
Gibber can understand _scale degrees_ as another way of representing pitches in sequences. A scale is a selection of pitches (usually 7 out of the 12 we usually have available in western music) that sound "good" together. Instead of writing "C" we could say "degree 0 of a C major scale". Gibber has lots of scales built-in (see the Scales tutorial in Gibber's left hand pane), but you can get started by just using low numbers (e.g., 0-7) in your sequences. If you change all your sequences to use this notation, they'll all be in the same key and probably sound good together!

## Here's one I made earlier

Well, here's some techno I made a bit earlier. You could try this as a starting point for your own work or just look to see how some other modulations might work! (There's a few things below that aren't covered above!)

```
s = Synth2({attack: ms(1)})
  .fx.add(Reverb())

s.note.seq( 
  [0,1,2,4,5,7],
  [1/4,1/8,1/16].random() 
)

s.note.values.shuffle()
s.cutoff.seq( [.1,.2,.3,.4], 1/2 )
s.cutoff = Add(.4, Sine(.05, .25)._ ) // LFO
s.resonance = 4
s.note.seq.stop()

k = Kick()
k.note.seq(90, 1/4)

k.note.seq.stop()

h = Hat()
h.note.seq(Rndi(1000,5000),1/16)

c = Clave().fx.add(Reverb())
c.note.seq(Rndf(7000,8000),[1/16,1/8].random())

c.note.seq.stop()

b = FM( 'bass') //, {decay: ms(200)} )
b.note.seq(0, 1/16)
b.index.seq([2,3,4,5,6],1/16)
b.pan.seq([-0.5,0,0.5].random(),[1/8].rnd())
```

{:.info}
One last key command: `Alt-Enter` will execute _multiple_ lines of code at once as long as they don't have empty lines in between. This can be handy to 

## This is just the start!

There's a lot to learn about Gibber, synthesis, live coding, music tech, and computing! Don't worry if this seems overwhelming. A good start for today is to make some sounds and try changing them a bit in Gibber!
