
from gpiozero import PWMOutputDevice
from time import sleep

#///////////////// Definir os pinos dos motores /////////////////
# Motor A, Left Side GPIO CONSTANTS
PWM_FORWARD_LEFT_PIN = 26	# IN1 - Pra frente
PWM_REVERSE_LEFT_PIN = 19	# IN2 - Pra trás
# Motor B, Right Side GPIO CONSTANTS
PWM_FORWARD_RIGHT_PIN = 6	# IN1 
PWM_REVERSE_RIGHT_PIN = 13	# IN2  

# Initialise objects for H-Bridge PWM pins
# Inicializar o  duty cycle em 0 e a frequência em 1000
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
  forwardLeft.value = 1.0
  reverseLeft.value = 0
  forwardRight.value = 1.0
  reverseRight.value = 0

def reverseDrive():
  print("Para tras")
  forwardLeft.value = 0
  reverseLeft.value = 1.0
  forwardRight.value = 0
  reverseRight.value = 1.0

def spinLeft():
  print("Girar para esquerda")
  forwardLeft.value = 0
  reverseLeft.value = 1.0
  forwardRight.value = 1.0
  reverseRight.value = 0

def SpinRight():
  print("Girar para direita")
  forwardLeft.value = 1.0
  reverseLeft.value = 0
  forwardRight.value = 0 
  reverseRight.value = 1.0

def forwardTurnLeft():
  print("Noroeste")
  forwardLeft.value = 0.2
  reverseLeft.value = 0
  forwardRight.value = 0.8
  reverseRight.value = 0

def forwardTurnRight():
  print("Nordeste")
  forwardLeft.value = 0.8
  reverseLeft.value = 0
  forwardRight.value = 0.2
  reverseRight.value = 0

def reverseTurnLeft():
  print("Sudoeste")
  forwardLeft.value = 0
  reverseLeft.value = 0.2
  forwardRight.value = 0
  reverseRight.value = 0.8

def reverseTurnRight():
  print("Sudeste")
  forwardLeft.value = 0
  reverseLeft.value = 0.8
  forwardRight.value = 0
  reverseRight.value = 0.2

def main():
  allStop()
  forwardDrive()
  sleep(7)
  reverseDrive()
  sleep(7)
  spinLeft()
  sleep(7)
  SpinRight()
  sleep(7)
  forwardTurnLeft()
  sleep(7)
  forwardTurnRight()
  sleep(7)
  reverseTurnLeft()
  sleep(7)
  reverseTurnRight()
  sleep(7)
  allStop()


if __name__ == "__main__":
  main()
