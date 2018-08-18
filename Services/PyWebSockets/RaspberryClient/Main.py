import time
from HttpProxy import HttpProxy
from Achievement import Achievement 
from GpioReader import GpioReader

class AchievementsWatcher(object):
    def __init__(self, httpProxy = None):
        self.httpProxy = httpProxy if httpProxy else HttpProxy('http://192.168.0.15:8888/achievements')
        self.gpioReader = GpioReader(1)

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
    ach = AchievementsWatcher()
    ach.Main()