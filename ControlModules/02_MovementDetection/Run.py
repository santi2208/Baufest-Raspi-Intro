import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

port = 17

def Main():
	try:
		print("Movemente Test Started")
		#COMPLETAR
	except (KeyboardInterrupt, SystemExit):
		raise
	finally:  
		GPIO.cleanup() 		

Main()