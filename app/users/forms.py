from dataclasses import field
from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        # fields = ['phone','rfc','bithday','sexo']