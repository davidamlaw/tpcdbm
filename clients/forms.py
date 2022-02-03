from django.forms import ModelForm
from . import models

class ClientAddForm(ModelForm):

    class Meta:
        model = models.ClientEfs
        fields = '__all__'

class ClientUpdateForm(ModelForm):

    class Meta:
        model = models.ClientEfs
        fields = '__all__'
