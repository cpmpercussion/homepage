---
layout: post
title: Getting the size of an array in libpd
categories: []
tags: []
status: publish
type: post
published: true
---

I really enjoy using libpd to embed interactive sound into [iOS apps](http://charlesmartin.com.au/apps). One tradeoff of doing this is that [Pd externals are often GPL licenced](https://github.com/libpd/libpd/wiki/misc#using-externals) so you can't use them in projects that are destined for the App Store - in particular, you can't use expr or expr~ which are very widely used objects included in Pd Vanilla.

As it turns out, expr is the only way to get the size of an array (or table) in Pd Vanilla, which can cause... difficulty.

The best way around this is to use the ["arraysize" external](http://puredata.info/downloads/arraysize) that is included with Pd-Extended and doesn't have a prescriptive licence.

Just copy the arraysize.c into an Xcode project that uses libpd and make sure that this file has the compiler flags "-DPD" in the Build Phases screen. Then setup a dummy method in the class where you setup libpd:

    void arraysize_setup();

and then call the setup method after initialising the PdAudioController, but before opening a patch file with PdBase like so:

    arraysize_setup();

Now go find the size of some arrays.
