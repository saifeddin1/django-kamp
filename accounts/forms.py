from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=False, help_text='optional')
    last_name = forms.CharField(
        max_length=30, required=False, help_text='optional')
    email = forms.CharField(
        max_length=30, help_text='Required')
    address = forms.CharField(
        max_length=100, required=False, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',
                  'first_name', 'last_name', 'email', 'address',)
