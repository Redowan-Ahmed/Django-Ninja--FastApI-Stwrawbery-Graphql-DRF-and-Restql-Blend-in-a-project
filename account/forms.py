from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm, PasswordChangeForm
from django.forms import PasswordInput, CharField
from django.views.generic.edit import FormMixin
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email',
                  'phone_number', 'password1', 'password2']


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = '__all__'

class CustomUserPasswordChangeForm(FormMixin, PasswordChangeForm):
    old_password = CharField(widget = PasswordInput(attrs={
                'class': "form-control",
                'placeholder': 'Current password'
                }))
    new_password1 = CharField(widget = PasswordInput(attrs={
                'class': "form-control pe-50",
                'placeholder': 'New password'
                }))
    new_password2 = CharField(widget = PasswordInput(attrs={
                'class': "form-control pe-50",
                'placeholder': 'Re-type new password'
                }))

    class Meta:
        model = CustomUser
        fields = ['old_password', 'new_password1', 'new_password2']
