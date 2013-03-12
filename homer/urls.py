from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^belenchia/', include('belenchia.foo.urls')),

    url(r'^$', 'homer.views.home', name='home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('estates.views',
    url(r'^estates/$', 'home_estates', name='home_estates'), 
    url(r'^ajax/$', 'ajax_magic', name='ajax_magic'),
    url(r'^estates/search-result/$', 'search_estates', name='search_estates'),
    url(r'^estates/detail/(?P<pk>\d+)/$', 'detail_single_estate', name='detail_single_estate'),
)

urlpatterns += patterns('news.views',
    url(r'^administrator/', include('news.urls')),
)


#For media files
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
