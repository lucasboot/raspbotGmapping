from gpiozero import PWMOutputDevice
from time import sleep
import rospy
from raspbot.srv import MotorWay
from raspbot.srv import MotorWayRequest
from raspbot.srv import MotorWayResponse
from std_msgs.msg import Int16
import raspbot.msg
import time

# Motor A, Left Side GPIO CONSTANTS
PWM_FORWARD_LEFT_PIN = 6	# GPIO26
PWM_REVERSE_LEFT_PIN = 13	# GPIO19 

# Motor B, Right Side GPIO CONSTANTS
PWM_FORWARD_RIGHT_PIN = 26	# GPIO06 
PWM_REVERSE_RIGHT_PIN = 19	# GPIO13 


forwardLeft = PWMOutputDevice(PWM_FORWARD_LEFT_PIN, True, 0, 1000)
reverseLeft = PWMOutputDevice(PWM_REVERSE_LEFT_PIN, True, 0, 1000)

forwardRight = PWMOutputDevice(PWM_FORWARD_RIGHT_PIN, True, 0, 1000)
reverseRight = PWMOutputDevice(PWM_REVERSE_RIGHT_PIN, True, 0, 1000)
def setup(fa, ra, fb, rb):
	rospy.wait_for_service('motorway')
	try:
		motor = rospy.ServiceProxy('motorway', MotorWay)
		
	
def allStop():
	print("Parando")
	forwardLeft.value = 0
	reverseLeft.value = 0
	forwardRight.value = 0
	reverseRight.value = 0
	setup(reverseLeft.value, forwardLeft.value, forwardRight.value, reverseRight.value)
	resp = motor(forwardLeft.value, reverseLeft.value,
	

def forwardDrive():
	print("Para frente")
	forwardLeft.value = 0.0
	reverseLeft.value = 1.0
	forwardRight.value = 1.0
	reverseRight.value = 0.0
	setup(reverseLeft.value, forwardLeft.value, forwardRight.value, reverseRight.value)

def reverseDrive():
	print("Para tras")
	forwardLeft.value = 1.0
	reverseLeft.value = 0.0
	forwardRight.value = 1.0
	reverseRight.value = 0
	setup(reverseLeft.value, forwardLeft.value, forwardRight.value, reverseRight.value)


def spinLeft():
	print("Girar para esquerda")
	forwardLeft.value = 1.0
	reverseLeft.value = 0
	forwardRight.value = 0
	reverseRight.value = 1.0
	setup(reverseLeft.value, forwardLeft.value, forwardRight.value, reverseRight.value)

def SpinRight():
	print("Girar para direita")
	forwardLeft.value = 0
	reverseLeft.value = 1.0
	forwardRight.value = 1.0
	reverseRight.value = 0
	setup(reverseLeft.value, forwardLeft.value, forwardRight.value, reverseRight.value)



def main():
    allStop()
    sleep(3)
    forwardDrive()
    sleep(40)
if __name__ == "__main__":
	while True:
		main()
