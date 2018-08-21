from gpiozero import PWMOutputDevice
from time import sleep

# Motor A, Left Side GPIO CONSTANTS
PWM_FORWARD_LEFT_PIN = 26	# GPIO26- Pra frente
PWM_REVERSE_LEFT_PIN = 19	# GPIO19 - Pra tras
# Motor B, Right Side GPIO CONSTANTS
PWM_FORWARD_RIGHT_PIN = 6	# GPIO06 
PWM_REVERSE_RIGHT_PIN = 13	# GPIO13 


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
	allStop()
	sleep(3)
	forwardDrive()
	sleep(3)
	reverseDrive()
	sleep(3)
	spinLeft()
	sleep(3)
	SpinRight()
	sleep(3)
	forwardTurnLeft()
	sleep(3)
	forwardTurnRight()
	sleep(3)
	reverseTurnLeft()
	sleep(3)
	reverseTurnRight()
	sleep(3)
	

if __name__ == "__main__":
	while(True):
		main()
  
