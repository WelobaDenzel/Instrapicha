from django import forms
from .models import Image, Profile, Comment

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['name']

class UploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = "__all__"

class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields = "__all__"
