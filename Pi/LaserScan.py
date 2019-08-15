#!/usr/bin/python
import rospy
from std_msgs.msg import Float32
from sensor_msgs.msg import LaserScan
import time
import VL53L0X
from gpiozero import Servo
from time import sleep
import numpy
import math
#Configurando o servo motor

#####################
'''
myGPIO=17 #5V e GND
myCorrection=0.45
maxPW=(2.0+myCorrection)/1000
minPW=(1.0-myCorrection)/1000
myServo = Servo(myGPIO,min_pulse_width=minPW,max_pulse_width=maxPW)
'''
#####################

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
	rate = rospy.Rate(10)  # rate para execucao dos comandos do ROS
	try:
			while True:
				num_readings = 47
				laser_frequency = 16 #arquivo testando no Raspberry
				scan_time = rospy.Time.now()
				scan = LaserScan()
				scan.header.stamp = scan_time
				scan.header.frame_id = "base_scan"
				scan.angle_min = (math.pi*3)/20
				scan.angle_max = (math.pi*17)/20
				scan.angle_increment = (math.pi*0.3)/20  # valor do incremento de cada 0.1 da lib gpiozero
				scan.time_increment = (1/laser_frequency)/(num_readings)
				scan.range_min = 0.05
				scan.range_max = 10.00
				#value = 3.0
				print((scan.angle_max - scan.angle_min)/num_readings)
				for i in range(0, num_readings, 1):
					'''
					value2=(float(value)-10)/10.0 
    					myServo.value=value2
					value = value + 0.3 # ((scan.angle_max - scan.angle_min)/num_readings)
					'''
					scan.ranges.append(tof.get_distance()/1000.0)
					scan.intensities.append(0)
					time.sleep(timing/1000000.00)
				scan_pub.publish(scan)
				#value = 3.0
				#value2=(float(value)-10)/10.0 
                                #myServo.value=value2 
				#print(value) 
				sleep(0.000001)
	except rospy.ROSInterruptException:
			GPIO.cleanup()
			pass
	
