import RPi.GPIO as gpio
from time import sleep

class WheelControl:
    def __init__(self, _PRINT_DEBUG = False, mLF_port = 11, mLB_port = 12, mRF_port = 13, mRB_port = 15):
