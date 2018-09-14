import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

ledRojo = 14
ledAmarillo = 12 
ledVerde = 16

def Main():
	try:
		TestLed(ledRojo)
		TestLed(ledAmarillo)
		TestLed(ledVerde)
	except (KeyboardInterrupt, SystemExit):
		raise
	finally:  
		GPIO.cleanup() 		

def TestLed(gpioPort):
	GPIO.setup(gpioPort, GPIO.OUT) 
	GPIO.output(gpioPort, GPIO.HIGH)
	time.sleep(5)
	GPIO.output(gpioPort, GPIO.LOW)

Main()