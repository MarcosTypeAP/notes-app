from django.contrib.auth.models import User
from users.models import Profile

from django import forms


class ProfileForm(forms.ModelForm):

    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'picture']


class SignupForm(forms.Form):

    username = forms.CharField(min_length=4, max_length=16)
    email = forms.CharField(min_length=6, max_length=320, widget=forms.EmailInput())

    password = forms.CharField(min_length=8, max_length=100, widget=forms.PasswordInput())
    password_confirmation = forms.CharField(min_length=8, max_length=100, widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data['username']
        username_exists = User.objects.filter(username=username)
        if username_exists:
            raise forms.ValidationError('Username is already in use')
        return username

    def clean(self):
        data = super().clean()
        if 'password' in data and 'password_confirmation' in data:
            password = data['password']
            password_confirmation = data['password_confirmation']
        else:
            raise forms.ValidationError('Password must be 8 to 100 characters')

        if password != password_confirmation:
            raise forms.ValidationError({'password_confirmation': 'Passwords do not match'})

        return data

    def save(self):
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()