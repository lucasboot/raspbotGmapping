from RasBot import RasBot
from time import sleep

# Delete the "True" parameter if you don't want debug mensages from the class RasBot
robot = RasBot(True)

# The values to the methods must be between 0 - 100 (0% - 100%)
robot.moveF(80)
sleep(1)
robot.moveB(80)
sleep(1)
robot.turnL(50)
sleep(1)
robot.turnR(50)
sleep(1)
robot.stop()
