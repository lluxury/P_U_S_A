from subprocess import Popen, PIPE
import sys

class Cmd(object):
    def __init__(self, *args):
        self.cmd = args
        self.prev = None
        self.p = None

    def __or__(self, next):
        next.prev = self
        return next
    
    def __iter__(self):
        self.start()
        return iter(self.p.stdout)
    
    def start(self):
        if self.prev:
            self.prev.start()
            input = self.prev.p.stdout
        else:
            input = sys.stdin
        self.p = Popen(self.cmd,
                stdin=input,
                stdout=PIPE)


#运行
from subtube import Runner
r = Runner("df -h", "du -h /tmp")
r.run()

#ImportError: No module named 'subtube'
r = Runner("df -h", "du -h /tmp", verbose=True)
r.run()



