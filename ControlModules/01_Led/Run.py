import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

ledRojo = 14
ledAmarillo = 12 
ledVerde = 16

def Main():
	try:
		#COMPLETAR
	except (KeyboardInterrupt, SystemExit):
		raise
	finally:  
		GPIO.cleanup() 		

Main()