#!/usr/bin/env python
from gpiozero import DigitalInputDevice
from gpiozero import PWMOutputDevice
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Float32
import time

# Motor B, Right Side GPIO CONSTANTS
PWM_FORWARD_RIGHT_PIN = 6	# GPIO06 
PWM_REVERSE_RIGHT_PIN = 13	# GPIO13 

forwardRight = PWMOutputDevice(PWM_FORWARD_RIGHT_PIN, True, 0, 1000)
reverseRight = PWMOutputDevice(PWM_REVERSE_RIGHT_PIN, True, 0, 1000)

####################################################################################
#Funcoes do motor
def allStop():
	#print("Parando")
	forwardRight.value = 0
	reverseRight.value = 0


def forwardDrive():
	#print("Para frente")
	forwardRight.value = 1.0
	reverseRight.value = 0.0

def reverseDrive():
	#print("Girar para esquerda")
	forwardRight.value = 0.0
	reverseRight.value = 1.0

#Funcao da distancia com o ultrassom

rospy.init_node('encoderEsquerdo', anonymous=True)
msg = Int16()
pub = rospy.Publisher('lwheel', Int16, queue_size=1)
pub2 = rospy.Publisher('girosl', Float32, queue_size=1)
encoder1 = DigitalInputDevice(20)
cont1 = 0
def parafrente():
    forwardDrive()
    inicio  = cont1
    start = time.time()
    #giros = Float32()
    while time.time() < start +1:
	news = time.time()
	while (encoder1.value == 0):
		pub.publish(msg)
       	global cont1
    	cont1 = cont1 +1
	msg.data = cont1
	pub.publish(msg)
	news = time.time()
    	while(encoder1.value == 1):
		pub.publish(msg)
	
def main():
    parafrente()
if __name__ == '__main__':
    while True:
        main()
allStop()
GPIO.cleanup()
