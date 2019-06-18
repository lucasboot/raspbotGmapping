from gpiozero import DigitalInputDevice

encoder1 = DigitalInputDevice(20)
cont1 = 0
def contando():
        global cont1
        cont1 = cont1 +1
        print cont1

while True:
        encoder1.wait_for_active()
        global cont1
        cont1 = cont1 +1
        print cont1
        encoder1.wait_for_inactive()




