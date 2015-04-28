# Color_Lamp
A web-connected lamp whose base changes colors to display a live data feed. I am recording my development progress using MIT's awesome tool, Build In Progress. [Follow along on the Color Lamp page!] (http://buildinprogress.media.mit.edu/projects/2225/steps)

## Hardware
I am using a BeagleBone Black to control the lamp. But, the code is Python2, so if you can run Python and have decent PWM capabilities, then this code is for you!

## Interface
You can communicate to the BeagleBone Black with simple JSON HTTP posts.

## Tasks in progress
### Twitter data feed
I am using the Twitter Sentiment Analysis tool from [Datumbox] (http://www.datumbox.com/) as the first source of live data. You give it a topic, it controls the lamp according to the current mood of Twitter on that topic. Application coming soon (in Python).
### Stress sensor
The final goal is to control the lamp with heart-rate/stress sensor data from a wearable device. Fitbit will have a new API for their heartrate soon. Or, perhaps I could convince Empatica to let me play with an [E4 wristband] (https://www.empatica.com/product-e4)
