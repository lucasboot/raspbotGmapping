from gpiozero import DigitalInputDevice
import time
from gpiozero import PWMOutputDevice
from time import sleep
import numpy

# Motor A, Left Side GPIO CONSTANTS
PWM_FORWARD_LEFT_PIN = 26	# GPIO26- Pra frente
PWM_REVERSE_LEFT_PIN = 19	# GPIO19 - Pra tras
# Motor B, Right Side GPIO CONSTANTS
PWM_FORWARD_RIGHT_PIN = 6	# GPIO06 
PWM_REVERSE_RIGHT_PIN = 13	# GPIO13 


encoder1 = DigitalInputDevice(21)
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

def forwardDrive(valor:
	print("Para frente")
	forwardLeft.value = 0.0
	reverseLeft.value = valor
	forwardRight.value = 0.0
	reverseRight.value = valor

def main():
    cont = 0
    vet = []
    start = time.time()
    for i in numpy.arange(0.5,1, 0.05):
        forwardDrive(i)
        while time.time() < start +4:
                encoder1.wait_for_active()
                cont = cont +1
                encoder1.wait_for_inactive()
        vet.append(cont1)
        cont = 0
    for v in vet:
        print(v)



if __name__ == "__main__":
		main()
  
