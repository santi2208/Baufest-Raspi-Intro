import RPi.GPIO as GPIO
import time
# The script as below using BCM GPIO 00..nn numbers

class ServoActions(object):
	def Deg0(self, gpioPort):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(gpioPort,GPIO.OUT)
		pwm = GPIO.PWM(gpioPort,50) 
		pwm.start(7.5)	
		pwm.ChangeDutyCycle(12.5) 
		time.sleep(0.60)	
		pwm.stop()
		
	def Deg45(self, gpioPort):
		print('NotImplemented')
		
	def Deg90(self, gpioPort):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(gpioPort,GPIO.OUT)
		pwm = GPIO.PWM(gpioPort,50) 
		pwm.start(7.5)	
		pwm.ChangeDutyCycle(7.5)
		time.sleep(0.60)			
		pwm.stop()
		
	def Deg135(self, gpioPort):
		print('NotImplemented')
		
	def Deg180(self, gpioPort):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(gpioPort,GPIO.OUT)
		pwm = GPIO.PWM(gpioPort,50) 
		pwm.start(7.5)	

		pwm.ChangeDutyCycle(2.5)		
		time.sleep(0.60)
		pwm.stop()
		
	def ScanOn(self, gpioPort):
		print('NotImplemented')
		
	def ScanOff(self, gpioPort):		
		print('NotImplemented')