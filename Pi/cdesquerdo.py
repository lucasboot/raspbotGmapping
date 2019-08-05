#!/usr/bin/env python
from gpiozero import DigitalInputDevice
from gpiozero import PWMOutputDevice
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Float32
import RPi.GPIO as GPIO
from gpiozero import PWMOutputDevice
from time import sleep
import time


GPIO.setmode(GPIO.BCM) 
GPIO_TRIGGER = 23 
GPIO_ECHO = 24
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

# Motor B, Right Side GPIO CONSTANTS
PWM_FORWARD_RIGHT_PIN = 6	# GPIO06 
PWM_REVERSE_RIGHT_PIN = 13	# GPIO13 

forwardRight = PWMOutputDevice(PWM_FORWARD_RIGHT_PIN, True, 0, 1000)
reverseRight = PWMOutputDevice(PWM_REVERSE_RIGHT_PIN, True, 0, 1000)

def distance():
	GPIO.output(GPIO_TRIGGER, True)
	time.sleep(0.00001) #set trigger apos 0,01ms
	GPIO.output(GPIO_TRIGGER, False)
	StartTime = time.time()
	StopTime = time.time()
	while GPIO.input(GPIO_ECHO) == 0:
		StartTime = time.time()
	while GPIO.input(GPIO_ECHO) == 1:
		StopTime = time.time()
	TimeElapsed = StopTime - StartTime
	distance = (TimeElapsed*34300)/2 #formula para obtencao da distancia
	return distance

####################################################################################
#Funcoes do motor
def allStop():
	#print("Parando")
	forwardRight.value = 0
	reverseRight.value = 0


def forwardDrive():
	#print("Para frente")
	forwardRight.value = 1.0
	reverseRight.value = 0.0

def reverseDrive():
	#print("Girar para esquerda")
	forwardRight.value = 0.0
	reverseRight.value = 1.0

#Funcao da distancia com o ultrassom

rospy.init_node('encoderEsquerdo', anonymous=True)
msg = Int16()
pub = rospy.Publisher('lwheel', Int16, queue_size=1)
pub2 = rospy.Publisher('girosl', Float32, queue_size=1)
encoder1 = DigitalInputDevice(20)
cont1 = 0

def parafrente(data):
	if(data):
    	forwardDrive()
	else:
		reverseDrive()
    inicio  = cont1
    #giros = Float32()
	while (encoder1.value == 0):
		pub.publish(msg)
    global cont1
	if(data):
    	cont1 = cont1 +1
	else:
		cont1 = cont1 -1 
	msg.data = cont1
	pub.publish(msg)
    while(encoder1.value == 1):
		pub.publish(msg)
	

if __name__ == '__main__':
	leituras = []
	i = 0
    while True:
		dist = distance()
		leituras.append(dist)
		i = i +1
		if(i==5):
			leituras = sorted(leituras)
        if (i < 5):
			parafrente(True)
		else if (leituras[2] < 15):
			parafrente(False)
			i = 0
			del leituras[0:5]
		else:
			parafrente(True)
			i=0
			del leituras[0:5]
allStop()
GPIO.cleanup()
