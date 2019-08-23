#! /usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as gpio
import time
from std_msgs.msg import Int16
from gpiozero import PWMOutputDevice
from time import sleep

current_milli_time = lambda: int(round(time.time() * 1000))

#///////////////// Definir os pinos dos motores /////////////////
# Motor A, Left Side GPIO CONSTANTS
PWM_FORWARD_LEFT_PIN = 26	# GPIO26- Pra frente
PWM_REVERSE_LEFT_PIN = 19	# GPIO19 - Pra tras
# Motor B, Right Side GPIO CONSTANTS
PWM_FORWARD_RIGHT_PIN = 6	# GPIO06 
PWM_REVERSE_RIGHT_PIN = 13	# GPIO13 

# Initialise objects for H-Bridge PWM pins
# Inicializar o  duty cycle em 0 e a frequência em 1000
forwardLeft = PWMOutputDevice(PWM_FORWARD_LEFT_PIN, True, 0, 1000)
reverseLeft = PWMOutputDevice(PWM_REVERSE_LEFT_PIN, True, 0, 1000)

forwardRight = PWMOutputDevice(PWM_FORWARD_RIGHT_PIN, True, 0, 1000)
reverseRight = PWMOutputDevice(PWM_REVERSE_RIGHT_PIN, True, 0, 1000)

def allStop():
  print("Parando")
  forwardLeft.value = 0
  reverseLeft.value = 0
  forwardRight.value = 0
  reverseRight.value = 0

def forwardDrive(rpm1, rpm2):
  print("Para frente")
  forwardLeft.value = 0
  reverseLeft.value = 0.5
  forwardRight.value = 0.5
  reverseRight.value = 0
  regular(rpm1, rpm2)

def regular(rpmr, rpml):
	while ((rpm1 > rpm2) and (rpm1 <=1 and rpm2<=1)):
		forwardRight.value = forwardRight.value + 0.05
	while ((rpm2 > rpm1) and (rpm1 <=1 and rpm2 <=1)):
		reverseLeft.value = reverseLeft.value + 0.05


gpio.setmode(gpio.BCM)
gpio.setup(20, gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(21, gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setmode(gpio.BCM)  
cont1 = 0
incre1 = 0
incre2= 0
cont2 = 0
allStop()
timeold = current_milli_time()
rpm1 = 0
rpm2 = 0
try:
	while True:
    		forwardDrive(rpm1, rpm2)
		if(gpio.input(20) == 1):
        		cont1 = cont1 + 1
			incre1 = incre1+1
		if (gpio.input(21) == 1):
        		cont2 = cont2 + 1
			incre2 = incre2 + 1
		if((current_milli_time() - timeold) >= 1000):
				rpm1 = (60 * 1000 / 20 ) / (current_milli_time() - timeold) * incre1
				rpm2 = (60 * 1000 / 20 ) / (current_milli_time() - timeold) * incre2
				print rpm1
				print rpm2
				incre1 = 0
				incre2=0
		
except KeyboardInterrupt:	
		allStop()
		gpio.cleanup()
		exit()
		pass
