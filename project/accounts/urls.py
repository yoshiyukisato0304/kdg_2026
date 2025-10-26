from django.urls import path
from .views import logoutcheck  # 関数を直接インポート
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),  # ダミーのインデックスページ
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', logoutcheck, name='logout'),
]