"""User login tests."""

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
            username='testusername',
            first_name='testfirstname',
            last_name='testlastname',
        )
        user.set_password('testpassword')
        user.profile = Profile.objects.create(user=user)
        user.save()
        import pdb; pdb.set_trace()

    def test_user_login(self):
        """Test that the user can login."""
        logged_in = self.client.login(**self.data)
        self.assertTrue(logged_in)

    def test_login_redirect(self):
        """Test that the login page redirect to the feed page
        if the login was successful and the user completed the profile."""
        response = self.client.post(self.login_url, self.data, follow=True)
        self.assertRedirects(response, self.feed_url, 
            status_code=302, target_status_code=200, 
            fetch_redirect_response=True
        )
