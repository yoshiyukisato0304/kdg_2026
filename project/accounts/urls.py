from django.urls import path
from .views import loginview, logoutcheck

urlpatterns = [
    path('', loginview, name='login'),
    path('logout/', logoutcheck, name='logout'),
]
