# project/middleware.py
from django.shortcuts import render, redirect
from django.conf import settings

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed_urls = [settings.LOGIN_URL, '/signup/']

        # 空パスならログインページにリダイレクト
        if request.path == '/accouts/':
            return redirect(settings.LOGIN_URL)

        # ログインしていない & 許可URL以外
        if not request.user.is_authenticated and request.path not in allowed_urls:
            return render(request, 'error.html', status=403)

        return self.get_response(request)
