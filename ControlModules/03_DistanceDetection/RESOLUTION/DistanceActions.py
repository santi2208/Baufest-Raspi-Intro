import RPi.GPIO as GPIO
import time
# The script as below using BCM GPIO 00..nn numbers
GPIO.setmode(GPIO.BCM)

class DistanceActions(object):
	def TakeDistanceOnce(self, gpioEcho, gpioTrigger):
		GPIO.setup(gpioTrigger, GPIO.OUT)
		GPIO.setup(gpioEcho, GPIO.IN)
		return self.TakeDistance(gpioTrigger, gpioEcho)
	
	def TakeDistance(self, GPIO_TRIGGER, GPIO_ECHO):
		# set Trigger to HIGH
		GPIO.output(GPIO_TRIGGER, True)
	 
		# set Trigger after 0.01ms to LOW
		time.sleep(0.00001)
		GPIO.output(GPIO_TRIGGER, False)
	 
		StartTime = time.time()
		StopTime = time.time()
	 
		# save StartTime
		while GPIO.input(GPIO_ECHO) == 0:
			StartTime = time.time()
	 
		# save time of arrival
		while GPIO.input(GPIO_ECHO) == 1:
			StopTime = time.time()
	 
		# time difference between start and arrival
		TimeElapsed = StopTime - StartTime
		# multiply with the sonic speed (34300 cm/s)
		# and divide by 2, because there and back
		distance = (TimeElapsed * 34300) / 2
	 
		return distance