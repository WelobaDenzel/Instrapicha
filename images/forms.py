from django import forms
from .models import Image, Profile

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['name']

class UploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = "__all__"
