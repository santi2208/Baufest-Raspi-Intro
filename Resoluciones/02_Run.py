#RESOLUCION 02 - Movement
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

gpioPort = 17

def Main():
	try:
		print("Movemente Test Started")
		GPIO.setup(gpioPort, GPIO.IN) 
		while True:
			i = GPIO.input(gpioPort)
			print(i)
			time.sleep(0.3)
	except (KeyboardInterrupt, SystemExit):
		raise
	finally:  
		GPIO.cleanup() 		

Main()