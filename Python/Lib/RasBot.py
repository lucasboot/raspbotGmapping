import RPi.GPIO as gpio
from time import sleep

class RasBot:
	def __init__(self, _PRINT_DEBUG = False, mLF_port = 11, mLB_port = 12, mRF_port = 13, mRB_port = 15):
		self.PRINT_DEBUG = _PRINT_DEBUG
		if not self.PRINT_DEBUG:
			gpio.setwarnings(False)
		gpio.cleanup()
		gpio.setmode(gpio.BOARD)
		self.m_LF_port = mLF_port
		self.m_LB_port = mLB_port
		self.m_RF_port = mRF_port
		self.m_RB_port = mRB_port
		gpio.setup(self.m_LF_port, gpio.OUT)
		gpio.setup(self.m_LB_port, gpio.OUT)
		gpio.setup(self.m_RF_port, gpio.OUT)
		gpio.setup(self.m_RB_port, gpio.OUT)
		self.mLF = gpio.PWM(self.m_LF_port, 100)
		self.mLB = gpio.PWM(self.m_LB_port, 100)
		self.mRF = gpio.PWM(self.m_RF_port, 100)
		self.mRB = gpio.PWM(self.m_RB_port, 100)
		self.mLF.start(0)
		self.mLB.start(0)
		self.mRF.start(0)
		self.mRB.start(0)
	def __del__(self):
		self.stop()
		gpio.cleanup()

	def setPorts(self, mLF_port, mLB_port, mRF_port, mRB_port):
		gpio.cleanup()
		gpio.setmode(gpio.BOARD)
		self.m_LF_port = mLF_port
		self.m_LB_port = mLB_port
		self.m_RF_port = mRF_port
		self.m_RB_port = mRB_port
		gpio.setup(self.m_LF_port, gpio.OUT)
		gpio.setup(self.m_LB_port, gpio.OUT)
		gpio.setup(self.m_RF_port, gpio.OUT)
		gpio.setup(self.m_RB_port, gpio.OUT)
		self.mLF = gpio.PWM(self.m_LF_port, 100)
		self.mLB = gpio.PWM(self.m_LB_port, 100)
		self.mRF = gpio.PWM(self.m_RF_port, 100)
		self.mRB = gpio.PWM(self.m_RB_port, 100)
		self.mLF.start(0)
		self.mLB.start(0)
		self.mRF.start(0)
		self.mRB.start(0)

	def stop(self):
		if self.PRINT_DEBUG:
			print('>> Stop')
		self.mLF.ChangeDutyCycle(0)
		self.mLB.ChangeDutyCycle(0)
		self.mRF.ChangeDutyCycle(0)
		self.mRB.ChangeDutyCycle(0)
		sleep(0.02)

	def motorL(self, direction, relative_velocity):
		if direction:
			self.mLB.ChangeDutyCycle(0)
			self.mLF.ChangeDutyCycle(relative_velocity)
			if self.PRINT_DEBUG:
				print('> L:  {}'.format(relative_velocity))
		else:
			self.mLF.ChangeDutyCycle(0)
			self.mLB.ChangeDutyCycle(relative_velocity)
			if self.PRINT_DEBUG:
				print('> L: -{}'.format(relative_velocity))

	def motorR(self, direction, relative_velocity):
		if direction:
			self.mRB.ChangeDutyCycle(0)
			self.mRF.ChangeDutyCycle(relative_velocity)
			if self.PRINT_DEBUG:
				print('> R:  {}'.format(relative_velocity))
		else:
			self.mRF.ChangeDutyCycle(0)
			self.mRB.ChangeDutyCycle(relative_velocity)
			if self.PRINT_DEBUG:
				print('> R: -{}'.format(relative_velocity))

	def moveF(self, relative_velocity):
		if self.PRINT_DEBUG:
			print('>> Forward')
		self.motorL(1,relative_velocity)
		self.motorR(1,relative_velocity)

	def moveB(self, relative_velocity):
		if self.PRINT_DEBUG:
			print('>> Backward')
		self.motorL(0,relative_velocity)
		self.motorR(0,relative_velocity)

	def turnL(self, relative_velocity):
		if self.PRINT_DEBUG:
			print('>> Left')
		self.motorL(0,relative_velocity)
		self.motorR(1,relative_velocity)

	def turnR(self, relative_velocity):
		if self.PRINT_DEBUG:
			print('>> Right')
		self.motorL(1,relative_velocity)
		self.motorR(0,relative_velocity)
