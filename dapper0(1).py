#!/usr/bin/env python3

# Import the necessary libraries
import time
import math
from ev3dev2.motor import *
from ev3dev2.sound import Sound
from ev3dev2.button import Button
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *

# ---------- Cria os motores do objeto
motorA = LargeMotor(OUTPUT_A)
motorB = LargeMotor(OUTPUT_B)
left_motor = motorA
right_motor = motorB
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
steering_drive = MoveSteering(OUTPUT_A, OUTPUT_B)
CSd = ColorSensor(INPUT_2)
CSe = ColorSensor(INPUT_1)

CSe.mode = 'COL-COLOR'
CSd.mode = 'COL-COLOR'

# Here is where your code starts

while True:
    if CSe.color == 6 and CSd.color == 6:
        tank_drive.on(5, 5)
    elif CSe.color != 6 and CSd.color == 6:
        tank_drive.on(-3.5, 5)
        while CSe.color != 6 and CSd.color != 6:
            tank_drive.on(-5, 0)
    elif CSe.color == 6 and CSd.color != 6:
        tank_drive.on(5, -3.5)
        while CSe.color != 6 and CSd.color != 6:
            tank_drive.on(0, -5)
           
                
    else:
        tank_drive.on(0,0)
