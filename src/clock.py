import time

class Clock():
    def __init__(self, rate):
        self.rate = rate
        self.spf = 1 / rate
        self.start = None
        self.end = None
        self.exe = None

    def startTicker(self):
        self.start = time.time()

    def endTicker(self):
        self.end = time.time()
        self.exe = self.end - self.start

        if self.exe <= self.spf:
            time.sleep(self.spf - self.exe)
