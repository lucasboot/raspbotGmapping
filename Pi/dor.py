#!/usr/bin/python

import time
import math
import rospy
from std_msgs.msg import Int16

dist_meas = 0.00
d_m =0
sensor = 20
contador = 0
pulso = 0

def cb(data):
	global pulso
	pulso = data.data

def cb2(data):
	global contador
	contador = data.data

def calculate_speed(r_cm, pulsos):
	global dist_meas,m_per_sec, sensor, d_m
	if pulsos !=0:							# to avoid DivisionByZero error
		circ_cm = (2*math.pi)*r_cm			# calculate wheel circumference in CM
		d_m = circ_cm/100 			# convert cm to m
		m_per_sec = d_m/5		# calculate m/sec
		dist_meas = (pulsos/sensor) * circ_cm	# measure distance traverse in cm
		return m_per_sec
	else:
		return 0


if __name__ == '__main__':
	while True:
		start = time.time()
		global contador
		global pulso
		sub2 = rospy.Subscriber('lwheel', Int16, cb2)
		while time.time() < start +5:
			sub = rospy.Subscriber('lwheel', Int16, cb)
		giros = pulso - contador
		calculate_speed(3.225, giros)	# call this function with wheel radius as parameter
		sleep(0.1)
