import sys
sys.path.append('../../Services/UDPService/')
from UDPService import *
from CommandConstants import GetActionName
from CommandConstants import GetGpioPort
from StepperActions import *

class MainStepperController(object):
	def __init__(self, udpService = None):
		if udpService:
    			self.udpService = udpService
		else:	
			self.udpService = UDPService()
	
	def RunStepperService(self, portNumber, host = None):
		try:
			print("Stepper Controller running...")
		
		except (KeyboardInterrupt, SystemExit):
			raise
		except:
			traceback.print_exc()
		finally:  
			GPIO.cleanup() 
		
if __name__ == '__main__':
	port = int(sys.argv[1])
	mainStepperController = MainStepperController()
	mainStepperController.RunStepperService(port, sys.argv[2] if len(sys.argv) > 1 else None)