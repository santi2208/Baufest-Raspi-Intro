import sys
sys.path.append('../../Services/UDPService/')
from UDPService import *
from CommandConstants import GetActionName
from CommandConstants import GetGpioPort
from ServoActions import *

class MainServoController(object):
	def __init__(self, udpService = None):
		if udpService:
    			self.udpService = udpService
		else:	
			self.udpService = UDPService()
	
	def RunServoService(self, portNumber, host = None):
		try:
			print("Servo Controller running...")
			while 1:
			
		except (KeyboardInterrupt, SystemExit):
			raise
		except:
			traceback.print_exc()
		finally:  
			GPIO.cleanup() 

if __name__ == '__main__':
	port = int(sys.argv[1])
	mainServoController = MainServoController()
	mainServoController.RunServoService(port, sys.argv[2] if len(sys.argv) > 1 else None)