import time
import sys
from DistanceActions import *

def Main():
	try:
		trigger = int(sys.argv[1])
		echo = int(sys.argv[2])
		distanceActions = DistanceActions()
		while 1:
			distance = distanceActions.TakeDistance(echo,trigger)
			print(distance)
			time.sleep(0.3)
	except (KeyboardInterrupt, SystemExit):
		raise
	except:
		traceback.print_exc()
	finally:  
		GPIO.cleanup() 
		
Main()