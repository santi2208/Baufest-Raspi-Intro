import RPi.GPIO as GPIO
import time
# The script as below using BCM GPIO 00..nn numbers
GPIO.setmode(GPIO.BCM)

class DistanceActions(object):
	def __init__(self, gpioEcho, gpioTrigger):
		self.Echo = gpioEcho
		self.Trigger = gpioTrigger
		GPIO.setup(gpioTrigger, GPIO.OUT)
		GPIO.setup(gpioEcho, GPIO.IN)

	def TakeDistanceOnce(self):
		return self.TakeDistance(self.Trigger, self.Echo)
	
	def TakeDistance(self):
		# set Trigger to HIGH
		GPIO.output(self.Trigger, True)
	 
		# set Trigger after 0.01ms to LOW
		time.sleep(0.00001)
		GPIO.output(self.Trigger, False)
	 
		StartTime = time.time()
		StopTime = time.time()
	 
		# save StartTime
		while GPIO.input(self.Echo) == 0:
			StartTime = time.time()
	 
		# save time of arrival
		while GPIO.input(self.Echo) == 1:
			StopTime = time.time()
	 
		# time difference between start and arrival
		TimeElapsed = StopTime - StartTime
		# multiply with the sonic speed (34300 cm/s)
		# and divide by 2, because there and back
		distance = (TimeElapsed * 34300) / 2
	 
		return distance