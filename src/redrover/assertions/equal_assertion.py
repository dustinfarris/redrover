from base import BaseAssertion


class EqualAssertion(BaseAssertion):
  """Compare the equivalence of two objects."""

  def __init__(self, subject, other):
    self.subject = subject
    self.other = other
    self.passes = subject == other

  @property
  def message(self):
    if self.passes:
      msg = '{subject} equals {other}'
    else:
      msg = '{subject} does not equal {other}'

    return msg.format(
      subject=repr(self.subject),
      other=repr(self.other))
