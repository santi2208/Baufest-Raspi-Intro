import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN) #RELAY 1
GPIO.setup(17, GPIO.IN) #MOVE
GPIO.setup(12, GPIO.IN) #LED
GPIO.setup(14, GPIO.IN) #LED
GPIO.setup(16, GPIO.IN) #LED
GPIO.setup(5, GPIO.IN)  #SERVO
#GPIO.setup(23, GPIO.IN) #TRIGGER

class GpioReader(object):
    def __init__(self, teamNumber):
        self.teamNumber = teamNumber
    
    def ReadAllOnce(self):
        gpios = [20, 17, 12, 14, 16, 5]
        result = []
        for gNumber in gpios:
            gValue = GPIO.input(gNumber)
            result.append([self.teamNumber, gNumber, gValue])
        return result