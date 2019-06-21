#!/usr/bin/python

import time
import math
import rospy
from std_msgs.msg import Int16

rospy.init_node('calcvelesquerda', anonymous=True)
dist_meas = 0.00
d_m =0
sensor = 20
contador = 0
pulso = 0



def calculate_speed(r_cm, pulsos):
	global m_per_sec, d_m
	if pulsos !=0:							# to avoid DivisionByZero error
		circ_cm = float((2*math.pi)*r_cm)			# calculate wheel circumference in CM
		d_m =float(circ_cm/100.0) 			# convert cm to m
		m_per_sec =(float(d_m*(pulsos/20.0)))/5		# calculate m/sec
		# measure distance traverse in cm
		return m_per_sec
	else:
		return 0.0


def cb(data):
	print(calculate_speed(3.225,data.data))

if __name__ == '__main__':
	while True:
		sub = rospy.Subscriber('girosl', Int16, cb)
		time.sleep(0.01)
