#!/usr/bin/env python
import optparse

def main():
    p = optparse.OptionParser()
    p.add_option('--sysadmin', '-s', default="BOFH")
    options, arguments = p.parse_args()
    print ('Hello, %s' % options.sysadmin)

if __name__ == '__main__':
    main()

#python3 hello_world_optparse.py
#python3 hello_world_optparse.py --sysadmin Noah
#python3 hello_world_optparse.py --s Jeremy