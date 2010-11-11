#!/usr/bin/env python

import sys
from os import mkdir, chdir
from os.path import exists, abspath

import apptemplate

def usage():
  print "Usage: %s app_name" % sys.argv[0]

def create_app(app):
  if exists("/".join([abspath('.'), app])):
    print "Already exists: %s" % app
    exit(0)

  mkdir(app)
  deploy_files(app)

def deploy_files(app):
  chdir(app)
  with open('app.yaml', 'w') as f:
    print >>f, apptemplate.AppYamlFormat % app

def main():
  if len(sys.argv) < 2:
    usage()
    exit(0)
  create_app(sys.argv[1])

if __name__ == '__main__':
  main()

