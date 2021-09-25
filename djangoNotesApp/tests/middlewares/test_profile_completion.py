"""djangoNotesApp profile completion middleware tests."""

# Django
from django.test import TestCase
from django.urls import reverse_lazy

# Models
from django.contrib.auth.models import User
from users.models import Profile


class ProfileCompletionMiddlewareTest(TestCase):

    def setUp(self):
        self.feed_url = reverse_lazy('notes:feed')
        self.login_url = reverse_lazy('users:login')
        self.update_profile_url = reverse_lazy('users:update_profile')
        self.data = {
            'username': 'testusername', 
            'password': 'testpassword',
        }
        user = User.objects.create_user(
            **self.data,
        )
        user.profile = Profile.objects.create(user=user)
        user.save()

    def test_new_user_profile_redirect(self):
        """Test that new users logged or users without 
        the completed profile data are redirected to profile update page."""
        response = self.client.post(self.login_url, self.data, follow=True)
        self.assertRedirects(response, self.update_profile_url, 
            status_code=302, target_status_code=200, 
            fetch_redirect_response=True
        )
        response = self.client.get(self.feed_url, follow=True)
        self.assertRedirects(response, self.update_profile_url, 
            status_code=302, target_status_code=200, 
            fetch_redirect_response=True
        )