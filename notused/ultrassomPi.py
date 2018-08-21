#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import rospy
from std_msgs.msg import Float64

GPIO.setmode(GPIO.BCM) 
GPIO_TRIGGER = 23 
GPIO_ECHO = 24
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
	#metodo para calculo da distancia >
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

if __name__ == '__main__':
	pub = rospy.Publisher('distancia', Float64, queue_size=1) #criacao de um publicador no topico distancia
	rospy.init_node('rangesensor', anonymous=True) #inicializacao do node rangesensor
	rate = rospy.Rate(1) #rate para execucao dos comandos do ROS
	try:
		while True:
			dist = distance() #le o valor do ultrassom e coloca o valor na variavel dist
			pub.publish(dist) #publica a distancia no topico distancia
			time.sleep(0.0001)
	except rospy.ROSInterruptException:
		print("finalizado")
		GPIO.cleanup()
	pass
