from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.shortcuts import get_object_or_404
from django.shortcuts import HttpResponseRedirect #, HttpResponse
from . import forms
from . import models

class ClientAddView(CreateView):
    form_class = forms.ClientAddForm
    model = models.ClientEfs
    success_url = '/clients/'
    template_name = 'clients/client_add.html'

class ClientUpdateView(UpdateView):
    form_class = forms.ClientUpdateForm
    model = models.ClientEfs
    success_url = '/clients/'
    template_name = 'clients/client_update.html'

class ClientDetailView(DetailView):
    model = models.ClientEfs
    template_name = 'clients/client_detail.html'

class ClientListView(ListView):
    model = models.ClientEfs
    template_name = 'clients/client_list.html'
