#pin 03 do rasp, ligar no pino 5V dele (primeiro da borda)
import RPi.GPIO as GPIO
import time
'''comandos para configurar as portas dos motores'''
GPIO.setmode(GPIO.BOARD)
GPIO.setup(03, GPIO.OUT) 
pwm = GPIO.PWM(03, 50)
pwm.start(0.0)
GPIO.setwarnings(False)

'''comportamento'''
try:
    while True:
        pwm.ChangeDutyCycle(2.5) 
        print("posicao 1")
        time.sleep(3) # sleep 3 secs
        pwm.ChangeDutyCycle(4.0)  
        print("posicao 2")
        time.sleep(3)
        pwm.ChangeDutyCycle(5.5)  
        print("posicao 3")
        time.sleep(3)
        pwm.ChangeDutyCycle(7.0)
        print("posicao 4")
        time.sleep(3) 
        pwm.ChangeDutyCycle(8.5)
        print("posicao 5")
        time.sleep(3)
        pwm.ChangeDutyCycle(7.0) 
        print("posicao 4")
        time.sleep(3) 
        pwm.ChangeDutyCycle(5.5)  
        print("posicao 3")
        time.sleep(3)
        pwm.ChangeDutyCycle(4.0)  
        print("posicao 2")
        time.sleep(3)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
