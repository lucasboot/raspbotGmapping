from gpiozero import DigitalInputDevice
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Float32
import time

rospy.init_node('encoderEsquerdo', anonymous=True)
msg = Int16()
pub = rospy.Publisher('lwheel', Int16, queue_size=1)
pub2 = rospy.Publisher('girosl', Float32, queue_size=1)
encoder1 = DigitalInputDevice(20)
cont1 = 0
while True:
	inicio  = cont1
        start = time.time()
        giros = Float32()
        while time.time() < start +1:
		news = time.time()
		while (encoder1.value == 0):
			pub.publish(msg)
			#print(msg.data)
               		if((news + 1)< time.time()):
                        	giros.data = 0.0
                        	pub2.publish(giros)
                global cont1
                cont1 = cont1 +1
                msg.data = cont1
                pub.publish(msg)
		news = time.time()
		#print(cont1)
                while(encoder1.value == 1):
			pub.publish(msg)
			#print(msg.data)

			if((news + 1)< time.time()):
                               giros.data = 0.0
                               pub2.publish(giros) 
        giros.data =float(cont1 - inicio)/20.0
	pub2.publish(giros)
