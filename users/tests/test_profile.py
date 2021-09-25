"""User update profile tests."""

# Django
from django.test import TestCase
from django.urls import reverse_lazy

# Models
from django.contrib.auth.models import User
from users.models import Profile


class UserLoginTest(TestCase):

    def setUp(self):
        self.update_profile_url = reverse_lazy('users:update_profile')
        self.login_url = reverse_lazy('users:login')
        self.feed_url = reverse_lazy('notes:feed')
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