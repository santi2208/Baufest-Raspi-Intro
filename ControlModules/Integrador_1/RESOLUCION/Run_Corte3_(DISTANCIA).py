import RPi.GPIO as GPIO
import time
from DistanceActions import *

trigger = 23
echo = 24
minDistance = 15
led = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

def Main():
    distanceActions = DistanceActions(echo, trigger)
    while True:
        distance = distanceActions.TakeDistance()
        print(distance)
        if(distance <= minDistance):
            GPIO.output(led, GPIO.HIGH)
        else:
            GPIO.output(led, GPIO.LOW)
        time.sleep(0.3)
Main() 