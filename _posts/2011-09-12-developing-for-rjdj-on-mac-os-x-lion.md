---
layout: post
title: Developing for RjDj on Mac OS X Lion
categories:
- news
tags:
- development
- rjdj
status: publish
type: post
published: true
meta: {}
---

update the developer tools from [rjdj.me](http://rjdj.me) have been updated for lion now.

So I got back to developing some RjDJ with my new MacBook Pro which (naturally) runs lion. But! The development tools don’t work anymore.

To run the rjzserver from the command line, you need to install wxpython from their website

    http://www.wxpython.org/download.php

Then install mako templates:

    sudo easy_install mako

Now you need to run this line instructs Python to run in 32 bit mode.

    defaults write com.apple.versioner.python Prefer-32-Bit -bool yes

And then you can run rjzserver:

    python rjzserver.py