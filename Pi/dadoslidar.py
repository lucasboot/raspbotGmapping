import time
import VL53L0X
from gpiozero import Servo

# Create a VL53L0X object
tof = VL53L0X.VL53L0X(i2c_bus=1,i2c_address=0x29)
# I2C Address can change before tof.open()
# tof.change_address(0x32)
tof.open()
# Start ranging
tof.start_ranging(VL53L0X.Vl53l0xAccuracyMode.BETTER)
myServo = Servo(myGPIO,min_pulse_width=minPW,max_pulse_width=maxPW)
arq = open("lidar.csv", "w")

timing = tof.get_timing()
if timing < 20000:
    timing = 20000
print("Timing %d ms" % (timing/1000))
start = time.time()
cont = 0
value = 3.0
while True:
    distance = tof.get_distance()
    value2=(float(value)-10)/10.0 
    myServo.value=value2
	value = value + 0.3 
    if distance > 0:
        print(distance/10)
        time.sleep(timing/1000000.00)
print (cont)
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