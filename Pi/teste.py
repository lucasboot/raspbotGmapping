from gpiozero import PWMOutputDevice
from time import sleep
import rospy
from std_msgs.msg import Bool
import time

rospy.init_node('motores', anonymous=True)
pub1 = rospy.Publisher('motorA', Bool, queue_size=1)
pub2 = rospy.Publisher('motorB', Bool, queue_size=1)

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

def allStop():
	print("Parando")
	forwardLeft.value = 0
	reverseLeft.value = 0
	forwardRight.value = 0
	reverseRight.value = 0

def forwardDrive():
	print("Para frente")
	forwardLeft.value = 0.0
	reverseLeft.value = 1.0
	forwardRight.value = 0.0
	reverseRight.value = 1.0

def reverseDrive():
	print("Para tras")
	forwardLeft.value = 1.0
	reverseLeft.value = 0.0
	forwardRight.value = 1.0
	reverseRight.value = 0


def spinLeft():
	print("Girar para esquerda")
	forwardLeft.value = 1.0
	reverseLeft.value = 0
	forwardRight.value = 0
	reverseRight.value = 1.0

def SpinRight():
	print("Girar para direita")
	forwardLeft.value = 0
	reverseLeft.value = 1.0
	forwardRight.value = 1.0
	reverseRight.value = 0

def forwardTurnLeft():
	print("Noroeste")
	forwardLeft.value = 0 
	reverseLeft.value = 0.8
	forwardRight.value =0
	reverseRight.value = 1.0

def forwardTurnRight():
	print("Nordeste")
	forwardLeft.value = 0
	reverseLeft.value = 1.0
	forwardRight.value = 0
	reverseRight.value = 0.8

def reverseTurnLeft():
	print("Sudoeste")
	forwardLeft.value = 0.8
	reverseLeft.value = 0
	forwardRight.value = 1.0
	reverseRight.value = 0

def reverseTurnRight():
	print("Sudeste")
	forwardLeft.value = 1.0
	reverseLeft.value = 0
	forwardRight.value = 0.8
	reverseRight.value = 0

def main():
    msg1 = Bool()
    msg2 = Bool()
    allStop()
    sleep(3)
    forwardDrive()
    start = time.time()
    while (start +20 > time.time()):
            msg1.data = True
            msg2.data = True
            pub1.publish(msg1)
            pub2.publish(msg2)
    reverseDrive()
    start = time.time()
    while (start +20 > time.time()):
            msg1.data = False
            msg2.data = False
            pub1.publish(msg1)
            pub2.publish(msg2)

if __name__ == "__main__":
	while(True):
		main()
  
