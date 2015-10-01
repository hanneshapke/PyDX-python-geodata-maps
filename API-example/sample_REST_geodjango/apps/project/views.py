from rest_framework import viewsets
from .models import CallLocation
from .serializers import CallSerializer
from .utils import set_call_locations


class CallLocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = CallSerializer

    def get_queryset(self):
        # This call should be async and part of a celery task
        set_call_locations()
        # return all emergency calls
        return CallLocation.objects.all().order_by('-timestamp')
