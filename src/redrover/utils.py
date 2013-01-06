from django.core.urlresolvers import NoReverseMatch, reverse
from django.db.models import Model as DjangoModel


def get_url(obj, *args, **kwargs):
  """Try to infer a URL from an ambiguous object."""
  if isinstance(obj, DjangoModel):
    return obj.get_absolute_url()
  try:
    return reverse(obj, *args, **kwargs)
  except NoReverseMatch:
    return str(obj)
  except:
    raise RuntimeError("Could not infer a url from object %s." % repr(obj))
