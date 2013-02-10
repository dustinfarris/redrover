from django.core.urlresolvers import NoReverseMatch, reverse
from django.db.models import Model as DjangoModel
from django.utils.encoding import iri_to_uri


def get_url(obj, *args, **kwargs):
    """Try to infer a URL from an ambiguous object."""
    if isinstance(obj, DjangoModel):
        return obj.get_absolute_url()
    obj = iri_to_uri(obj)
    if obj.startswith('http'):
        return obj
    try:
        return reverse(obj, *args, **kwargs)
    except NoReverseMatch:
        return obj
    except Exception, msg:
        raise RuntimeError(msg)
