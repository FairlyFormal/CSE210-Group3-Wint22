import time
import datetime

class Timer():

    def __init__(self):
        self._now = datetime.datetime.now()
        self._later = datetime.datetime.now()
        self._diff_delta = self._later - self._now
        self._seconds = 0

    def execute(self,cast,script):
        self._later = datetime.datetime.now()
        self._diff_delta = self._later - self._now
        if self._seconds != self._diff_delta.total_seconds():
            self._seconds = self._diff_delta.total_seconds()
            print("countdown:" + str(self._seconds))