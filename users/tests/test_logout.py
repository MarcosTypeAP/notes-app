"""User logout tests."""

# Django
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse_lazy

# Models
from django.contrib.auth.models import User
from users.models import Profile


class UserLoginTest(TestCase):

    def setUp(self):
        self.login_url = reverse_lazy('users:login')
        self.feed_url = reverse_lazy('notes:feed')
        self.logout_url = reverse_lazy('users:logout')
        self.data = {
            'username': 'testusername', 
            'password': 'testpassword',
        }
        user = User.objects.create_user(
            **self.data,
            first_name='testfirstname',
            last_name='testlastname',
        )
        user.profile = Profile.objects.create(user=user)
        user.save()

    def test_user_logout(self):
        """Test that the logout url works correctly."""
        c = Client()
        response = c.post(self.login_url, self.data)
        self.assertRedirects(response, self.feed_url, 
            status_code=302, target_status_code=200, 
            fetch_redirect_response=True
        )
        response = c.get(self.feed_url)
        self.assertEqual(response.status_code, 200)
        response = c.get(self.logout_url)
        self.assertRedirects(response, self.login_url, 
            status_code=302, target_status_code=200, 
            fetch_redirect_response=True
        )
        response = c.get(self.feed_url)
        self.assertRedirects(response, self.login_url + '?next=/', 
            status_code=302, target_status_code=200, 
            fetch_redirect_response=True
        )