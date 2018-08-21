import math
import time
import VL53L0X
from gpiozero import Servo
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
# Create a VL53L0X object
tof = VL53L0X.VL53L0X(i2c_bus=1,i2c_address=0x29)
# I2C Address can change before tof.open()
# tof.change_address(0x32)
tof.open()
# Start ranging


myGPIO=17 #5V e GND
myCorrection=0.45
maxPW=(2.0+myCorrection)/1000
minPW=(1.0-myCorrection)/1000
myServo = Servo(myGPIO,min_pulse_width=minPW,max_pulse_width=maxPW)
tof.start_ranging(VL53L0X.Vl53l0xAccuracyMode.BETTER)
arq = open("lidar.csv", "w+")
timing = tof.get_timing()
if timing < 20000:
    timing = 20000
print("Timing %d ms" % (timing/1000))
start = time.time()
cont = 0
value = 3.0

for i in numpy.arange(3,17,0.3):
    arq.write(str((((math.pi*i)/20)*180)/math.pi))
    arq.write(",")
arq.write("\n")
if os.name != 'nt':
    settings = termios.tcgetattr(sys.stdin)
while True:
    key = getKey()
    if (key == 'g' ):
		arq.close() 
		break
    distance = tof.get_distance()
    value2=(float(value)-10)/10.0 
    myServo.value=value2
    value = value + 0.3 
    arq.write(str(distance)+ " ")
    if(value >= 17.0):
        value = 3.0
        arq.write("\n")
    time.sleep(0.01)
arq.close()
tof.stop_ranging()
tof.close()
'''
    
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
