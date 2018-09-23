#RESOLUCION Integrador 1 Corte 2 - Movimiento
import RPi.GPIO as GPIO
import time

ledRojo = 14
ledAmarillo = 12 
ledVerde = 16
move = 17
relayPort = 20

GPIO.setmode(GPIO.BCM)

GPIO.setup(ledRojo, GPIO.OUT)
GPIO.setup(ledAmarillo, GPIO.OUT)
GPIO.setup(ledVerde, GPIO.OUT)
GPIO.setup(move, GPIO.IN) 
GPIO.setup(relayPort, GPIO.OUT) 

def DetectMovementOnce():
    while True:
        i = GPIO.input(move)
        if i == 1:
            return True
        time.sleep(1.4)

def Main():
    try:    
        while True:
            moved = DetectMovementOnce()
            if(moved):
                print("Se movio algo.")
                GPIO.output(ledRojo, GPIO.HIGH)
                GPIO.output(ledAmarillo, GPIO.HIGH)
                GPIO.output(ledVerde, GPIO.HIGH)
                GPIO.output(relayPort, GPIO.HIGH)
                time.sleep(3)
            GPIO.output(ledRojo, GPIO.LOW)    
            GPIO.output(ledAmarillo, GPIO.LOW)
            GPIO.output(ledVerde, GPIO.LOW)
            GPIO.output(relayPort, GPIO.LOW)
    except (KeyboardInterrupt, SystemExit):
        raise
    finally:  
        GPIO.cleanup() 		

Main()