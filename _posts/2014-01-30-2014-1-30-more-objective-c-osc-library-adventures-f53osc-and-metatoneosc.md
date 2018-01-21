---
layout: post
title: 'More Objective C OSC Library Adventures: F53OSC and MetatoneOSC'
categories:
- note
tags:
- OSC
- Objective-C
- programming
- iOS
status: publish
type: post
published: true
meta: {}
---

I've previously written about my adventures in [finding a good OSC library](http://charlesmartin.com.au/blog/2013/3/26/finding-a-good-osc-library-for-ios) to use in iOS development. I found a new contender, [F53OSC](https://github.com/Figure53/F53OSC), yesterday that seemed to be a complete implementation of OSC 1.0 and doesn't require any XCode sub-projects (very annoying to setup when starting a new app).

Ideally for an OSC library, I should be able to drag a the folder of source files into my project and be ready to go.

After a bit of experimentation I updated the library to work with ARC and added a convenience method to make it easy to send OSC messages to different hosts. My forked library is called [MetatoneOSC](https://github.com/cpmpercussion/MetatoneOSC). The goal with this is to have the easiest to setup and use OSC library. The usage notes are below.

Super thanks to [Figure 53](http://figure53.com) for putting the library together.

## Usage

Just add the source files to a project and import F53OSC.h.

### Sending messages

    F53OSCClient *oscClient = [[F53OSCClient alloc] init];
    F53OSCMessage *message =
    [F53OSCMessage messageWithAddressPattern:@"/bla/bli/blo"
                                   arguments:@[@1,@"A string argument!",@5.82]];
    [oscClient sendPacket:message toHost:@"192.168.1.14" onPort:3000];'

### Receiving messages

Whatever object is receiving messages needs to be a

`<F53OSCPacketDestination data-preserve-html-node="true">` and implement the 
takeMessage method.

    F53OSCServer *oscServer = [[F53OSCServer alloc] init];
    [oscServer setPort:3000];
    [oscServer setDelegate:self];
    [oscServer startListening];
    
    - (void)takeMessage:(F53OSCMessage *)message {
        // This method is called whenever the oscServer receives a message.
        NSString *addressPattern = message.addressPattern;
        NSArray *arguments = message.arguments;
    }
