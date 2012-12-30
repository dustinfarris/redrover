from django.db import models

from base import BaseAssertion


class RespondToAssertion(BaseAssertion):
  """Determine if a Django Model has a particular attribute or method."""

  def __init__(self, subject, attr):
    if not isinstance(subject, models.Model):
      raise ValueError(
        '`respond_to` must be called on a Django Model instance.')

    self.subject = subject
    self.attribute = attr
    fields = [f.__dict__['name'] for f in subject._meta.fields]
    attributes = dir(subject)
    self.passes = attr in fields + attributes

  @property
  def message(self):
    if self.passes:
      msg = '{subject} responds to {attribute}'
    else:
      msg = '{subject} does not respond to {attribute}'

    return msg.format(
      subject=repr(self.subject),
      attribute=repr(self.attribute))
