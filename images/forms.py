from django import forms
from .models import Image, Profile

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__" 
