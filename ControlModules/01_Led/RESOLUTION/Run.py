import sys
sys.path.append('../../../Services/UDPService/')
from UDPService import *
from LedActions import *
from CommandConstants import GetActionName
from CommandConstants import GetGpioPort

class MainLedController(object):
	def __init__(self, udpService = None):
		if udpService:
			self.udpService = udpService
		else:	
			self.udpService = UDPService()

	def RunLedService(self, portNumber, host = None):
		try:	
			print("Led Controller running...")
			while 1:
				# Receive UDP Params
				udpRawAction = self.udpService.ListenToPortOnce(portNumber, host)
				actionName = udpRawAction.split('#')[0]
				ledName = udpRawAction.split('#')[1]
				functionName = GetActionName(actionName)
				gpioNumber = GetGpioPort(ledName)
				if(functionName is not None and gpioNumber is not None):
					gpioNumber = int(gpioNumber) 
					# Execute Action
					ledActions = LedActions()
					getattr(ledActions,functionName)(gpioNumber)
					print functionName
		except (KeyboardInterrupt, SystemExit):
			raise
		except:
			traceback.print_exc()
		finally:  
			GPIO.cleanup() 

if __name__ == '__main__':
	port = int(sys.argv[1])
	mainLedController = MainLedController()
	mainLedController.RunLedService(port, sys.argv[2] if len(sys.argv) > 1 else None)