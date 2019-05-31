#! /usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as gpio
import time
import rospy
from std_msgs.msg import Int16
from gpiozero import PWMOutputDevice
from time import sleep
import rospy

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

def forwardDrive():
  print("Para frente")
  forwardLeft.value = 0
  reverseLeft.value = 0.8
  forwardRight.value = 0.8
  reverseRight.value = 0

rospy.init_node('encoders', anonymous=True)
gpio.setmode(gpio.BCM)
gpio.setup(20, gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(21, gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setmode(gpio.BCM)  
pub1 = rospy.Publisher('lwheel', Int16, queue_size=1)
pub2 = rospy.Publisher('rwheel', Int16, queue_size=1)
msg1 = Int16()
msg2 = Int16()
cont1 = 0
cont2 = 0
allStop()
try:
	while (cont1 < 20 and cont2 < 20):
    		forwardDrive()
		if(gpio.input(20) == 1):
        		cont1 = cont1 + 1
        		msg1.data = cont1
        		pub1.publish(msg1)
        		print cont1
		if (gpio.input(21) == 1):
        		cont2 = cont2 + 1
        		msg2.data = cont2
        		pub2.publish(msg2)
        		print cont2
	
except rospy.ROSInterruptException:	
		allStop()
		gpio.cleanup()
		exit()
		pass
