from django.db import models
from django.contrib.auth.models import User
# from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    profile_photo= models.ImageField(upload_to='profiles/',null=True)
    bio= models.CharField(max_length=240, null=True)


    def save_profile(self):
        self.save()

    @classmethod
    def my_profile(cls,id):
        profile= cls.objects.get(id=id)
        return profile

    def __str__(self):
        return self.user


class Image(models.Model):
    posted_by = models.ForeignKey(User, null=True)
    insta_image = models.ImageField(upload_to='picha/',null=True)
    caption = models.TextField(null=True)



    @classmethod
    def all_images(self):
        all_images = cls.objects.all()
        return Image.objects.all()

    @classmethod
    def get_user_images(cls, profile_id):
        images=Image.objects.filter(profile_id=user.id)

class Comment(models.Model):
    poster = models.ForeignKey(User, related_name='comments',null=True)
    image = models.ForeignKey(Image, related_name='comments',null=True)
    comment = models.TextField(null=True)


    def save_comment(self):
        self.save()

    def __str__(self):
        return self.comment

class Likes(models.Model):
    image = models.ForeignKey(Image, related_name='likes',null=True)
    liked_by = models.ForeignKey(User, related_name='liked_images',null=True)
