#!/usr/bin/python

import time
import math
import rospy
from std_msgs.msg import Float32

rospy.init_node('calcveldireita', anonymous=True)

def calculate_speed(r_cm, giros):						
		circ_cm = (2*math.pi)*r_cm
		cm_per_sec=(circ_cm*giros)/3.0		
		return cm_per_sec

def cb(data):
	print(calculate_speed(3.225,data.data))

if __name__ == '__main__':
	while True:
		sub = rospy.Subscriber('girosr', Float32, cb)
		time.sleep(0.01)

