from django.urls import path
from .views import UserLoginAPIView, UserRegistrationAPIView

app_name = 'apps.accounts'

urlpatterns = [
    path('users/sign-up/', UserRegistrationAPIView.as_view(), name="sign-up"),
    path('users/login/', UserLoginAPIView.as_view(), name="login"),
]
