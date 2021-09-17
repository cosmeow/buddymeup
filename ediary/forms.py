from django import forms

from .models import Users

class PostRegistrationForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = ('first_name', 'last_name','email','password',)