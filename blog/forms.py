# blog/forms.py

from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        raw_password = self.cleaned_data.get('password')
        user.set_password(raw_password)
        if commit:
            user.save()
        return user