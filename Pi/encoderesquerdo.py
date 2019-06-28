from gpiozero import DigitalInputDevice
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Float32
from std_msgs.msg import Bool
import time

rospy.init_node('encoderEsquerdo', anonymous=True)
pub = rospy.Publisher('lwheel', Int16, queue_size=1)
pub2 = rospy.Publisher('girosl', Float32, queue_size=1)
encoder1 = DigitalInputDevice(21)
cont1 = 0
def callback (data):
        global cont1
        print(data.data)
        '''if(data.data):
                cont1 = cont1 +1 
        else:
                cont1 = cont1 - 1
           '''     
while True:
	inicio  = cont1
        start = time.time()
        giros = Float32()
        while time.time() < start +1:
		while (encoder1.value == 0):
                        news = time.time()
			pub.publish(msg)
                        if((news + 1) < time.time()):
                       		 giros.data = 0.0
                               	 pub2.publish(giros)
                
                rospy.Subscriber('motorA', Bool, callback)
               	msg = Int16()
		global cont1
		msg.data = cont1
                pub.publish(msg)
                while(encoder1.value == 1):
                       		news = time.time()
				pub.publish(msg)

                       		if((news + 1 )< time.time()):
                                	giros.data = 0.0
                                	pub2.publish(giros) 
        giros.data =float(cont1 - inicio)/20.0
        pub2.publish(giros)
