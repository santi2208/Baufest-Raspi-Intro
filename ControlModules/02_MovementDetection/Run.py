import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

def Main():
	try:
		print("Movement Test Started...")
		while 1:
	
			# print("Se movio algo.")
			# time.sleep(3)
	except (KeyboardInterrupt, SystemExit):
		raise
	finally:  
		GPIO.cleanup() 		

Main()