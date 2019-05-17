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
import rospy
from std_msgs.msg import Float32
from sensor_msgs.msg import LaserScan
import time
import VL53L0X

myGPIO=17 #5V e GND
myCorrection=0.45
maxPW=(2.0+myCorrection)/1000
minPW=(1.0-myCorrection)/1000

myServo = Servo(myGPIO,min_pulse_width=minPW,max_pulse_width=maxPW)

print("Using GPIO17")
print("Max pulse width is set to 2.45 ms")
print("Min pulse width is set to 0.55 ms")

if __name__ == '__main__':
	rospy.init_node('rangesensor', anonymous=True)
	tof = VL53L0X.VL53L0X(i2c_bus=1,i2c_address=0x29)
	tof.open()
	tof.start_ranging(VL53L0X.Vl53l0xAccuracyMode.BETTER)
	timing = tof.get_timing()	
	if timing < 20000:
		timing = 20000
	print("Timing %d ms" % (timing/1000))
	scan_pub = rospy.Publisher('scan', LaserScan, queue_size=1)
	rate = rospy.Rate(1)
	try:
			while True:
                for value in numpy.arange(0,20, 0.01):
                    value2=(float(value)-10)/10 
                    myServo.value=value2
                    print("Servo value set to "+str(value2))
                    sleep (0.1)
				num_readings = 10
				laser_frequency = 40
				scan_time = rospy.Time.now()
				scan = LaserScan()
				scan.header.stamp = scan_time
				scan.header.frame_id = "laser_frame"
				scan.angle_min = -1.57
				scan.angle_max = 1.57
				scan.angle_increment = 0.157075  # valor do incremento de cada 0.1 da lib gpiozero
				scan.time_increment = (1/laser_frequency)/(num_readings)
				scan.range_min = 0.05
				scan.range_max = 2.00
				for i in range(0, num_readings-1, 1):
					scan.ranges[i] = tof.get_distance()
					scan.intensities[i] = 0
					time.sleep(timing/1000000.00)
				scan_pub.publish(scan)
	except rospy.ROSInterruptException:
			GPIO.cleanup()
		pass