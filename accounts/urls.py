from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import (login, register, logout, dashboard, password_reset_request,
                    ProfileUpdateView, AddressView)

urlpatterns = [
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('logout', logout, name='logout'),
    path('dashboard', dashboard, name='dashboard'),
    path('profile/<int:pk>', login_required(
         ProfileUpdateView.as_view()), name='profile'),
    path('profile/address', login_required(  # TODO move to coreapp?
         AddressView.as_view()), name='user-address'),
    path("password-reset", password_reset_request, name="password-reset")
]
