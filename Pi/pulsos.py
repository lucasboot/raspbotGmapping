from gpiozero import DigitalInputDevice
import time
from gpiozero import PWMOutputDevice
from time import sleep
import numpy

# Motor A, Left Side GPIO CONSTANTS
PWM_FORWARD_LEFT_PIN = 26	# GPIO26- Pra frente
PWM_REVERSE_LEFT_PIN = 19	# GPIO19 - Pra tras


encoder1 = DigitalInputDevice(20)
forwardLeft = PWMOutputDevice(PWM_FORWARD_LEFT_PIN, True, 0, 1000)
reverseLeft = PWMOutputDevice(PWM_REVERSE_LEFT_PIN, True, 0, 1000)

def allStop():
	print("Parando")
	forwardLeft.value = 0
	reverseLeft.value = 0

def forwardDrive(valor):
	print("Para frente")
	forwardLeft.value = valor
	reverseLeft.value =  0.0

def main():
	while True:
		forwardDrive(1.0)
'''
    arq = open("dados.txt", "w")
    cont = 0
    vet = []
    for i in numpy.arange(0.5,1, 0.04):
	start = time.time()
        forwardDrive(i)
        while time.time() < start +4:
                encoder1.wait_for_active()
                cont = cont +1
                encoder1.wait_for_inactive()
	vet.append(i)
        vet.append(cont)
	arq.write(str(i))
	arq.write(", ")
	arq.write(str(cont))
	arq.write("\n")
        cont = 0
    arq.close()
    for v in vet:
        print(v)
'''


if __name__ == "__main__":
		main()
  
