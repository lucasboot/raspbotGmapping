from gpiozero import DigitalInputDevice
import rospy
from std_msgs.msg import Int16

rospy.init_node('encoderEsquerdo', anonymous=True)
msg = Int16()
pub = rospy.Publisher('lwheel', Int16, queue_size=1)
encoder1 = DigitalInputDevice(20)
cont1 = 0
while True:
        encoder1.wait_for_active()
        global cont1
        cont1 = cont1 +1
        msg.data = cont1
        pub.publish(msg)
        print cont1
        encoder1.wait_for_inactive()




