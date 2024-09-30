from django.urls import path
from .views import UserRegistrationView, UserProfileView, UserProfileUpdateView

urlpatterns = [
    path('auth/register/', UserRegistrationView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/update/', UserProfileUpdateView.as_view(), name='profile-update'),
]
