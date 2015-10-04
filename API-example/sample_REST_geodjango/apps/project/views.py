# Django Packages
from django.http import JsonResponse
from django.views.generic.base import TemplateView
# 3rd party
from rest_framework import viewsets
from rest_framework_gis.filters import InBBOXFilter
# project packages
from .models import CallLocation
from .serializers import CallSerializer
from .utils import set_call_locations


class CallLocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = CallSerializer
    # bbox defines which column is used to select the objects returned
    # to the frontend
    bbox_filter_field = 'location'
    # filter settings
    filter_backends = (InBBOXFilter, )
    # the overlapping allows polygons to be partially be part of the bbox
    bbox_filter_include_overlapping = True  # not needed for PointFields

    def get_queryset(self):
        # This call should be async and part of a celery task
        set_call_locations(username='pdxpolicelog')
        # return all emergency calls
        return CallLocation.objects.all().order_by('-timestamp')


class RefreshTwitterStreamDataAjax(TemplateView):
    """
    This Ajax view triggers an update of the twitter stream data
    """

    def get(self, request, *args, **kwargs):
        # This call should be async and part of a celery task
        message, status = set_call_locations(username='pdxpolicelog')
        # return message (e.g. errors)
        return JsonResponse(
            dict(message=message, status=status),
            status=status)


class CallSinglePageAppView(TemplateView):
    """ This templateview servers the Angular page with the js client """
    template_name = "project/angular_api_client.html"
