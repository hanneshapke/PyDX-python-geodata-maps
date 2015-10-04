from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView

from .models import CallLocation, Neighborhood
from .forms import CallLocationForm


class CallLocationCreateView(CreateView):

    model = CallLocation
    form = CallLocationForm
    success_url = reverse_lazy('home')
    fields = ['address', 'call_type', 'comment']

    def get_context_data(self, *args, **kwargs):
        context = super(
            CallLocationCreateView, self
        ).get_context_data(**kwargs)

        context['neighborhoods'] = Neighborhood.objects.all()
        context['pk'] = int(self.kwargs.get('pk', -1))
        if context['pk'] > 0:
            neighborhood = get_object_or_404(Neighborhood, pk=context['pk'])
            context['object_list'] = CallLocation.objects.filter(
                location__within=neighborhood.poly)
        else:
            context['object_list'] = CallLocation.objects.all()
        return context
