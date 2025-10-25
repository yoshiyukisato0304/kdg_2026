from django.urls import path
from .views import UserLoginView,LogoutcheckView ,UserLogoutView

app_name = 'accounts'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/check', LogoutcheckView.as_view(), name='logoutcheck'),
    path('logout/approval', UserLogoutView.as_view(), name='logout'),
]