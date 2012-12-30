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
    except ValidationError:
      self.passes = False

  @property
  def message(self):
    if self.passes:
      msg = '{subject} is valid'
    else:
      msg = '{subject} is not valid'

    return msg.format(subject=repr(self.subject))
