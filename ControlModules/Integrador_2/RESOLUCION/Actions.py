import RPi.GPIO as GPIO
import time
# The script as below using BCM GPIO 00..nn numbers
GPIO.setmode(GPIO.BCM)
fullSeq = [[1,0,0,0], [1,1,0,0], [0,1,0,0], [0,1,1,0], [0,0,1,0], [0,0,1,1], [0,0,0,1], [1,0,0,1]]

class Actions(object): 
    #--------RELAY ACTIONS---------------
	def TurnOnSwitch(self, gpioPort):
		print('FUNCTION: TurnOnSwitch')
		GPIO.setup(gpioPort, GPIO.OUT)
		GPIO.output(gpioPort, GPIO.LOW)

	def TurnOffSwitch(self, gpioPort):
		print('FUNCTION: TurnOffSwitch')	
		GPIO.setup(gpioPort, GPIO.OUT)
		GPIO.output(gpioPort, GPIO.HIGH)		

    #--------STEPPER ACTIONS---------------
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
    
    #--------SERVO ACTIONS---------------
	def Deg0(self, gpioPort):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(gpioPort,GPIO.OUT)
		pwm = GPIO.PWM(gpioPort,50) 
		pwm.start(7.5)	
		pwm.ChangeDutyCycle(12.5) 
		time.sleep(0.60)	
		pwm.stop()
		
	def Deg90(self, gpioPort):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(gpioPort,GPIO.OUT)
		pwm = GPIO.PWM(gpioPort,50) 
		pwm.start(7.5)	
		pwm.ChangeDutyCycle(7.5)
		time.sleep(0.60)			
		pwm.stop()
		
	def Deg180(self, gpioPort):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(gpioPort,GPIO.OUT)
		pwm = GPIO.PWM(gpioPort,50) 
		pwm.start(7.5)	

		pwm.ChangeDutyCycle(2.5)		
		time.sleep(0.60)
		pwm.stop()

	def LedOn(self, led):
		GPIO.setup(led, GPIO.OUT)
		GPIO.output(led, GPIO.HIGH)

	def LedOff(self, led):
		GPIO.setup(led, GPIO.OUT)
		GPIO.output(led, GPIO.LOW)