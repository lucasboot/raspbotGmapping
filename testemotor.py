/**
 * H-bridge module HG7881CP/HG7881CP example code
 * http://diyprojects.eu/how-to-use-h-bridge-hg7881-with-external-power-supply-and-arduino
 */

/**
 * Create variables to be used to run motor A
 */
import RPi.GPIO as GPIO
from time import sleep
Motor1A = 16 //Raspberry digital 8 is connected to HG7881's A-1A terminal
Motor1B = 18 //Raspberry digital 18 is connected to HG7881's A-1B terminal

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)

print ("Para frente")
GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)

sleep(5)

print ("Para tras")
GPIO.output(Motor1A,GPIO.LOW)
GPIO.output(Motor1B,GPIO.HIGH)

sleep (5)

print("Parando...")
GPIO.output(Motor1A, GPIO.LOW)
GPIO.output(Motor1B, GPIO.LOW)
GPIO.cleanup()
sleep(10)