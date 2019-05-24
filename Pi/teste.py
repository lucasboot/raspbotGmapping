
#!/usr/bin/env python2.7  
# script by Alex Eames https://raspi.tv/  
# https://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio  
import RPi.GPIO as GPIO 
import rospy
from std_msgs.msg import Int16

GPIO.setmode(GPIO.BCM)  

rospy.init_node('encoders', anonymous=True)
pub1 = rospy.Publisher('lwheel', Int16, queue_size=1)
pub2 = rospy.Publisher('rwheel', Int16, queue_size=1)
msg1 = Int16()
msg2 = Int16()
cont1 = 0
cont2 = 0
# GPIO 23 set up as input. It is pulled up to stop false signals  
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)


try:  
    if(GPIO.event_detected(20)):
        cont1 = cont1 + 1
        print(cont1)
        msg1.data = cont1
        pub1.publish(msg1)
    if(GPIO.event_detected(21)):
        cont2 = cont2 + 1
        print(cont2)
        msg2.data = cont2
        pub2.publish(msg2)    
except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
GPIO.cleanup()           # clean up GPIO on normal exit