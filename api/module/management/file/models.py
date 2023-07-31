from django import forms
from service.framework.model.timestamped_model import TimeStampedModel


class File(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()