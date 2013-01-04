from django.conf.urls import patterns, url
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from models import Person


urlpatterns = patterns('',
  url('^$', ListView.as_view(model=Person), name='index'),
  url('^(?P<pk>\d+)/$', DetailView.as_view(model=Person), name='detail'),
)
