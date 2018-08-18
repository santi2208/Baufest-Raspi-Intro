import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN) 
GPIO.setup(21, GPIO.IN) 
GPIO.setup(17, GPIO.IN) 
GPIO.setup(14, GPIO.IN) 

class GpioReader(object):
    def __init__(self, teamNumber):
        self.teamNumber = teamNumber
    
    def ReadAllOnce(self):
        gpios = [20, 21, 17, 14]
        result = []
        for gNumber in gpios:
            gValue = GPIO.input(gNumber)
            result.append([self.teamNumber, gNumber, gValue])
        return result