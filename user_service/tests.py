from django.test import TestCase
from .models import User

class UserRegistrationTest(TestCase):
    def test_user_registration(self):
        user = User.objects.create_user(
            email='testuser@example.com',
            password='strongpassword123'
        )
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertTrue(user.check_password('strongpassword123'))
