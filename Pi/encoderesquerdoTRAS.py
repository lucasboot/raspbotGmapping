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
import VL53L0X

# Create a VL53L0X object
tof = VL53L0X.VL53L0X(i2c_bus=1,i2c_address=0x29)
# I2C Address can change before tof.open()
# tof.change_address(0x32)
tof.open()
# Start ranging
tof.start_ranging(VL53L0X.Vl53l0xAccuracyMode.BETTER)

timing = tof.get_timing()
if timing < 20000:
    timing = 20000

def setup():
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

def parafrente(data, cont):
	if(data):
		forwardDrive()
	else:
		reverseDrive()
	msg = Int16()		
	while (encoder1.value == 0):
		pub.publish(msg)
	if(data):
		cont = cont +1
	else:
		cont = cont -1
	msg.data = cont1
	pub.publish(msg)
	while(encoder1.value == 1):
		pub.publish(msg)
	return cont

if __name__ == '__main__':
	setup()
	cont1 = 0
    try:
		while True:
			#distance = tof.get_distance()
			dist = distance()
			print(dist)
			if (dist < 20.0):
				cont1 = parafrente(False, cont1)
				print("Gira")
			else:
				cont1 = parafrente(True, cont1)
				print("Para frente")
			time.sleep(0.0001)
    except rospy.ROSInterruptException:
		allStop()
		tof.stop_ranging()
		tof.close()
		GPIO.cleanup()
    pass
