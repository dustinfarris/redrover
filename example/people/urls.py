from django.conf.urls import patterns, url
from django.views.generic.list import ListView

from models import Person


urlpatterns = patterns('',
  url('^$', ListView.as_view(model=Person), name='index'),
)