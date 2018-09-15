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
	#COMPLETAR

def Deg90(gpioPort):
	#COMPLETAR

def Deg180(gpioPort):
	#COMPLETAR

Main()