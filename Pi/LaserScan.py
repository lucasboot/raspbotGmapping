#!/usr/bin/python
import rospy
from std_msgs.msg import Float32
from sensor_msgs.msg import LaserScan
import time
import VL53L0X

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
				num_readings = 67
				laser_frequency = 16 #arquivo testando no Raspberry
				scan_time = rospy.Time.now()
				scan = LaserScan()
				scan.header.stamp = scan_time
				scan.header.frame_id = "laser"
				scan.angle_min = 0
				scan.angle_max = 3.141592654
				scan.angle_increment = 0.047123889  # valor do incremento de cada 0.1 da lib gpiozero
				scan.time_increment = (1/laser_frequency)/(num_readings)
				scan.range_min = 0.05
				scan.range_max = 2.00
				for i in range(0, num_readings, 1):
					scan.ranges.append(tof.get_distance()/1000.0)
					scan.intensities.append(0)
					time.sleep(timing/1000000.00)
				scan_pub.publish(scan)
	except rospy.ROSInterruptException:
			GPIO.cleanup()
			pass
	
