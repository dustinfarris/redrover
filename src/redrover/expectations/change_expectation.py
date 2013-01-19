from base import BaseExpectation


class ChangeExpectation(BaseExpectation):
  """Determine if the result of a callable changes."""

  def __init__(self, subject, by=None):
    if callable(subject):
      self.subject = subject
    else:
      raise RuntimeError(
        "The subject of a change expectation must be a callable.")
    self.delta = by

  def enter(self):
    self.original_value = self.subject()
    return self.original_value

  def exit(self):
    self.new_value = self.subject()
    if self.delta:
      self.passes = abs(self.original_value - self.new_value) == self.delta
    else:
      self.passes = self.original_value != self.new_value
    return self.passes

  @property
  def message(self):
    if self.passes:
      if self.delta:
        msg = '{subject} changed by {delta}'
      else:
        msg = '{subject} changed'
    else:
      if self.delta:
        msg = '{subject} did not change by {delta} (it changed by {actual})'
      else:
        msg = '{subject} did not change'

    return msg.format(
      subject=repr(self.subject),
      delta=repr(self.delta),
      actual=abs(self.original_value - self.new_value))
