#!/usr/bin/python

# Use CTRL-C to break out of While loop.
#
# Author : Matt Hawkins
# Date   : 20/01/2018
#
# https://www.raspberrypi-spy.co.uk/tag/servo/
#
#--------------------------------------
from gpiozero import Servo
from time import sleep
import numpy

myGPIO=17 #5V e GND
myCorrection=0.45
maxPW=(2.0+myCorrection)/1000
minPW=(1.0-myCorrection)/1000

myServo = Servo(myGPIO,min_pulse_width=minPW,max_pulse_width=maxPW)

print("Using GPIO17")
print("Max pulse width is set to 2.45 ms")
print("Min pulse width is set to 0.55 ms")

while True:

  for value in numpy.arange(3,17, 0.3):
    value2=(float(value)-10)/10 
    myServo.value=value2
    print("Servo value set to "+str(value2))
    sleep (0.1)
  


