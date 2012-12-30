class BaseAssertion(object):
  passes = None

  @property
  def message(self):
    """Should be implemented by child classes."""
    raise NotImplementedError
