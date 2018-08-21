from gpiozero import DigitalInputDevice
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Float32
from std_msgs.msg import Bool
import time

msg = Int16()
encoder1 = DigitalInputDevice(20)
cont1 = 0
def callback (data):   
        global cont1
	print("cheguei po")
        if(data.data == True):
                cont1 = cont1 +1 
        else:
                cont1 = cont1 - 1
                       
def main():
	rospy.init_node('encoderDireito', anonymous=True)
	pub3 = rospy.Publisher('rwheel', Int16, queue_size=1)
	pub4 = rospy.Publisher('girosr', Float32, queue_size=1)
	inicio  = cont1
        start = time.time()
        giros = Float32()
        while time.time() < start +1:
		news = time.time()
		while (encoder1.value == 0):
			pub3.publish(msg)
                        if((news + 1 )< time.time()):
                                giros.data = 0.0
                                pub4.publish(giros)
                
		#cont1 = cont1 +1
                rospy.Subscriber('motorB', Bool, callback)
                global cont1
		msg.data = cont1
                pub3.publish(msg)
		news=time.time()
                while(encoder1.value == 1):
			pub3.publish(msg)
                        if((news + 1 )< time.time()):
                                giros.data = 0.0
                                pub4.publish(giros)
        giros.data=float((cont1 - inicio))/20.0
        pub4.publish(giros)
	rospy.spin()
if __name__ == '__main__':
    main()
