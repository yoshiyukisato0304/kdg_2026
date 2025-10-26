from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import View
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib.auth import logout

class IndexView(TemplateView):
    template_name = 'index.html'

class UserLoginView(LoginView):
    template_name = 'login.html'


def logoutcheck(request):
    logout(request)
    return redirect('login')

class UserLogoutView(LogoutView):
    pass

