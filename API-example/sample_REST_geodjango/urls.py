from django.conf.urls import include, url
# from django.contrib import admin
from rest_framework import routers

from project.views import CallLocationViewSet

# admin.autodiscover()

# urlpatterns = patterns(
#     '',
#     url(r'^$', CallLocationCreateView.as_view(), name='home'),
#     url(r'^admin/', include(admin.site.urls)),
# )

router = routers.DefaultRouter()
router.register(r'calls', CallLocationViewSet, base_name="Calls")
# router.register(r'types', CallTypeViewSet, base_name="Types")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework'))
]
