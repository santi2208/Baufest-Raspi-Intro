from UDPService import * 
import socket, sys

def TestR(port, ip):
    udpService = UDPService()
    while True:
        print(udpService.ListenToPortOnce(port, ip))

port = int(sys.argv[1])
ip = sys.argv[2]
print(port)
TestR(port, ip)