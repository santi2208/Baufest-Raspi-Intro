#RESOLUCION 01 - Led
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

ledRojo = 14
ledAmarillo = 12 
ledVerde = 16
GPIO.setup(ledRojo, GPIO.OUT) 
GPIO.setup(ledAmarillo, GPIO.OUT) 
GPIO.setup(ledVerde, GPIO.OUT) 

def Main():
	FlashLeds()
	DimLeds()

def TestLed(gpioPort):
	GPIO.output(gpioPort, GPIO.HIGH)
	time.sleep(0.045)
	GPIO.output(gpioPort, GPIO.LOW)

def FlashLeds():
	try:
		for i in range(30):
			TestLed(ledRojo)
			TestLed(ledAmarillo)
			TestLed(ledVerde)
	except (KeyboardInterrupt, SystemExit):
		raise

def DimLeds():
	p = GPIO.PWM(ledVerde, 50)
	p.start(0)
	am = GPIO.PWM(ledAmarillo, 50)
	am.start(0)
	rd = GPIO.PWM(ledRojo, 50)
	rd.start(0)
	try:
		for a in range(3):
			for i in range(100):
				p.ChangeDutyCycle(i)
				am.ChangeDutyCycle(i)
				rd.ChangeDutyCycle(i)
				time.sleep(0.02)
			for i in range(100):
				p.ChangeDutyCycle(100 - i)
				am.ChangeDutyCycle(100 - i)
				rd.ChangeDutyCycle(100 - i)
				time.sleep(0.02)
				
	except KeyboardInterrupt:
		pass
	p.stop()
	am.stop()
	rd.stop()
	GPIO.cleanup()

Main()
