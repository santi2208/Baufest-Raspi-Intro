import RPi.GPIO as GPIO
import time

led = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
move = 17
GPIO.setup(move, GPIO.IN) 

def DetectMovementOnce():
    while True:
        i = GPIO.input(move)
        if i == 1:
            return True
        time.sleep(1.4)

def Main():
    while True:
        moved = DetectMovementOnce()
        if(moved):
            print("Se movio algo.")
            GPIO.output(led, GPIO.HIGH)
            time.sleep(3)
        GPIO.output(led, GPIO.LOW)    
Main()