class ExpectationError(AssertionError):
  pass


def _expectation(_expected_outcome, _action_class, *_args, **_kwargs):

  class Expectation(object):

    def __init__(self, action_class, *args, **kwargs):
      self.action = action_class(*args, **kwargs)

    def __enter__(self):
      return self.action.enter()

    def __exit__(self, type, value, traceback):
      if self.action.exit() != _expected_outcome:
        raise ExpectationError(self.action.message)
        return False
      return True

  return Expectation(_action_class, *_args, **_kwargs)


class Expect(object):

  @classmethod
  def to(cls, action_class, *args, **kwargs):
    return _expectation(True, action_class, *args, **kwargs)

  @classmethod
  def not_to(cls, action_class, *args, **kwargs):
    return _expectation(False, action_class, *args, **kwargs)
