#RESOLUCION 03 - Distance
import time
import sys
from DistanceActions import *

trigger = 24
echo = 23

def Main():
	try:
		distanceActions = DistanceActions(trigger, echo)
		while 1:
			distance = distanceActions.TakeDistance()
			print(distance)
			time.sleep(0.3)
	except (KeyboardInterrupt, SystemExit):
		raise
	finally:  
		GPIO.cleanup() 
		
Main()