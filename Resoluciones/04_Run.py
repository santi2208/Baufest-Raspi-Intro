#RESOLUCION 04 - Relay
import time
import sys
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

relayPort = 20

def Main():
    try:
		GPIO.setup(relayPort, GPIO.OUT)
		GPIO.output(relayPort, GPIO.HIGH)
		time.sleep(5)
		GPIO.output(relayPort, GPIO.LOW)
    except (KeyboardInterrupt, SystemExit):
        raise
    finally:  
        GPIO.cleanup() 
		
Main()