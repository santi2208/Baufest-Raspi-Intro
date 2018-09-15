import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN) #RELAY 1
GPIO.setup(17, GPIO.IN) #MOVE
GPIO.setup(12, GPIO.IN) #LED AMARILLO
GPIO.setup(14, GPIO.IN) #LED ROJO
GPIO.setup(16, GPIO.IN) #LED VERDE
GPIO.setup(5, GPIO.IN)  #SERVO
#GPIO.setup(23, GPIO.IN) #TRIGGER

class GpioReader(object):
    def __init__(self, teamNumber):
        self.teamNumber = teamNumber
    
    def ReadAllOnce(self, invertirSwitch):
        gpios = [20, 17, 16, 12, 14, 5]
        result = []
        for gNumber in gpios:
            gValue = GPIO.input(gNumber)
            gpioValue = self.InvertNum(gValue) if (gNumber == 20 and invertirSwitch) else gValue
            print("GPIO VALUE: {}".format(gpioValue))
            result.append([self.teamNumber, gNumber, gpioValue])
        return result
    
    def InvertNum(self, num):
        if(num == 1):
            return 0
        if(num == 0):
            return 1