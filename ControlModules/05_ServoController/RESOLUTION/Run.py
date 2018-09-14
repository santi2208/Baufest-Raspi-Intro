import sys
import time
import RPi.GPIO as GPIO

servo = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo,GPIO.OUT)

def Main():
	try:
		print("Servo Controller running...")
		Deg0(servo)
		time.sleep(1)
		Deg90(servo)
		time.sleep(1)
		Deg180(servo)
	except (KeyboardInterrupt, SystemExit):
		raise
	finally:  
		GPIO.cleanup() 

def Deg0(gpioPort):
	pwm = GPIO.PWM(gpioPort,50) 
	pwm.start(7.5)	
	pwm.ChangeDutyCycle(12.5) 
	time.sleep(1)	
	pwm.stop()

def Deg90(gpioPort):
	pwm = GPIO.PWM(gpioPort,50) 	    	
	pwm.start(7.5)	
	pwm.ChangeDutyCycle(7.5)
	time.sleep(1)			
	pwm.stop()

def Deg180(gpioPort):
	pwm = GPIO.PWM(gpioPort,50)     	
	pwm.start(7.5)	
	pwm.ChangeDutyCycle(2.5)		
	time.sleep(1)
	pwm.stop()			

Main()