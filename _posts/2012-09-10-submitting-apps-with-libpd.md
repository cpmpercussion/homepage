---
layout: post
title: Submitting iOS apps with libpd
categories:
- note
tags:
- XCode
- programming
- iOS
- libpd
status: publish
type: post
published: true
meta: {}
description: "2014-10-02 - added some updates for XCode 6 So I've been working on submitting my Snow Music iOS app to app store, but was frustrated at the final step"
---

**2014-10-02 - added some updates for XCode 6**

So I've been working on submitting my Snow Music iOS app to app store, but was frustrated at the final step: archiving and verifying the app.

The problem was that my app uses [libpd](http://libpd.cc), a static library. The app was compiling perfectly well and XCode could install it on my devices, but when archiving the app to verify and upload it for review the verification would fail since:

>"Snow Music does not contain a single-bundle application or contains multiple products. Please select another archive, or adjust your scheme to create a single-bundle application."

It turns out that this is just a confusing situation for using static libraries in XCode and not a problem with libpd. I found a straightforward explanation on Aaron Douglas' site to solve his problem with another static library. The solution was as follows (adapted from Aaron's instructions):

* Select the libpd project, a subproject of the App's project.
* In Build Settings for the libpd project, set "Skip Install" to "Yes". (you need to have selected "All" build settings, not just "Basic").
* In Build Settings for the target "libpd-ios", set "Skip Install" to "Yes".
* In Build Phases for the target "libpd-ios" look under Headers and drag all of the files listed under Public and Private to the Project area.

Anyway, the project has archived, verified and uploaded correctly so now I'm just waiting for review!

**PS: two years later lots of people still find this post useful! Including me!**
