#!/usr/bin/env python
import RPi.GPIO as GPIO
from gpiozero import PWMOutputDevice
from time import sleep
import time


GPIO.setmode(GPIO.BCM) 
GPIO_TRIGGER = 23 
GPIO_ECHO = 24
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

# Motor A, Left Side GPIO CONSTANTS
PWM_FORWARD_LEFT_PIN = 6	# GPIO26
PWM_REVERSE_LEFT_PIN = 13	# GPIO19 

# Motor B, Right Side GPIO CONSTANTS
PWM_FORWARD_RIGHT_PIN = 26	# GPIO06 
PWM_REVERSE_RIGHT_PIN = 19	# GPIO13 


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
	forwardLeft.value = 0.0
	reverseLeft.value = 0.5
	forwardRight.value = 0.5
	reverseRight.value = 0.0

def spinLeft():
	print("Girar para esquerda")
	forwardLeft.value = 0
	reverseLeft.value = 0
	forwardRight.value = 0.8
	reverseRight.value = 0

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
def main():
    dist = distance() #le o valor do ultrassom e coloca o valor na variavel dist
    print(dist)
    if(dist > 20):
		forwardDrive()
    else:
		spinLeft()
		sleep(3)
if __name__ == '__main__':
    while True:
        main()
allStop()
GPIO.cleanup()
