from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, UpdateView
from django.urls import reverse_lazy

from users.forms import SignupForm, ProfileForm

from users.models import Profile

import cloudinary_storage


class ProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'logged/users/profile.html'
    model = Profile
    form_class = ProfileForm
    success_url = reverse_lazy('users:update_profile')

    def get_object(self):
        self.old_picture = self.request.user.profile.picture
        return self.request.user.profile

    def form_valid(self, form):
        user = self.request.user
        data = form.cleaned_data
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.save()
        self.object = form.save()
        return super(ProfileView, self).form_valid(form)


class SignupView(FormView):
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'users/logout.html'


class LoginView(LoginView):
    template_name = 'users/login.html'