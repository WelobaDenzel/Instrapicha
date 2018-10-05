from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.
class Profile(models.Model):
    profile_photo= models.ImageField(upload_to='picha/')
    bio= models.CharField(max_length=240)
    username = models.ForeignKey(User,on_delete=models.CASCADE)

    def save_profile(self):
        self.save()

    @classmethod
    def my_profile(cls,id):
        profile= cls.objects.get(id=id)
        return profile

    class Meta:
        ordering = ['username']

class Comment(models.Model):
    comment = models.CharField(max_length=70, blank=True)
    username = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.comment


class Image(models.Model):
    insta_image = models.ImageField(upload_to='picha/')
    caption = models.CharField(max_length=70)
    like=models.IntegerField(default=0)
    profile= models.ForeignKey(Profile)
    comments = models.ForeignKey(Comment,on_delete=models.CASCADE, null=True, blank=True)

    @classmethod
    def all_images(self):

        return Image.objects.all()

class Likes(models.Model):
    likes= models.IntegerField (default=0)
    image_id = models.ForeignKey(Image)
