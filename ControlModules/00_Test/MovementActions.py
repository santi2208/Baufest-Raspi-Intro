import RPi.GPIO as GPIO
import time
# The script as below using BCM GPIO 00..nn numbers
GPIO.setmode(GPIO.BCM)

class MovementActions(object):
	def DetectMovementOnce(self, gpioPort):
		GPIO.setup(gpioPort, GPIO.IN) 
		while True:
			i = GPIO.input(gpioPort)
			if i == 1:
				return True
			time.sleep(1.4)

	def ReadOnce(self, gpioPort):
		GPIO.setup(gpioPort, GPIO.IN)
		return GPIO.input(gpioPort)	