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
			while 1:
				udpRawAction = self.udpService.ListenToPortOnce(portNumber, host)
				actionName = udpRawAction.split('#')[0]
				stepperName = udpRawAction.split('#')[1]
				functionName = GetActionName(actionName)
				gpioNumbers = GetGpioPort(stepperName)
				if(functionName is not None and gpioNumber is not None):				
					gpioNumber = int(gpioNumber) 
					stepperActions = StepperActions()
					getattr(stepperActions,functionName)(gpioNumbers)
					print(functionName)
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