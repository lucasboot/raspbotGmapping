#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Float32
import math
def callback(data):
   # print( (2*math.pi*3.225*data.data)/1.0)
     print(data.data)
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("motorA", Bool, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
