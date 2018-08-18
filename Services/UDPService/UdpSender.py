from UDPService import * 
import socket, sys

def Test(port, ip):
    udpService = UDPService()
    while True:
        try:
            msg = raw_input("")
            udpService.SendMessage(msg, port, ip)
        except Exception as e:
            print('>>>>ERROR Message>>>>> {}'.format(e))

port = int(sys.argv[1])
ip = sys.argv[2]
Test(port, ip)