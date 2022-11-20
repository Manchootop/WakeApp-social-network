from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

UserModel = get_user_model()


class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = UserModel
        fields = ['email', 'password1', 'password2']
