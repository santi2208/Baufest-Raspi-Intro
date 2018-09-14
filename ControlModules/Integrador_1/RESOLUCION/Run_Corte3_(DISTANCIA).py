import RPi.GPIO as GPIO
import time
from DistanceActions import *

trigger = 24
echo = 23
minDistance = 10
midDistance = 20
maxDistance = 30

ledRojo = 14
ledAmarillo = 12 
ledVerde = 16

GPIO.setmode(GPIO.BCM)

GPIO.setup(ledRojo, GPIO.OUT)
GPIO.setup(ledAmarillo, GPIO.OUT)
GPIO.setup(ledVerde, GPIO.OUT)

def Main():
    try:    
        distanceActions = DistanceActions(trigger, echo)
        while True:
            distance = distanceActions.TakeDistance()
            print(distance)
            if(distance <= minDistance):
                GPIO.output(ledRojo, GPIO.HIGH)
                GPIO.output(ledAmarillo, GPIO.LOW)
                GPIO.output(ledVerde, GPIO.LOW)
            else:
                if(distance >= minDistance and distance <= midDistance):
                    GPIO.output(ledRojo, GPIO.LOW)
                    GPIO.output(ledAmarillo, GPIO.HIGH)
                    GPIO.output(ledVerde, GPIO.LOW)
                else:
                    GPIO.output(ledRojo, GPIO.LOW)
                    GPIO.output(ledAmarillo, GPIO.LOW)
                    GPIO.output(ledVerde, GPIO.HIGH)
            time.sleep(0.3)
    except (KeyboardInterrupt, SystemExit):
        raise
    finally:  
        GPIO.cleanup() 		
Main() 