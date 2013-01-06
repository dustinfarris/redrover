from base import BaseAssertion


class ContainAssertion(BaseAssertion):
  """Determine if one object exists within another."""

  def __init__(self, subject, other):
    self.subject = subject
    self.other = other
    self.passes = other in subject

  @property
  def message(self):
    if self.passes:
      msg = '{other} is in {subject}'
    else:
      msg = '{other} is not in {subject}'

    return msg.format(
      subject=repr(self.subject),
      other=repr(self.other))
