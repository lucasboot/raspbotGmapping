from gpiozero import PWMOutputDevice
from time import sleep

# Motor A, Left Side GPIO CONSTANTS
PWM_FORWARD_LEFT_PIN = 26       # GPIO26- Pra frente
PWM_REVERSE_LEFT_PIN = 19       # GPIO19 - Pra tras
# Motor B, Right Side GPIO CONSTANTS
PWM_FORWARD_RIGHT_PIN = 6       # GPIO06 
PWM_REVERSE_RIGHT_PIN = 13      # GPIO13 


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

allStop()
