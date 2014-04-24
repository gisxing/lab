""" a simple Distributing lock. with no expired function"""
from contextlib import contextmanager
import threading
import time
import random
import sys

class Thread(threading.Thread):
        def __init__(self, name):
            threading.Thread.__init__(self)
            self.name = name

        def run(self):
            with simple_lock('my_lock', 1, self.name) as locked:
                if locked:
                    time.sleep(random.randint(0,1) * 1.5)
                    for i in xrange(10):
                        print self.name

_myLock = {}
SLEEP_SECONDS = .1

@contextmanager
def simple_lock(key, timeout,pid):
    """simple lock."""
    try:
        locked = False
        for _ in xrange(int(timeout/SLEEP_SECONDS)):
            if _myLock.get(key, None):
                # already lock , retry
                print "wait the lock", pid
            else:
                _myLock[key] = True
                locked = True
                print "get the lock", pid
                break
            time.sleep(SLEEP_SECONDS)
        if not locked:
            print "get lock timeout!", pid 
        yield locked
 
    finally:
        # release the lock
        _myLock[key] = None
        print "in finally", pid
 
def main(argv):
    for x in xrange(2):
        thread_sample = Thread(x)
        thread_sample.start()

if __name__ =="__main__":
    main(sys.argv)
