#!/usr/bin/env python

import sys

counter = 1
while True:
    line = sys.stdin.readline()
    if not line:
        break
    print ("%s: %s" % (counter, line))
    counter += 1

#枚举
# who | ./sys_stdin_readline.py\