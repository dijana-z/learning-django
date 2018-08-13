from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        """
        information about your class
        """
        # what do you want to create?
        model = User
        fields = ['username', 'email', 'password']