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

	# Motor A, Left Side 
	###################################################################################

PWM_FORWARD_LEFT_PIN = 6	# GPIO06
PWM_REVERSE_LEFT_PIN = 13	# GPIO13 

forwardLeft = PWMOutputDevice(PWM_FORWARD_LEFT_PIN, True, 0, 1000)
reverseLeft = PWMOutputDevice(PWM_REVERSE_LEFT_PIN, True, 0, 1000)

	####################################################################################
	#Funcoes do motor
rospy.init_node('encoderEsquerdo', anonymous=True)
pub = rospy.Publisher('lwheel', Int16, queue_size=1)
encoder1 = DigitalInputDevice(20)
			

def allStop():
	#print("Parando")
	forwardLeft.value = 0
	reverseLeft.value = 0


def forwardDrive():
	#print("Para frente")
	forwardLeft.value = 1.0
	reverseLeft.value = 0.0

def reverseDrive():
	#print("Girar para esquerda")
	forwardLeft.value = 0.0
	reverseLeft.value = 1.0

#Funcao da distancia com o ultrassom
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

def parafrente(data, cont, value):
	if(data):
		forwardDrive()
	else:
		reverseDrive()
	msg = Int16()
	msg.data = cont		
	while ((encoder1.value == 0 and value==0)or (encoder1.value==1 and value==1)):
		pub.publish(msg)
	if(data):
		cont = cont +1
	else:
		cont = cont -1
	msg.data = cont
	pub.publish(msg)
	while((encoder1.value == 1 and value==1) or (encoder1.value==0 and value==0)):
		pub.publish(msg)
	return cont

if __name__ == '__main__':
    cont1 = 0
    try:
		while True:
			dist = distance()
			print(dist)
			if (dist < 20.0):
				cont1 = parafrente(False, cont1, encoder1.value)
				print("Gira")
			else:
				cont1 = parafrente(True, cont1, encoder1.value)
				print("Para frente")
			time.sleep(0.0001)
    except rospy.ROSInterruptException:
		allStop()
		GPIO.cleanup()
    pass
