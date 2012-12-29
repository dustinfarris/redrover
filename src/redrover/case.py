class BaseAssertion(object):
  passes = None

  @property
  def message(self):
    """Should be implemented by child classes."""
    raise NotImplementedError


class EqualAssertion(BaseAssertion):
  """Compare the equivalence of two objects."""

  def __init__(self, subject, other):
    self.subject = subject
    self.other = other
    self.passes = subject == other

  @property
  def message(self):
    if self.passes:
      msg = '{subject_type} {subject_value} equals {other}'
    else:
      msg = '{subject_type} {subject_value} does not equal {other}'
    return msg.format(
      subject_type=type(self.subject).__name__.capitalize(),
      subject_value=str(self.subject),
      other=str(self.other))


class BeAssertion(BaseAssertion):
  """Determine if two objects are identical."""

  def __init__(self, subject, other):
    self.subject = subject
    self.other = other
    self.passes = subject is other

  @property
  def message(self):
    if self.passes:
      msg = '{subject_type} {subject_value} is {other}'
    else:
      msg = '{subject_type} {subject_value} is not {other}'
    return msg.format(
      subject_type=type(self.subject).__name__.capitalize(),
      subject_value=str(self.subject),
      other=str(self.other))
