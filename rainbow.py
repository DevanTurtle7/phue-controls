#!/usr/bin/python
#Started January 10th, 2018
#Devan Kavalchek

#XY COLOR
#[1,0] - R
#[0,1] - G
#[0,0] - B

from phue import Bridge
import time

b = Bridge('') #YOUR IP

colorLights = []
playing = True
rainbowRooms = ["Devan's Bedroom"]
lights = []
intervalTime = .1

#CUSTOM FOR STATEMENT SETU[
def my_range(start, end, step):
    while start <= end:
        yield start
        start += step
#/CUSTOM FOR STATEMENT SETUP

#BRIDGE SETUP
if b == None:
    b.connect();
    print("connecting to bridge...")
else:
    print("bridge is connected");

print(b.get_group(1, 'lights'))
#/BRIDGE SETUP

#GET COLOR LIGHTS
for room in b.get_group():
    for name in rainbowRooms:
        iRoom = int(room)
        if b.get_group(iRoom, 'name') == name.__str__():
            for light in b.get_group(iRoom, 'lights'):
                iLight = int(light)
                if b.get_light(iLight, 'type') == "Extended color light":
                    colorLights.append(b.get_light(iLight, 'name'))
                    b.set_light(iLight, 'on', True)
                    b.set_light(iLight, 'bri', 254)

print(colorLights)
#/GET COLOR LIGHTS

#RAINBOW
while playing:
    for x in my_range(0,1, .05):
        for cLight in colorLights:
            b.set_light(cLight, 'xy', [0,1-x])
        time.sleep(intervalTime)
        
    for x in my_range(0,1, .05):
        for cLight in colorLights:
            b.set_light(cLight, 'xy', [x,0])
        time.sleep(intervalTime)

    for x in my_range(0,1, .05):
        for cLight in colorLights:
            b.set_light(cLight, 'xy', [1,x])
        time.sleep(intervalTime)

    for x in my_range(0,1, .05):
        for cLight in colorLights:
            b.set_light(cLight, 'xy', [1-x,1])
        time.sleep(intervalTime)

    time.sleep(intervalTime)
#/RAINBOW
