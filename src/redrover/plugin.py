from nose.plugins.errorclass import ErrorClass, ErrorClassPlugin


class My(Exception):
  pass


class MyError(ErrorClassPlugin):
  me = ErrorClass(My, label='DUSTIN', isfailure=True)
