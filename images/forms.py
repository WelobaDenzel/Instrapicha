from django import forms
from .models import Image, Profile, Comments

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

class UploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = "__all__"

class AddComment(forms.ModelForm):
    class Meta:
        model= Comments
        fields = "__all__"
