#!/usr/bin/python
import rospy
from std_msgs import Float32
from sensor_msgs import LaserScan
import time
import board
import busio

import adafruit_vl53l0x

if __name__ == '__main__':
    # inicializacao do node rangesensor
    rospy.init_node('rangesensor', anonymous=True)
    i2c = busio.I2C(board.SCL, board.SDA)
    vl53 = adafruit_vl53l0x.VL53L0X(i2c)
    scan_pub = rospy.Publisher('scan', LaserScan, queue_size=1)
    rate = rospy.Rate(1)  # rate para execucao dos comandos do ROS
    try:
		while True:
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
				scan.ranges[i] = 1  # vl53.range/1000
				scan.intensities[i] = 0
				time.sleep(1.0)
			scan_pub.publish(scan)
    except rospy.ROSInterruptException:
		GPIO.cleanup()
		pass
		
