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
	GPIO.output(GPIO_TRIGGER, True)
# set Trigger after 0.01ms to LOW
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER, False)
	StartTime = time.time()
	StopTime = time.time()
	while GPIO.input(GPIO_ECHO) == 0:
		StartTime = time.time()
	while GPIO.input(GPIO_ECHO) == 1:
		StopTime = time.time()

	TimeElapsed = StopTime - StartTime
	distance = (TimeElapsed*34300)/2

	return distance

if __name__ == '__main__':
	pub = rospy.Publisher('distancia', Float64, queue_size=1)
	rospy.init_node('rangesensor', anonymous=True)
	rate = rospy.Rate(1)
	try:
		while True:
			dist = distance()
			pub.publish(dist)
#print ("distancia = %.1f cm" % dist)

	except rospy.ROSInterruptException:
		print("finalizado")
		GPIO.cleanup()
	pass
