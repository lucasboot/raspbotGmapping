from gpiozero import DigitalInputDevice
import time
from gpiozero import PWMOutputDevice
from time import sleep
import numpy
import sys, select, os
if os.name == 'nt':
  import msvcrt
else:
  import tty, termios

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
	#print("Para trs")
	forwardRight.value = 0.0
	reverseRight.value = 0.7
  	forwardLeft.value =  0.0
	reverseLeft.value = 1.0

def reverseDrive():
	#print("Girar para esquerda")
	forwardRight.value = 0.7
	reverseRight.value = 0.0
  	forwardLeft.value = 0.0
	reverseLeft.value = 0.7

def reverseDDrive():
	#print("Para frente")
	forwardRight.value = 0.0
	reverseRight.value = 0.7
  	forwardLeft.value =  1.0
	reverseLeft.value = 0.0

def main():
        
    while(1):
        key = getKey()
        if(key == 'w'):
            		forwardDrive()
        elif (key == 'q'):
			reverseDrive()
        elif (key == 'e' ): 
			reverseDDrive()
	elif (key == 's' ): 
			backwardDrive()
        else:
	  		allStop()
if __name__ == "__main__":
		
		if os.name != 'nt':
        		settings = termios.tcgetattr(sys.stdin)
		main()
  
		if os.name != 'nt':
        		termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
GPIO.cleanup()
