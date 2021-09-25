"""User sign up tests."""

# Django
from django.test import TestCase
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

# Models
from django.contrib.auth.models import User


class UserSignupTest(TestCase):

    signup_url = reverse_lazy('users:signup')

    def test_create_user(self):
        """Test that signup page creates a user successfully."""
        data = {
            'username': 'testusername',
            'email': 'testemail@testcase.com',
            'password': 'testpassword',
            'password_confirmation': 'testpassword',
        }
        response = self.client.post(self.signup_url, data, follow=True)
        self.assertEqual(response.status_code, 200)
        user = get_object_or_404(User, username='testusername')
        self.assertEqual(user.username, 'testusername')
