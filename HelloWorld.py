#!/usr/bin/env python3

from ev3dev2.sound import Sound

sound = Sound()
for i in range(1, 10):
    sound.speak('Hello Karandeep!')
    sound.speak('Hello Rewa!')
    sound.speak('Hello Naani!')
    sound.speak('Hello Mumma!')
    sound.speak('Hello daddy!')