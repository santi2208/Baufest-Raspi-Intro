import time
import sys
from MovementActions import *

def Main():
	try:
		print("Movemente Test Started")
		gpioPort = int(sys.argv[1]) #14
		movementActions = MovementActions()
		while 1:
			i = movementActions.DetectMovementOnce(gpioPort)
			if i:
				print("Se movio algo.")
				time.sleep(3)
	except (KeyboardInterrupt, SystemExit):
		raise
	except:
		traceback.print_exc()
	finally:  
		GPIO.cleanup() 		

Main()