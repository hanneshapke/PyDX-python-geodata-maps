from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

from project.views import (CallLocationViewSet, CallSinglePageAppView,
                           RefreshTwitterStreamDataAjax)

admin.autodiscover()


router = routers.DefaultRouter()
router.register(r'calls', CallLocationViewSet, base_name="Calls")

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api/refresh/',
        RefreshTwitterStreamDataAjax.as_view(), name='refresh'),
    url(r'^$', CallSinglePageAppView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework'))
]
