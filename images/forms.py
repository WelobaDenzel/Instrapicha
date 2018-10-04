from django import forms
from .models import Image, Profile

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

class UploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = "__all__"
