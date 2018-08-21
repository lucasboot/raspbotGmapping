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
def allStop():
	#print("Parando")
	forwardLeft.value = 0
	reverseLeft.value = 0


def forwardDrive():
	#print("Para frente")
	forwardLeft.value = 0.0
	reverseLeft.value = 1.0

def reverseDrive():
	#print("Girar para esquerda")
	forwardLeft.value = 1.0
	reverseLeft.value = 0.0

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

rospy.init_node('encoderEsquerdo', anonymous=True)
msg = Int16()
pub = rospy.Publisher('lwheel', Int16, queue_size=1)
pub2 = rospy.Publisher('girosl', Float32, queue_size=1)
encoder1 = DigitalInputDevice(21)
cont1 = 0
def parafrente():
	forwardDrive()
	inicio  = cont1
        start = time.time()
        giros = Float32()
        while time.time() < start +1:
	    news = time.time()
	    while (encoder1.value == 0):
		pub.publish(msg)
               	if((news + 1)< time.time()):
                        giros.data = 0.0
                        pub2.publish(giros)
            global cont1
            cont1 = cont1 +1
            msg.data = cont1
            pub.publish(msg)
	    news = time.time()
            while(encoder1.value == 1):
		pub.publish(msg)
		if((news + 1)< time.time()):
                	giros.data = 0.0
                	pub2.publish(giros) 
            giros.data =float(cont1 - inicio)/20.0
	    pub2.publish(giros)

def paratras():
	reverseDrive()
	inicio  = cont1
        start = time.time()
        giros = Float32()
        while time.time() < start +1:
	    news = time.time()
	    while (encoder1.value == 0):
		pub.publish(msg)
               	if((news + 1)< time.time()):
                        giros.data = 0.0
                        pub2.publish(giros)
            global cont1
            cont1 = cont1 -1
            msg.data = cont1
            pub.publish(msg)
	    news = time.time()
            while(encoder1.value == 1):
		pub.publish(msg)

		if((news + 1)< time.time()):
                	giros.data = 0.0
                	pub2.publish(giros) 
            giros.data =float(cont1 - inicio)/20.0
	    pub2.publish(giros)

def main():
	dist = distance()
	if (dist < 5.0):
		paratras()
	else:
		parafrente()

if __name__ == '__main__':
    while True:
        main()
allStop()
GPIO.cleanup()
