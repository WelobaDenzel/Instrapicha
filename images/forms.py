from django import forms
from .models import *

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

class UploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = "__all__"

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
