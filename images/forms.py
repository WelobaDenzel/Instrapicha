from django import forms
from .models import *

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class UploadForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude =['user','thoughts','like','profile']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude =['user','imagecomment']
