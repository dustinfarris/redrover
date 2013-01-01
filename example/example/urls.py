from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('',
  url(r'^$', direct_to_template, {'template': 'home.html'}, name='home'),
  url(r'^people/', include('people.urls', namespace='people')),
)
