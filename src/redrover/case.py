class Equal(object):

  def __init__(self, subject, other):
    self.subject = subject
    self.other = other

  def process(self):
    return self.subject == self.other

  def __unicode__(self):
    if self.process():
      message = '{subject_type} {subject_value} equals {other}'
    else:
      message = '{subject_type} {subject_value} does not equal {other}'
    return message.format(
      subject_type=type(self.subject).__name__,
      subject_value=str(self.subject),
      other=str(self.other))
