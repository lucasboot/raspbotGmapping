
from gpiozero import PWMOu tputDevice
from time import sleep
import rospy

#///////////////// Definir os pinos dos motores /////////////////
# Motor A, Left Side GPIO CONSTANTS
PWM_FORWARD_LEFT_PIN = 26	# GPIO26- Pra frente
PWM_REVERSE_LEFT_PIN = 19	# GPIO19 - Pra tras
# Motor B, Right Side GPIO CONSTANTS
PWM_FORWARD_RIGHT_PIN = 6	# GPIO06 
PWM_REVERSE_RIGHT_PIN = 13	# GPIO13 

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
  #allStop()
  sub = rospy.Subscriber('distancia', Float64, direcao) #sub para alterar o valor enviado aos motores
  
  '''
  forwardDrive()
  sleep(2)
  reverseDrive()
  sleep(2)
  spinLeft()
  sleep(2)
  SpinRight()
  sleep(2)
  forwardTurnLeft()
  sleep(2)
  forwardTurnRight()
  sleep(2)
  reverseTurnLeft()
  sleep(2)
  reverseTurnRight()
  sleep(2)
  allStop()
  '''

def direcao(data):
  if (data.data < 1):
    reverseDrive()
  else:
    forwardDrive()

if __name__ == "__main__":
   try:
        main()
    except rospy.ROSInterruptException:
        allStop()
        pass
  
