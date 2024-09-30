from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse

class CustomAccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        # После логина пользователь перенаправляется на дашборд
        return reverse('user_dashboard')
