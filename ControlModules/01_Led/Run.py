import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

def Main():
	try:
		print("Movement Test Started...")
		while 1:
			#Prender Led
			time.sleep(1)
			#Apagar Led
	except (KeyboardInterrupt, SystemExit):
		raise
	finally:  
		GPIO.cleanup() 		

Main()