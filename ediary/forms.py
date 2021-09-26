from django import forms

from .models import Users
from .models import ExerciseLocation, Exercise, Activities

class PostRegistrationForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = ('first_name', 'last_name','email','password',)

class PostActivityForm(forms.ModelForm):

    class Meta:
        model = Activities
        fields = ('user','date','location','exercise','duration_min', 'distance_km')
