#! /usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as gpio
import time

rospy.init_node('encoders', anonymous=True)
gpio.setmode(gpio.BCM)
gpio.setup(20, gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(21, gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setmode(gpio.BCM)  
cont1 = 0
cont2 = 0

def eventoesquerdo(channel):
	global cont1 = cont1 + 1
	print(cont1)

def eventodireito(channel):
	global cont2 = cont2 + 1
        print(cont2)


gpio.add_event_detect(20, gpio.RISING, callback=eventoesquerdo, bouncetime=300)
gpio.add_event_detect(21, gpio.RISING, callback=eventodireito, bouncetime=300)

try:


except KeyboardInterrupt:  
    gpio.cleanup()        
gpio.cleanup()    	

