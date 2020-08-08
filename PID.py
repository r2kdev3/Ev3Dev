#!/usr/bin/env python3
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.motor import SpeedPercent, MoveTank, LineFollowErrorTooFast

tank = MoveTank(OUTPUT_B, OUTPUT_C)
tank.cs = ColorSensor(INPUT_1)
try:
    tank.follow_line(
        kp=0.8, ki=0.25, kd=14,
        target_light_intensity = 30,
        follow_left_edge = True,
        speed=SpeedPercent(10)
    )
except LineFollowErrorTooFast:
    tank.stop()
    raise