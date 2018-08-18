import RPi.GPIO as GPIO
import time
# The script as below using BCM GPIO 00..nn numbers
GPIO.setmode(GPIO.BCM)

class LedActions(object):
    def LedON(self, gpioPort):
        GPIO.setup(gpioPort, GPIO.OUT) 
        GPIO.output(gpioPort, GPIO.HIGH)

    def LedOFF(self, gpioPort):
        GPIO.setup(gpioPort, GPIO.OUT) 
        GPIO.output(gpioPort, GPIO.LOW)