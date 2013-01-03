from django.core.exceptions import ValidationError
from django.db import models

from base import BaseAssertion


class BeValidAssertion(BaseAssertion):
  """Determine if a Django Model is valid."""

  def __init__(self, subject):
    if not isinstance(subject, models.Model):
      raise ValueError('`be_valid` must be called on a Django Model instance.')

    self.subject = subject
    self.passes = True
    try:
      subject.full_clean()
    except ValidationError, e:
      self.passes = False
      self.error_messages = e.message_dict

  @property
  def message(self):
    if self.passes:
      msg = '{subject} is valid'
      return msg.format(subject=repr(self.subject))
    else:
      msg = '{subject} is not valid.  {message}'
      errors = []
      for i in self.error_messages:
        errors += [(i, ' '.join(self.error_messages[i]))]
      return msg.format(
        subject=repr(self.subject),
        message="\033[0m" + ''.join(["%s: %s" % i for i in errors]))
