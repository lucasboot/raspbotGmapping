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
	teste = 0
        while time.time() < start +5:
		while (teste == 0):
			pub.publish(msg)
                encoder1.wait_for_active()
                global cont1
                cont1 = cont1 +1
                msg.data = cont1
                pub.publish(msg)
                #print cont1
                encoder1.wait_for_inactive()
	giros = Int16()
	print (cont1 - inicio)
        giros.data = cont1 - inicio
        pub2.publish(giros)
