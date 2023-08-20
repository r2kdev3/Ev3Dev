#!/usr/bin/env python3

import time
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, InfraredSensor
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.motor import SpeedPercent, MoveTank, LineFollowErrorTooFast
from ev3dev2.sound import Sound

# initialize the sound class
sound = Sound()

# call the method speak
sound.speak('Go!')

sp = SpeedPercent(25)
tank = MoveTank(OUTPUT_A, OUTPUT_D)
steering = LargeMotor(OUTPUT_C)
shouldMoveForward = False
shouldMoveBackward = False
shouldTurnRight = False
shouldTurnLeft = False

def top_left_channel_1_action(state):
    global shouldMoveForward
    shouldMoveForward = True

def top_right_channel_1_action(state):
    global shouldMoveBackward
    shouldMoveBackward = True

def bottom_left_channel_1_action(state):
    global shouldTurnLeft
    shouldTurnLeft = True

def bottom_right_channel_1_action(state):
    global shouldTurnRight
    shouldTurnRight = True

# def on_channel1_beacon(state):
    # sound.speak('beacon button')
    # global shouldMoveForward
    # shouldMoveForward = False
    # tank.stop()

# tank.on_for_rotations(sp, sp, 2)

# steering = LargeMotor(OUTPUT_C)
# steering.on_for_rotations(SpeedPercent(20), 0.10)

# def bottom_right_channel_4_action(state):
# print("bottom right on channel 4: %s" % state)

ir = InfraredSensor()
ir.on_channel1_top_left = top_left_channel_1_action
ir.on_channel1_top_right = top_right_channel_1_action
ir.on_channel1_bottom_left = bottom_left_channel_1_action
ir.on_channel1_bottom_right = bottom_right_channel_1_action
# ir.on_channel1_beacon = on_channel1_beacon
# ir.on_channel4_bottom_right = bottom_right_channel_4_action

while True:
    ir.process()
    if shouldMoveForward == True:
        tank.on_for_rotations(sp, sp, -1)
        shouldMoveForward = False
    if shouldMoveBackward == True:
        tank.on_for_rotations(sp, sp, 1)
        shouldMoveBackward = False
    if shouldTurnRight == True:
        steering.on_for_rotations(sp, -0.5)
        shouldTurnRight = False
    if shouldTurnLeft == True:
        steering.on_for_rotations(sp, 0.5)
        shouldTurnLeft = False
    time.sleep(0.01)