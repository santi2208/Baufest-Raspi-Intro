import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN) #RELAY 1
GPIO.setup(21, GPIO.IN) #RELAY 2
GPIO.setup(17, GPIO.IN) #MOVE
GPIO.setup(14, GPIO.IN) #LED
GPIO.setup(6, GPIO.IN)  #STEPPER
GPIO.setup(13, GPIO.IN) #STEPPER
GPIO.setup(19, GPIO.IN) #STEPPER
GPIO.setup(26, GPIO.IN) #STEPPER
GPIO.setup(5, GPIO.IN)  #SERVO

class GpioReader(object):
    def __init__(self, teamNumber):
        self.teamNumber = teamNumber
    
    def ReadAllOnce(self):
        gpios = [20, 21, 17, 14, 6, 13, 19, 26, 5]
        result = []
        for gNumber in gpios:
            gValue = GPIO.input(gNumber)
            result.append([self.teamNumber, gNumber, gValue])
        return result