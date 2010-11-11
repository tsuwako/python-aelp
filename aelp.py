#!/usr/bin/env python

import sys

def usage():
  print "Usage: %s app_name" % sys.argv[0]

def create_app(app):
  pass

def main():
  if len(sys.argv) < 2:
    usage()
    exit(0)
  create_app(sys.argv[1])

if __name__ == '__main__':
  main()
