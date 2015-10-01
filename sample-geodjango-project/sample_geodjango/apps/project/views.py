from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy

from .models import CallLocation
from .forms import CallLocationForm


class CallLocationCreateView(CreateView):

    model = CallLocation
    form = CallLocationForm
    success_url = reverse_lazy('home')
    # template = 'project/calllocation_form.html'
    fields = ['address', 'call_type', 'comment']

    def get_context_data(self, **kwargs):
        context = super(
            CallLocationCreateView,
            self
        ).get_context_data(**kwargs)
        context['object_list'] = CallLocation.objects.all()
        return context
