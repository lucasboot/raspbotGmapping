#!/usr/bin/env python


from gpiozero import DigitalInputDevice
from gpiozero import PWMOutputDevice
from std_msgs.msg import Int16
from std_msgs.msg import Float32
import time
import rospy
import sys, select, os
if os.name == 'nt':
  import msvcrt
else:
  import tty, termios



# Motor A, Left Side GPIO CONSTANTS
PWM_FORWARD_LEFT_PIN = 6	# GPIO06 
PWM_REVERSE_LEFT_PIN = 13	# GPIO13 

forwardLeft = PWMOutputDevice(PWM_FORWARD_LEFT_PIN, True, 0, 1000)
reverseLeft = PWMOutputDevice(PWM_REVERSE_LEFT_PIN, True, 0, 1000)

# Motor B, Right Side GPIO CONSTANTS
PWM_FORWARD_RIGHT_PIN = 26	# GPIO06 
PWM_REVERSE_RIGHT_PIN = 19	# GPIO13 

forwardRight = PWMOutputDevice(PWM_FORWARD_RIGHT_PIN, True, 0, 1000)
reverseRight = PWMOutputDevice(PWM_REVERSE_RIGHT_PIN, True, 0, 1000)

#Funcoes do motor
def allStop():
	#print("Parando")
	forwardRight.value = 0
	reverseRight.value = 0
  	forwardLeft.value = 0
	reverseLeft.value = 0


def forwardDrive():
	#print("Para frente")
	forwardRight.value = 0.7
	reverseRight.value = 0.0
  	forwardLeft.value =  1.0
	reverseLeft.value = 0.0

def backwardDrive():
	#print("Para frente")
	forwardRight.value = 0.0
	reverseRight.value = 0.7
  	forwardLeft.value =  0.0
	reverseLeft.value = 1.0

def reverseDrive():
	#print("Girar para esquerda")
	forwardRight.value = 1.0
	reverseRight.value = 0.0
  	forwardLeft.value = 0.0
	reverseLeft.value = 1.0

def reverseDDrive():
	#print("Para frente")
	forwardRight.value = 0.0
	reverseRight.value = 1.0
  	forwardLeft.value =  1.0
	reverseLeft.value = 0.0

msg = """
Control Your Raspbot!
---------------------------
Moving around:
   q     w     e

         s   
              

CTRL-C to quit
"""

e = """
Communications Failed
"""

def getKey():
    if os.name == 'nt':
      return msvcrt.getch()

    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

rospy.init_node('raspbot_teleop')

#esquerdo
msg = Int16()
pub = rospy.Publisher('lwheel', Int16, queue_size=1)
encoder1 = DigitalInputDevice(20)
cont1 = 0

#direito
msg2 = Int16()
pub2 = rospy.Publisher('rwheel', Int16, queue_size=1)
encoder2 = DigitalInputDevice(21)
cont2 = 0

if __name__=="__main__":
    if os.name != 'nt':
        settings = termios.tcgetattr(sys.stdin)
    print (msg)
    a = True
    while(a):
        key = getKey()
        if key == 'w' :
	        forwardDrive()
          global cont1
          global cont2
          for i in range (4):
             cont1 = cont1 +1
             cont2 = cont2 +1 
             msg.data = cont1
             msg2.data = cont2
             pub.publish(msg)
             pub2.publish(msg2)
        elif key == 'q' :
          reverseDrive()
          global cont1
          global cont2
          for i in range (4):
             cont1 = cont1 -1
             cont2 = cont2 +1 
             msg.data = cont1
             msg2.data = cont2
             pub.publish(msg)
             pub2.publish(msg2)
        elif key == 'e' :
          reverseDDrive()
          global cont1
          global cont2
          for i in range (4):
             cont1 = cont1 -1
             cont2 = cont2 +1 
             msg.data = cont1
             msg2.data = cont2
             pub.publish(msg)
             pub2.publish(msg2)
        elif key == 's' :
          backwardDrive()
          global cont1
          global cont2
          for i in range (4):
             cont1 = cont1 -1
             cont2 = cont2 -1 
             msg.data = cont1
             msg2.data = cont2
             pub.publish(msg)
             pub2.publish(msg2)
	elif key == 'l':
		a = False
        else: #parado
          allStop()
          global cont1
          global cont2
          msg.data = cont1
          msg2.data = cont2
          pub.publish(msg)
          pub2.publish(msg2)

    if os.name != 'nt':
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
GPIO.cleanup()
