#!/usr/bin/python

# MIT License
# 
# Copyright (c) 2017 John Bryan Moore
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import time
import VL53L0X
from gpiozero import Servo
from time import sleep
import numpy

cont = 0;
# Create a VL53L0X object
tof = VL53L0X.VL53L0X(i2c_bus=1,i2c_address=0x29)
tof.open()
tof.start_ranging(VL53L0X.Vl53l0xAccuracyMode.BETTER)
myGPIO=17 
myCorrection=0.45
maxPW=(2.0+myCorrection)/1000
minPW=(1.0-myCorrection)/1000

myServo = Servo(myGPIO,min_pulse_width=minPW,max_pulse_width=maxPW)


timing = tof.get_timing()
if timing < 20000:
    timing = 20000
print("Timing %d ms" % (timing/1000))
value = 0
while (value<=20):
    value2=(float(value)-10)/10 
    myServo.value=value2
    print("Servo value set to "+str(value2))
    distance = tof.get_distance()
    if distance > 0:
        #print("%d mm, %d cm, %d" % (distance, (distance/10), count))
        cont = cont + 1
    value = value + 0.3
    time.sleep(timing/1000000.00)
    
print(str(cont) + " leituras realizadas")
tof.stop_ranging()
tof.close()


  
  
