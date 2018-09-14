import sys
import RPi.GPIO as GPIO
import time
import argparse
from DistanceActions import *
from MovementActions import *

GPIO.setmode(GPIO.BCM)
ledRojo = 14
ledAmarillo = 12 
ledVerde = 16
servo = 5
trigger = 24
echo = 23
movPort = 17
relayPort = 20

class Test(object):

    def Main(self, opt):
        if(opt == 1): #Led Rojo
            self.TestLed(ledRojo)
        if(opt == 2):
            self.TestLed(ledVerde)
        if(opt == 3):
            self.TestLed(ledAmarillo)
        if(opt == 4):
            self.TestServo(servo)            
        if(opt == 5):
            self.TestDistancia(trigger, echo)
        if(opt == 6):
            self.TestMovimiento(movPort)
        if(opt == 7):
            self.TestRelay(relayPort)

        
    def TestLed(self, gpioPort):
        GPIO.setup(gpioPort, GPIO.OUT) 
        GPIO.output(gpioPort, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(gpioPort, GPIO.LOW)
    
    def TestServo(self, gpioPort):
        self.Deg0(gpioPort)
        time.sleep(5)
        self.Deg180(gpioPort)
    
    def TestDistancia(self, trigger, echo):
        try:
            distanceActions = DistanceActions()
            while 1:
                distance = distanceActions.TakeDistance(echo,trigger)
                print(distance)
                time.sleep(0.3)
        except (KeyboardInterrupt, SystemExit):
            raise
        finally:  
            GPIO.cleanup() 

    def TestMovimiento(self, gpioPort):
        try:
            print("Movemente Test Started")
            GPIO.setup(gpioPort, GPIO.IN) 
            while True:
                moved = self.DetectMovementOnce(gpioPort)
                if(moved):
                    print("Se movio algo.")
                    time.sleep(3)
        except (KeyboardInterrupt, SystemExit):
            raise
        finally:  
            GPIO.cleanup() 		

    def TestRelay(self, gpioPort):
        GPIO.setup(gpioPort, GPIO.OUT)
        GPIO.output(gpioPort, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(gpioPort, GPIO.LOW)

    def Deg0(self, gpioPort):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(gpioPort,GPIO.OUT)
        pwm = GPIO.PWM(gpioPort,50) 
        pwm.start(7.5)	
        pwm.ChangeDutyCycle(12.5) 
        time.sleep(0.60)	
        pwm.stop()

    def Deg180(self, gpioPort):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(gpioPort,GPIO.OUT)
        pwm = GPIO.PWM(gpioPort,50) 
        pwm.start(7.5)	

        pwm.ChangeDutyCycle(2.5)		
        time.sleep(0.60)
        pwm.stop()
    
    def DetectMovementOnce(self, gpioPort):
        while True:
            i = GPIO.input(gpioPort)
            print(i)
            # if i == 0:
            #     return True
            time.sleep(0.3)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', help='1: Led Rojo || 2: Led Verde || 3: Led Amarillo || 4: Servo || 5: Distancia || 6: Movimiento || 7: Relay')
    args = parser.parse_args()    
    opt = int(args.test)
    service = Test()
    service.Main(opt)