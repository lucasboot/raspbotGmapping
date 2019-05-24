#!/usr/bin/env python
import RPIO
import rospy
from std_msgs.msg import Int16

#definir a funcao de callback

rospy.init_node('encoders', anonymous=True)
pub1 = rospy.Publisher('lwheel', Int16, queue_size=1)
pub2 = rospy.Publisher('rwheel', Int16, queue_size=1)
msg1 = Int16()
msg2 = Int16()
cont1 = 0
cont2 = 0
def gpio_cb(gpio_id, value):
   cont1 = cont +1
   ms1.data = msg1
   pub1.publish(ms1)

def gpio_cb2(gpio_id, value):
   cont2 = cont2 +1
   ms2.data = msg2
   pub2.publish(ms2)
#adicionar a interrupcao
try:
    while True:
        RPIO.add_interrupt_callback(20, gpio_cb1, edge='falling', pull_up_down=RPIO.PUD_UP, threaded_callback=True, debounce_timeout_ms=0)
        RPIO.add_interrupt_callback(21, gpio_cb2, edge='falling', pull_up_down=RPIO.PUD_UP, threaded_callback=True, debounce_timeout_ms=0)
    #colocar a interrupcao em loop
        RPIO.wait_for_interrupts()
except rospy.ROSInterruptException:
		GPIO.cleanup()
		pass