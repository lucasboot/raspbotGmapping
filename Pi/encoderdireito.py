from gpiozero import DigitalInputDevice
import rospy
from std_msgs.msg import Int16
import time

rospy.init_node('encoderEsquerdo', anonymous=True)
msg = Int16()
giros = Int16()
giros.data = 0
pub = rospy.Publisher('rwheel', Int16, queue_size=1)
pub2 = rospy.Publisher('giros', Int16, queue_size=1)
encoder1 = DigitalInputDevice(21)
cont1 = 0
while True:
        global giros = cont1
        start = time.time()
        while time.time() < start +5:
                encoder1.wait_for_active()
                global cont1
                cont1 = cont1 +1
                msg.data = cont1
                pub.publish(msg)
                print cont1
                encoder1.wait_for_inactive()
        giros.data = cont1 - giros.data
        pub2.publish(giros)