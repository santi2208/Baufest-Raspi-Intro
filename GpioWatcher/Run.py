import sys
import time
import argparse
from HttpProxy import HttpProxy
from Achievement import Achievement 
from GpioReader import GpioReader

class GPIOSsWatcher(object):
    def __init__(self, teamNumber, sIp, invertirSwitch):
        self.httpProxy = HttpProxy("http://{}:8888/achievements".format(sIp))
        self.gpioReader = GpioReader(teamNumber)
        self.invertirSwitch = False if (invertirSwitch is None or invertirSwitch == "0") else True
        print(self.invertirSwitch)
        
    def Main(self):
        lastValues = None
        while  1:
            gpiosRes = self.gpioReader.ReadAllOnce(self.invertirSwitch) #[[2,10,1],[2,11,1]]
            if(lastValues != gpiosRes):
                print (gpiosRes)
                self.httpProxy.InformGpioStatus(gpiosRes)
                lastValues = gpiosRes
            time.sleep(0.5)          

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--team', help='Numero identificatorio de Equipo')
    parser.add_argument('--sIp', help='Ip del servidor.')
    parser.add_argument('--inv', help='Invertir Estado del Relay - 0: NO | 1: Si. Default: NO')
    args = parser.parse_args()    

    watcher = GPIOSsWatcher(int(args.team), args.sIp, args.inv)
    watcher.Main()