import socket, traceback
from sys import stdin

class UDPService(object):
	def ListenToPortOnce(self, portNumber, host = None):
		if host is None:
    			host = socket.gethostbyname(socket.gethostname())
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
		s.bind((host, portNumber))

		try:
			message, address = s.recvfrom(portNumber)
			return (message)
		except (KeyboardInterrupt, SystemExit):
			raise
		except:
			traceback.print_exc()
	
	def SendMessage(self, message, portNumber, host):
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
		try:
			s.sendto(message, (host, portNumber))
		except:
			s.sendto(bytes(message, "utf-8"), (host, portNumber))
			