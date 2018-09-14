import sys
import time
import argparse
from HttpProxy import HttpProxy
from Achievement import Achievement 
from GpioReader import GpioReader

class GPIOSsWatcher(object):
    def __init__(self, teamNumber, url):
        self.httpProxy = HttpProxy(url) #'http://192.168.0.14:8888/achievements'
        self.gpioReader = GpioReader(teamNumber)

    def Main(self):
        lastValues = None
        while  1:
            gpiosRes = self.gpioReader.ReadAllOnce() #[[2,10,1],[2,11,1]]
            if(lastValues != gpiosRes):
                print (gpiosRes)
                self.httpProxy.InformGpioStatus(gpiosRes)
                lastValues = gpiosRes
            time.sleep(0.5)          

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--team', help='Numero identificatorio de Equipo')
    parser.add_argument('--url', help='Url a la que se reporta el estado de los componentes')
    args = parser.parse_args()    

    watcher = GPIOSsWatcher(int(args.team), args.url)
    watcher.Main()