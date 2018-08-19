import sys
import time
from HttpProxy import HttpProxy
from Achievement import Achievement 
from GpioReader import GpioReader

class GPIOSsWatcher(object):
    def __init__(self, teamNumber, httpProxy = None):
        self.httpProxy = httpProxy if httpProxy else HttpProxy('http://192.168.0.14:8888/achievements')
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
    watcher = GPIOSsWatcher(int(sys.argv[1]))
    watcher.Main()