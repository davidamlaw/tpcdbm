from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class LoginPage(TemplateView):
    template_name = 'login.html'

class HomePage(LoginRequiredMixin, TemplateView):
    login_url = '/'
    redirect_field_name = '/'
    template_name = 'home.html'
