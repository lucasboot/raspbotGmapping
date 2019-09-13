#!/usr/bin/env python
import math
import time
import numpy
import sys, select, os
import rospy
from sensor_msgs.msg import LaserScan
global laser = LaserScan()

def callback(data):
    global laser
    laser = data
    
if __name__ == '__main__':
    arq = open("lidar.csv", "w+")
    rospy.init_node('dados', anonymous=True)
    rospy.Subscriber("/kobuki/laser/scan", LaserScan, callback)
    global laser
    for i in range(len(laser.ranges)):
        
    rospy.spin()