from django import forms
from .models import Member

class UserForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'email', 'password']