#! /usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as gpio
import time
import rospy
from std_msgs.msg import Int16

rospy.init_node('encoders', anonymous=True)
gpio.setmode(gpio.BCM)
gpio.setup(20, gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(21, gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setmode(gpio.BCM)  
pub1 = rospy.Publisher('lwheel', Int16, queue_size=1)
pub2 = rospy.Publisher('rwheel', Int16, queue_size=1)
msg1 = Int16()
msg2 = Int16()
cont1 = 0
cont2 = 0

while True:
	if(gpio.input(20) == 1):
        cont1 = cont1 + 1
        msg1.data = cont1
        pub1.publish(msg1)
        print cont1
    if (gpio.input(21) == 1):
        cont2 = cont2 + 1
        msg2.data = cont2
        pub2.publish(msg2)
        print cont2
	time.sleep(0.1)
gpio.cleanup()
exit()