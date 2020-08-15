#!/usr/bin/env python3
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.motor import SpeedPercent, MoveTank, LineFollowErrorTooFast, MediumMotor
from ev3dev2.sound import Sound

def MoveHead(speed, seconds):
    MM = MediumMotor(OUTPUT_C)
    MM.on_for_seconds(speed=speed, seconds=seconds)

def BarkSound(barktype):
    spkr=Sound()
    if barktype == 1:
        spkr.play_file('/home/robot/LightEmmitingDiode/sounds/Dog bark 1.wav')
    elif barktype == 2:
        spkr.play_file('/home/robot/LightEmmitingDiode/sounds/Dog bark 2.wav')
    elif barktype == 3:
        spkr.play_file('/home/robot/LightEmmitingDiode/sounds/Dog growl.wav')
    elif barktype == 4:
        spkr.play_file('/home/robot/LightEmmitingDiode/sounds/Dog whine.wav')
    elif barktype == 5:
        spkr.play_file('/home/robot/LightEmmitingDiode/sounds/Elephant call.wav')
    else:
        spkr.play_file('/home/robot/LightEmmitingDiode/sounds/Dog sniff.wav')


while True:
    MoveHead(50, 7)
    BarkSound(6)
    BarkSound(3)
    MoveHead(-50, 7)
    BarkSound(1)
    BarkSound(4)


