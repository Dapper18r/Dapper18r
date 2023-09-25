#!/usr/bin/env python3

# ---------- Importa as bibliotecas necessarias
import time # importando o tempo para a logica de programacao
import math # importando a matematica para a logica de programaaao
from ev3dev2.motor import * # importando tudo da biblioteca ev3dev2.motor
from ev3dev2.sound import Sound # importando o som da biblioteca ev3dev2.sound
from ev3dev2.button import Button # importando os botoes da biblioteca ev3dev2.button
from ev3dev2.sensor import * # importando tudo da biblioteca ev3dev2.sensor
from ev3dev2.sensor.lego import * # importando tudo da biblioteca ev3dev2.sensor.lego
#from ev3dev2.sensor.virtual import * # importando tudo da biblioteca ev3dev2.sensor.virtual

# ---------- Cria os motores do objeto
motorA = LargeMotor(OUTPUT_A) # Setando o motor na saida A como motorA
motorB = LargeMotor(OUTPUT_B) # Setando o motor na saida B como motorB
#motorC = LargeMotor(OUTPUT_C) # setando o motor na saída C como motorC
#motorD = LargeMotor(OUTPUT_D) # setando o motor na saída D como motorD

left_motor = motorA # Traduzindo que o motorA como motor da esquerda
right_motor = motorB # Traduzindo que o motorB como motor da direita
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B) # Setando o comando Tank_drive para utilizar os motores A e B juntos
steering_drive = MoveSteering(OUTPUT_A, OUTPUT_B) # Setando o comando steering_drive para utilizar a curva com os motores A e B

#spkr = Sound() # Setando a variavel som
#btn = Button() # Setando a variavel botao
#radio = Radio()  # Setando a variavel radio

CS1 = ColorSensor(INPUT_1)  # setando sensor de cor na entrada 
CS2 = ColorSensor(INPUT_2) # setando sensor de cor na entrada 
IS = InfraredSensor(INPUT_4)
##US = UltrasonicSensor(INPUT_4)  # setando sensor ultrasonico na entrada 
GS = GyroSensor(INPUT_3) # setando o sensor de giro na entra 
#TS = TouchSensor(INPUT_4) # setando o sensor de toque na entrada 
#color_sensor_in5 = ColorSensor(INPUT_5) # setando sensor de cor na entrada
SEM_COR = 0
PRETO = 1
AZUL = 2
VERDE = 3
AMARELO = 4
VERMELHO = 5
BRANCO = 6
MARROM = 7

x = 0

CS1.mode = 'COL-COLOR'
CS2.mode = 'COL-COLOR'
#US.mode = 'US-DIST-CM'
IS.mode = 'IR-PROX'
GS.mode = 'GYRO-ANG'
#TS.mode = 'TOUCH'

# Parâmetros da odometria (em centímetros)
circunferencia_roda = 21.5
diametro_roda = 6.9  # Diâmetro da roda em centímetros
circunferencia_roda = 3.1416 * diametro_roda  # Circunferência da roda

# Posição inicial do robô
x = 0
y = 0
theta = 0  # Ângulo de orientação

global rotina
rotina = 0 
#------------------------------------def's-----------------------------------------------------#

# Função para atualizar a odometria com base no movimento das rodas

#------------------------------------odo-----------------------------------------------------#
def atualizar_odometria(left_motor, right_motor):
    # Obtenha o número de rotações de cada motor
    esquerda_rotacoes = left_motor.position
    direita_rotacoes = right_motor.position
    
    # Calcule a distância percorrida por cada roda
    distancia_esquerda = (esquerda_rotacoes / 360) * circunferencia_roda
    distancia_direita = (direita_rotacoes / 360) * circunferencia_roda
    
    # Calcule a mudança na posição e orientação do robô
    delta_d = (distancia_esquerda + distancia_direita) / 2
    delta_theta = (distancia_direita - distancia_esquerda) / diametro_roda
    
    # Atualize a posição e orientação do robô
    global x, y, theta
    x += delta_d * cos(theta)
    y += delta_d * sin(theta)
    theta += delta_theta

    # Zere as posições dos motores para a próxima iteração
    left_motor.position = 0
    right_motor.position = 0

# Movimente o robô para a frente por 10 cm
    tank.on_for_rotations(50, 50, 1)  # Velocidade de 50%, 1 rotação

# Atualize a odometria
    atualizar_odometria(tank.left_motor, tank.right_motor)

# Imprima a posição estimada do robô
    print("Posição do Robô (x, y, theta):", x, y, degrees(theta))

# Gire o robô em torno do próprio eixo por 90 graus
    tank.turn_right(50, 90)  # Velocidade de 50%, 90 graus

# Atualize a odometria novamente
    atualizar_odometria(tank.left_motor, tank.right_motor)

# Imprima a nova posição estimada do robô
    print("Nova Posição do Robô (x, y, theta):", x, y, degrees(theta))

# Pare o robô
    tank.off()

    

#------------------------------------botao de inicio-----------------------------------------------------#
def comeco(): # para evitar alguns erros, fizemos isso para começar o robo resetando o sensor de gyro
    global rotina
    if IS.proximity >= 10: # quando o sensor infravermelho detectar algo a frente, ele da sequencia ao código
        GS.reset() # reseta o sensor de gyro
        time.sleep(.2) #espera
    else:
        print("aguardando") 
        
#------------------------------------fasendo o caminho-----------------------------------------------------#
def procurando_azul(): # caso a rotina seja igual a 1, ele começa a a procurar a zona azul
    global rotina
    if (CS1 and CS2) == 6: # caso os 2 sensores sejam iguais a branco, ele começa a andar para frente
        tank_drive.on(10,10)
    elif CS1 and CS2 == 2: # caso os sensores sejam iguais a azul, ele para e printa o "achei!!!!"
        print("achei!!!!")
        rotina += 2
    elif (CS1 or CS2) != 6 or (cCS1 or CS2) != 2: # caso os sensores detectem alguma parede, ele aumenta 1 a rotina
        print("parede a frente")
        tank_drive.on_for_seconds(-5,-5,3)
        ttank.on_for_rotations(10, -10, 0.25)
while True:
    while rotina == 0:
        print("comeco")
        comeco()
        rotina += 1
    
    while rotina == 1:
        print("mim de")
        procurando_azul()
        rotina += 1

    while rotina == 2:
        print("parede")
        curva()
        rotina -= 1
        print("rotina atual", rotina)

    while rotina == 3:
        print("acabou o programa, achei o azul")
        tank_drive.on(0,0)
        time.sleep(.3)
