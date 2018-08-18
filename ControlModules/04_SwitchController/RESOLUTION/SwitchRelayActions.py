import RPi.GPIO as GPIO
# The script as below using BCM GPIO 00..nn numbers
GPIO.setmode(GPIO.BCM)

class SwitchRelayActions(object): 
	def TurnOnSwitch(self, gpioPort):
		print('FUNCTION: TurnOnSwitch')
		GPIO.setup(gpioPort, GPIO.OUT)
		GPIO.output(gpioPort, GPIO.LOW)

	def TurnOffSwitch(self, gpioPort):
		print('FUNCTION: TurnOffSwitch')	
		GPIO.setup(gpioPort, GPIO.OUT)
		GPIO.output(gpioPort, GPIO.HIGH)		