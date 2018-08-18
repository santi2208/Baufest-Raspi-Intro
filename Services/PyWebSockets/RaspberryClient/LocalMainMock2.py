import time
from HttpProxy import HttpProxy

class AchievementsWatcher(object):
    def __init__(self, httpProxy = None):
        self.httpProxy = httpProxy if httpProxy else HttpProxy()

    def Main(self):
        lastValues = None
        while  1:
            gpiosRes = [[1,20,0], [1,21,1], [2,17,1]]
            # if(lastValues != gpiosRes):
            print (gpiosRes)
            self.httpProxy.InformGpioStatus(gpiosRes)
            lastValues = gpiosRes
            time.sleep(5)          

if __name__ == '__main__':
    ach = AchievementsWatcher()
    ach.Main()