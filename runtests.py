#!/usr/bin/env python
import os
import sys


def runtests(args=None):
  import pytest
  
  if 'NOSE_REDNOSE' not in os.environ:
    os.environ['NOSE_REDNOSE'] = '1'
  
  if not args:
    args = []
    
  if not any(a for a in args[1:] if not a.starswith('-')):
    args.append('tests')
  
  sys.exit(pytest.main(args))
  
  
if __name__ == '__main__':
  runtests(sys.argv)