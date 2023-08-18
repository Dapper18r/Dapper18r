#!/usr/bin/env python3

# ---------- Importa as bibliotecas necessarias
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


CS1 = ColorSensor(INPUT_1)   
CS2 = ColorSensor(INPUT_2)  
IS = InfraredSensor(INPUT_4)
GS = GyroSensor(INPUT_3) 


CS1.mode = 'COL-COLOR'
CS2.mode = 'COL-COLOR'
IS.mode = 'IR-PROX'
GS.mode = 'GYRO-ANG'
#TS.mode = 'TOUCH'



# ---------- Aqui é onde seus codigos começam

#----------- def´s

def arrumando(): 
    
    if (CS1.color and CS2.color) == 6:
        tank_drive.on(10,10)
    elif CS1.color == 6 and CS2.color != 6:
        tank_drive.on(10,0)
        while (CS1.color and CS2.color) != 6:
        tank_drive.on(0,0)