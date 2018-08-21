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
import time
import VL53L0X

# Create a VL53L0X object
tof = VL53L0X.VL53L0X(i2c_bus=1,i2c_address=0x29)
# I2C Address can change before tof.open()
# tof.change_address(0x32)
tof.open()
# Start ranging
tof.start_ranging(VL53L0X.Vl53l0xAccuracyMode.BETTER)

timing = tof.get_timing()
if timing < 20000:
    timing = 20000
myGPIO=17 #5V e GND
myCorrection=0.45
maxPW=(2.0+myCorrection)/1000
minPW=(1.0-myCorrection)/1000

myServo = Servo(myGPIO,min_pulse_width=minPW,max_pulse_width=maxPW)

print("Using GPIO17")
print("Max pulse width is set to 2.45 ms")
print("Min pulse width is set to 0.55 ms")

#while True:
start = time.time()
cont = 0
cont2 = 0
for value in numpy.arange(3,17, 0.3):
  cont2 = cont2 +1
  value2=(float(value)-10)/10 
  distance = tof.get_distance()
  if distance > 0:
    print(distance/10)
    cont = cont +1
  myServo.value=value2
  #print("Servo value set to "+str(value2))
  time.sleep(timing/1000000.00)
print("Numero de leituras")
print(cont)
print("Execucoes:")
print(cont2)
#print(time.time() - start)
tof.stop_ranging()
tof.close()
  


