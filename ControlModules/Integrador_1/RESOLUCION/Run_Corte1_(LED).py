import RPi.GPIO as GPIO
import time

led = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

def Main():
    GPIO.output(led, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(led, GPIO.LOW)

Main()