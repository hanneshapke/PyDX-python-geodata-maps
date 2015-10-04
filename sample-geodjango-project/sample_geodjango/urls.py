from django.conf.urls import patterns, include, url
from django.contrib import admin

from project.views import CallLocationCreateView

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^(?P<pk>[0-9]+)/$',
        CallLocationCreateView.as_view(), name='neighborhood'),
    url(r'^$', CallLocationCreateView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
