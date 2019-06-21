from gpiozero import DigitalInputDevice
import rospy
from std_msgs.msg import Int16
import time

rospy.init_node('encoderEsquerdo', anonymous=True)
msg = Int16()
pub = rospy.Publisher('lwheel', Int16, queue_size=1)
pub2 = rospy.Publisher('girosl', Int16, queue_size=1)
encoder1 = DigitalInputDevice(21)
cont1 = 0
while True:
	inicio  = cont1
        start = time.time()
        while time.time() < start +5:
		while (encoder1.value == 0):
			pub.publish(msg)
                global cont1
                cont1 = cont1 +1
                msg.data = cont1
                pub.publish(msg)
                while(encoder1.value == 1):
                        pub.publish(msg)  
	giros = Int16()
	#print (cont1 - inicio)
        giros.data = cont1 - inicio
        pub2.publish(giros)
