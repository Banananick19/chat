from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class SingUpForm(forms.ModelForm):

    username = forms.CharField(max_length=100, required=True)
    email = forms.CharField(widget=forms.EmailInput, required=True)
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput, required=True)

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        return password1

    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError(
                'Введенные пароли не совпадают',
                code='password_mismatch')}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class SingInForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
