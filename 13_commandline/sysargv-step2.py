#!/usr/bin/env python
import sys
num_arguments = len(sys.argv) - 1
#If there are no arguments to the command, send a message to standard error.
if num_arguments == 0:
sys.stderr.write('Hey, type in an option silly\n')
else:
print (sys.argv, "You typed in ", num_arguments, "arguments")


#IndentationError: expected an indented block