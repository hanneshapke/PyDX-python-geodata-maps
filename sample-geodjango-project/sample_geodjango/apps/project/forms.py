from django import forms

from .models import CallLocation


class CallLocationForm(forms.ModelForm):

    class Meta:
        model = CallLocation
        fields = (
            'address',
            'call_type',
            'comment'
        )
