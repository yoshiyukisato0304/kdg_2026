from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.shortcuts import redirect,render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

class IndexView(TemplateView):
    template_name = 'index.html'


def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'ユーザー名またはパスワードが正しくありません。')
            return redirect('login')
    return render(request, 'login.html')

def logoutcheck(request):
    logout(request)
    return redirect('login')


