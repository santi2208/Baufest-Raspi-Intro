import RPi.GPIO as GPIO
import time

ledRojo = 14
ledAmarillo = 12 
ledVerde = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledRojo, GPIO.OUT)
GPIO.setup(ledAmarillo, GPIO.OUT)
GPIO.setup(ledVerde, GPIO.OUT)

def Main():
    try:
        GPIO.output(ledRojo, GPIO.HIGH)
        GPIO.output(ledAmarillo, GPIO.HIGH)
        GPIO.output(ledVerde, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(ledRojo, GPIO.LOW)
        GPIO.output(ledAmarillo, GPIO.LOW)
        GPIO.output(ledVerde, GPIO.LOW)
    except (KeyboardInterrupt, SystemExit):
        raise
    finally:  
        GPIO.cleanup() 		

Main()