import time
import VL53L0X

# Create a VL53L0X object
tof = VL53L0X.VL53L0X(i2c_bus=1,i2c_address=0x29)
# I2C Address can change before tof.open()
# tof.change_address(0x32)
tof.open()
# Start ranging
tof.start_ranging(VL53L0X.Vl53l0xAccuracyMode.BETTER)

timing = tof.get_timing()
if timing < 20000:
    timing = 20000
print("Timing %d ms" % (timing/1000))
start = time.time()
cont = 0
while time.time() < start +1:
    distance = tof.get_distance()
    if distance > 0:
        print(distance/10)
        cont = cont + 1
    time.sleep(timing/1000000.00)
print (cont)
tof.stop_ranging()
tof.close()