from django.contrib.auth.views import LoginView, LogoutView

class UserLoginView(LoginView):
    template_name = 'account/login.html'

class UserLogoutView(LogoutView):
    pass