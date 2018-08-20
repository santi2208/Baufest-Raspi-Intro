import RPi.GPIO as GPIO
import time
from DistanceActions import *

trigger = 23
echo = 24
minDistance = 5
middleDistance = 10

redLed = 14
yellowLed = 12
greenLed = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(redLed, GPIO.OUT)
GPIO.setup(yellowLed, GPIO.OUT)
GPIO.setup(greenLed, GPIO.OUT)

def Main():
    distanceActions = DistanceActions(echo, trigger)
    while True:
        distance = distanceActions.TakeDistance()
        print(distance)
        if(distance <= minDistance):
            GPIO.output(redLed, GPIO.HIGH)
            GPIO.output(yellowLed, GPIO.LOW)
            GPIO.output(greenLed, GPIO.LOW)
        else:
            if(distance > minDistance and distance <= middleDistance):
                GPIO.output(redLed, GPIO.LOW)
                GPIO.output(yellowLed, GPIO.HIGH)
                GPIO.output(greenLed, GPIO.LOW)
            else:
                GPIO.output(redLed, GPIO.LOW)
                GPIO.output(yellowLed, GPIO.LOW)
                GPIO.output(greenLed, GPIO.HIGH)
        time.sleep(0.3)
Main() 