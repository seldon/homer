from django.conf.urls import patterns, url
from news.models import News

urlpatterns = patterns('news.views',
    url(r'^$', 'list'),
    url(r'^(?P<slug>[\w-]+)/$', 'detail'),
)