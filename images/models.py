from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.
class Profile(models.Model):
    profile_photo= models.ImageField(upload_to='picha/')
    bio= HTMLField()
    name = models.ForeignKey(User, on_delete=models.CASCADE)

    def all_profiles(self):
        return Profile.objects.all()

class Image(models.Model):
    insta_image = models.ImageField(upload_to='picha/')
    caption = models.CharField(max_length=70)
    profile= models.ForeignKey(Profile)
    likes= models.IntegerField(default=0)
    comments= HTMLField()

    @classmethod
    def all_images(self):

        return Image.objects.all()
