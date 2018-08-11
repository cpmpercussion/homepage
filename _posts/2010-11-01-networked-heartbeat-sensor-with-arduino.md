---
layout: post
title: Networked Heartbeat Sensor with Arduino!
categories:
- essay
tags:
- Arduino
- performance
- last man to die
- heartbeat
- network
- sensor
status: publish
type: post
published: true
meta: {}
---

![]({{ site.baseurl }}/squarespace_images/500bb0b2e4b042ea6e35b13f_512574c0e4b0887e852129d2_1361409217964_interaction1-the+heartbeat+sensor.jpg)
  


This project was my first foray in the exciting world of 
bio-sensors! A few years ago I started a multimedia performance group called 
[Last Man to Die](http://www.lastmantodie.net), I knew that I wanted to hook our bodies up to computers to affect musical and visual aspects of performance. The first way to do this I thought of was a 
heartbeat sensor! A little bit of research showed that there were cheap and easy ways to build a heartbeat sensor that could connect to an Arduino, but there were a few hurdles I had to work out before it was ready for performance!


In this post I'm going to explain how to build the sensor and show you an Arduino program that sends a serial message to the computer every time it detects a heartbeat. I'll also show you how to use the Arduino Ethernet Shield to send heartbeat messages over a network or the internet! (awesome.)


The sensor uses two simple components, an IR LED and an IR phototransistor. Both components are powered by the Arduino's 5V output and one analogue input reads the voltage across the phototransistor.


##Building the heartbeat sensor circuit:



The sensor only uses four inexpensive parts!


*IR LED


*IR Phototransistor
(these two come together at Littlebird as 
[IR Emitters and Detectors](http://www.littlebirdelectronics.com/products/Infrared-Emitters-and-Detectors.html))


*10KOhm resistor (
[Little Bird link](http://www.littlebirdelectronics.com/products/Resistor-10k-Ohm-1%7B47%7D6th-Watt-PTH.html))


*220Ohm resistor (comes in the  
[Resistor Kit](http://www.littlebirdelectronics.com/products/Resistor-Kit-%252d-1%7B47%7D4W.html) at Little Bird)


Of course, you also need an Arduino (from  
[Little Bird](http://www.littlebirdelectronics.com/products/Arduino-Uno.html)).
  
       
![The heartbeat sensor circuit diagram.]({{ site.baseurl }}/squarespace_images/500bb0b2e4b042ea6e35b13f_512574e2e4b0d69820155bdf_1361409250989_interaction2+-+ArduinoHeartbeatSensor-Circuit-Diagram1.jpg) The heartbeat sensor circuit diagram. 
  


###Here's the circuit diagram:



The simple circuit is the
same as for an IR range sensor, commonly used in robot projects. As a rangefinder, the IR phototransistor measures brightness light reflected back from distant objects but in our sensor, it will measure the brightness of the IR light going 
through your skin.


The idea is that when your heart beats you have a quick rush of blood into tiny blood vessels close to your skin which makes it less transparent. This effect is easiest to observe on your finger tips or earlobe. So the IR emitter and phototransistor are placed next to each other (not much light goes through the side of the emitter!) and you put your finger on top. Light from the IR emitter illuminates your skin and so passes into the phototransistor.


The phototransistor is connected to the Arduino in a similar way to a potentiometer. One lead is connected to +5V and the other to ground. The +5V lead is also connected to an analogue input on the Arduino. When the phototransistor receives more IR light it becomes more resistive and a lower voltage is detected by the analogue input.


Here's a picture of my test circuit on a breadboard, note that my IR receiver and emitter look like regular round LEDs so I set them up so that the lenses were adjacent and both pointing up. Different types of IR receivers/emitters look different, check the data sheet to see where the IR light enters/exits.
  
       
![Arduino and the sensor circuit. My phone camera can see in infrared.]({{ site.baseurl }}/squarespace_images/500bb0b2e4b042ea6e35b13f_512575d0e4b0a141fc6b4e36_1361409489717_interaction3-heartbeatSensorTestCircuit.jpg) Arduino and the sensor circuit. My phone camera can see in infrared. 
  


  
       
![Raw data from the heartbeat senso. Each little bump is a heartbeat!]({{ site.baseurl }}/squarespace_images/500bb0b2e4b042ea6e35b13f_512575f3e4b0e3d521c36920_1361409524098_interaction4-Arduino-HeartbeatData.png) Raw data from the heartbeat senso. Each little bump is a heartbeat! 
  


Time to test! I wanted to view the raw data from the IR detector to prove to myself that it really could detect my heartbeat, so I loaded up the 
[Arduino Graph tutorial](http://www.arduino.cc/en/Tutorial/Graph) to graph the data in Processing. After a bit of fiddling holding my finger on the lenses, the data looked like this:


To finish the circuit, I soldered it in free form style since I wanted it to be as small as possible, I used some foam tape to separate the detector and emitter leaving just the lens visible and held it together with electrical tape.

![]({{ site.baseurl }}/squarespace_images/500bb0b2e4b042ea6e35b13f_5125764be4b0e3d521c369ef_1361409616599_interaction5+-+Finished+heartbeat+sensor+1.jpg)
  

  
   
![]({{ site.baseurl }}/squarespace_images/500bb0b2e4b042ea6e35b13f_5125764de4b0d698201565d0_1361409621022_interaction6+-+Finished+heartbeat+sensor+2.jpg)

##Programming



When you watch a graph of the IR detector in Processing, it's obvious where the heartbeats are, just a little bump right? But how to do you get the Arduino to detect each bump?


Similar projects around the internet have used an amplifier to boost the signal from the phototransistor, I found that the data was clear enough for the Arduino to track heartbeats accurately. My Arduino program follows the (average) rate of change of the phototransistor voltage and uses this to judge whether a heartbeat is occurring or not.


Here's the Arduino code, it prints an estimate of your current heart rate to serial each time it detects a heartbeat.


###Arduino Code



// Pins
const int ledPin = 13;
const int sensePin = 0;
// LED blink variables
int ledState = LOW;
long ledOnMillis = 0;
long ledOnInterval = 50;

// Hearbeat detect variables
int newHeartReading = 0;
int lastHeartReading = 0;
int Delta = 0;
int recentReadings[8] = {0,0,0,0,0,0,0,0};
int historySize = 8;
int recentTotal = 0;
int readingsIndex = 0;
boolean highChange = false;
int totalThreshold = 2;

// Heartbeat Timing
long lastHeartbeatTime = 0;
long debounceDelay = 150;
int currentHeartrate = 0;

void setup() {
    // initialize the serial communication:
    Serial.begin(9600);
    // initialize the digital pin as an output:
    pinMode(ledPin, OUTPUT); 
}

void loop() {
    // Turn off LED
    digitalWrite(ledPin, LOW);

    // Read analogue pin.
    newHeartReading = analogRead(sensePin);
    //Serial.println(newHeartReading);
    //Calculate Delta
    Delta = newHeartReading - lastHeartReading;
    lastHeartReading = newHeartReading;

    // Find new recent total
    recentTotal = recentTotal - recentReadings[readingsIndex] + Delta;
    // replace indexed recent value
    recentReadings[readingsIndex] = Delta;
    // increment index
    readingsIndex = (readingsIndex + 1) % historySize;

    //Debug
    //Serial.println(recentTotal);

    // Decide whether to start an LED Blink.
    if (recentTotal >= totalThreshold) {
        // Possible heartbeart, check time
        if (millis() - lastHeartbeatTime >= debounceDelay) {
            // Heartbeat
            digitalWrite(ledPin, HIGH);
            currentHeartrate = 60000 / (millis() - lastHeartbeatTime);
            lastHeartbeatTime = millis();
            // Print Results
            //Serial.println("Beat");
            if (currentHeartrate <= 200) { 
                Serial.println(currentHeartrate); 
            } 
        } 
    } 
    delay(10); 
}


I wanted to use the sensor with SuperCollider, a music programming language. As a proof of concept, I've connected the Arduino to SuperCollider via a Processing script that translates serial data from the Arduino into OSC messages. Here's a video demonstration and the processing and supercollider code is below!
 
   

 

###Processing code:



// Based on examples from Arduino's Graphing Tutorial and OscP5 documentation
import processing.serial.*;
Serial myPort; // The serial port
int xPos = 1; // horizontal position of the graph
import oscP5.*;
import netP5.*;
OscP5 oscP5;
NetAddress myRemoteLocation;
void setup () {
    // set the window size:
    size(640, 480); 
    frameRate(25);
    // Start OscP5
    oscP5 = new OscP5(this,12000);

    // List availabl serial ports.
    println(Serial.list());

    // Setup which serial port to use. 
    // This line might change for different computers.
    myPort = new Serial(this, Serial.list()[0], 9600);

    myPort.bufferUntil('\n');
    // Configure NetAddress to send OSC messages to
    myRemoteLocation = new NetAddress("127.0.0.1",57120);
    // set inital background:
    background(0);
}

void draw () {
}

void serialEvent (Serial myPort) {
    // read the string from the serial port.
    String inString = myPort.readStringUntil('\n');

    if (inString != null) {
        // trim off any whitespace:
        inString = trim(inString);
        // convert to an int
        println(inString); 
        int currentHeartrate = int(inString);

        if (currentHeartrate > 0) {
            // Construct and send OSC message of the current    heartrate   
            OscMessage myMessage = new OscMessage("/heartbeat");
            myMessage.add(currentHeartrate);
            oscP5.send(myMessage, myRemoteLocation);

            // draw the Heartrate BPM Graph.
            float heartrateHeight = map(currentHeartrate, 0, 200, 0, height);
            stroke(127,34,255);
            line(xPos, height, xPos, height - heartrateHeight);
            // at the edge of the screen, go back to the beginning:
            if (xPos >= width) {
                xPos = 0;
                background(0); 
            } else {
                // increment the horizontal position:
                xPos++;
            }
        } 
    }   
}

/* incoming osc message are forwarded to the oscEvent method. */
void oscEvent(OscMessage theOscMessage) {
    /* print the address pattern and the typetag of the received OscMessage */
    print("### received an osc message.");
    print(" addrpattern: "+theOscMessage.addrPattern());
    println(" typetag: "+theOscMessage.typetag());
}


###SuperCollider Code:



// create the OSCresponder
// Beeps each time it receives a heartbeat OSC message.
(
    n = NetAddr.new("127.0.0.1", nil);
    o = OSCresponder.new(n, "/heartbeat", { 
        arg time, resp, msg; 
    msg.postln; 
    { EnvGen.kr(Env.perc, 1.0, doneAction: 2) * 
            SinOsc.ar([440,440], 0, 0.1) }.play;
    } ).add;
)
o.remove; // remove the OSCresponder.


##Networking!



Everything is more fun when it's connected to a network!


I wanted my heartbeat sensor to be network-enabled so that it works autonomously (i.e. not tethered to a computer by USB) and can send the heartbeat signals to multiple computers simultaneously. With the magic of the 
[Arduino Ethernet Shield](http://www.littlebirdelectronics.com/products/Arduino-Ethernet-Shield.html) (or this cheaper 
[clone](http://www.littlebirdelectronics.com/products/Arduino-Ethernet-Shield-W5100.html)) this is totally possible! 


All you have to do is plug the Ethernet Shield into the top of the Arduino, load up the Ethernet Library, and you're ready to go. I wanted to send messages using the OSC protocol, so I also loaded Recotana's 
[OSC library for Arduino](http://recotana.com/recotanablog/?page_id=222).


###Here's the code if you want to try this out:



// cpm_heartbeatEthernet
// Version 1.0 October 2009.
// Copyright Charles Martin (http://www.charlesmartin.com.au).
// Uses recotana's OSCClass (http://www.recotana.com)
// Detect heartbeat using a light reading through skin  
// On each beat, send an OSC message of the instantaneous 
// heartrate.

#include "Ethernet.h"
#include "OSCClass.h"

// Pins
const int ledPin = 13;
const int sensePin = 0;

// LED blink variables
int ledState = LOW;
long ledOnMillis = 0;
long ledOnInterval = 50;

// Hearbeat detect variables
int newHeartReading = 0;
int lastHeartReading = 0;
int Delta = 0;
int recentReadings[8] = {0,0,0,0,0,0,0,0};
int historySize = 8;
int recentTotal = 0;
int readingsIndex = 0;
boolean highChange = false;
int totalThreshold = 2;

// Heartbeat Timing
long lastHeartbeatTime = 0;
long debounceDelay = 150;
int currentHeartrate = 0;

// Ethernet and OSC information
byte serverMac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
byte serverIp[] = { 192, 168, 0, 99 };
int serverPort = 10000;
// byte gateway[] = { 192, 168, 0, 1 };
// byte subnet[] = { 255, 255, 255, 0 };
byte destIp[] = {192,168,0,255};
int destPort = 3333;
char *topAddress="/heartbeat";
OSCMessage recMes;
OSCMessage sendMes; 
OSCClass osc(&recMes);

void setup() {
    Ethernet.begin(serverMac ,serverIp);
    osc.begin(serverPort);
    osc.flush(); 
    sendMes.setIp( destIp );
    sendMes.setPort( destPort );
    sendMes.setTopAddress(topAddress);
    // initialize the serial communication:
    Serial.begin(9600);
    // initialize the digital pin as an output:
    pinMode(ledPin, OUTPUT); 
}

void loop() {
    // Turn off LED
    digitalWrite(ledPin, LOW);

    // Read analogue pin.
    newHeartReading = analogRead(sensePin);
    //Serial.println(newHeartReading);
    //Calculate Delta
    Delta = newHeartReading - lastHeartReading;
    lastHeartReading = newHeartReading;

    // Find new recent total
    recentTotal = recentTotal - recentReadings[readingsIndex] + Delta;
    // replace indexed recent value
    recentReadings[readingsIndex] = Delta;
    // increment index
    readingsIndex = (readingsIndex + 1) % historySize;

    //Debug
    //Serial.println(recentTotal);

    // Decide whether to start an LED Blink.
    if (recentTotal >= totalThreshold) {
        // Possible heartbeart, check time
        if (millis() - lastHeartbeatTime >= debounceDelay) {
            // Heartbeat
            digitalWrite(ledPin, HIGH);
            currentHeartrate = 60000 / (millis() - lastHeartbeatTime);
            lastHeartbeatTime = millis();
            // Print Results
            //Serial.println("Beat");
            if (currentHeartrate <= 200)        { 
                Serial.println(currentHeartrate); // Send a serial message  
                sendMes.setArgs("i" , &currentHeartrate); // Setup an OSC message 
                osc.sendOsc( &sendMes ); // Send the heartbeat OSC message 
            } 
        } 
    } 
    delay(10); 
}


I wrapped the final result up in a crazy plastic box, so the audience can see the blinky lights and know that it's a 
real thing and not a prop. Here's a photo from a rehearsal using the sensor:
  
      
![]({{ site.baseurl }}/squarespace_images/500bb0b2e4b042ea6e35b13f_512576bbe4b01b12552d255a_1361409725561_interaction+7+-+Arduino_Heartbeat_Sensor_in_Action.jpg)
  


PS, I used this project with this group: 
[Last Man to Die](http://www.lastmantodie.net)


PPS, this project was in an article on Makezine 
[here](http://blog.makezine.com/archive/2009/10/sending_a_hearbeat_over_ethernet.html)!


PPPS, I got the idea from Recotana's 
[Heartbeat Midi Controller](http://www.flickr.com/photos/recotana/2283817820/in/pool-make). Recotana also wrote the 
[OSC library for Arduino](http://recotana.com/recotanablog/?page_id=222) which enabled this project.
