import time
import sys
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

relayPort = 20

def Main():
    try:
		#COMPLETAR
    except (KeyboardInterrupt, SystemExit):
        raise
    finally:  
        GPIO.cleanup() 
		
Main()