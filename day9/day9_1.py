import os
from time import localtime, time, sleep
class Clock(object):
    def __init__(self,hour,minute,second):
        self._hour = hour
        self._minute = minute
        self._second = second
    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)


    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def display(self):
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)

def main():
    clock = Clock.now()
    while True:
        print(clock.display())
        sleep(1)
        os.system('clear')
        clock.run()


if __name__ == '__main__':
    main()








ctime = localtime(time())
print(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)
