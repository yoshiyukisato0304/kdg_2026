from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import View

class UserLoginView(LoginView):
    template_name = 'account/login.html'

class LogoutcheckView(View):
    template_name = 'account/logout.html'

class UserLogoutView(LogoutView):
    pass