from base import BaseAssertion


class BeExactlyAssertion(BaseAssertion):
  """Determine if two objects are identical."""

  def __init__(self, subject, other):
    self.subject = subject
    self.other = other
    self.passes = subject is other

  @property
  def message(self):
    if self.passes:
      msg = '{subject} is {other}'
    else:
      msg = '{subject} is not {other}'
    return msg.format(
      subject=repr(self.subject),
      other=repr(self.other))
