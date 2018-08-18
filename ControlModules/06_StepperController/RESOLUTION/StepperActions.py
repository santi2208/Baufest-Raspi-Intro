import RPi.GPIO as GPIO
import time
# The script as below using BCM GPIO 00..nn numbers
GPIO.setmode(GPIO.BCM)
fullSeq = [[1,0,0,0], [1,1,0,0], [0,1,0,0], [0,1,1,0], [0,0,1,0], [0,0,1,1], [0,0,0,1], [1,0,0,1]]

class StepperActions(object):
	def Rotate45(self, gpioNumbers):
		self.SetOutPins(gpioNumbers)
		self.Rotate(64, gpioNumbers)
		
	def Rotate90(self, gpioNumbers):
		self.SetOutPins(gpioNumbers)
		self.Rotate(128, gpioNumbers)
		
	def Rotate135(self, gpioNumbers):
		self.SetOutPins(gpioNumbers)
		self.Rotate(192, gpioNumbers)
		
	def Rotate180(self, gpioNumbers):
		self.SetOutPins(gpioNumbers)
		self.Rotate(256, gpioNumbers)
		
	def Rotate225(self, gpioNumbers):
		self.SetOutPins(gpioNumbers)
		self.Rotate(320, gpioNumbers)
	
	def Rotate270(self, gpioNumbers):
		self.SetOutPins(gpioNumbers)
		self.Rotate(384, gpioNumbers)
	
	def Rotate360(self, gpioNumbers):
		self.SetOutPins(gpioNumbers)
		self.Rotate(512, gpioNumbers)
		
	def Rotate(self, numberOfCycles, gpioNumbers):
		for i in range(numberOfCycles):
			for halfstep in range(8):
				for pin in range(4):
					GPIO.output(gpioNumbers[pin], fullSeq[halfstep][pin])
				time.sleep(0.001)
				
	def SetOutPins(self, gpioNumbers):
		for pin in gpioNumbers:
			GPIO.setup(pin, GPIO.OUT)
			GPIO.output(pin,0)