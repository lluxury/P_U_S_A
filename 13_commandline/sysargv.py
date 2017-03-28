#!/usr/bin/env python
import sys

#Python indexes start at Zero, so let's not count the command itself which is
#sys.argv[0]
num_arguments = len(sys.argv) - 1
print (sys.argv, "You typed in ", num_arguments, "arguments")