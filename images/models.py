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

    @classmethod
    def get_profile(cls):
        profile = Profile.objects.all()
        return profile

    @classmethod
    def find_profile(cls,search_term):
        profile = Profile.objects.filter(user__username__icontains=search_term)
        return profile

class Image(models.Model):
    posted_by = models.ForeignKey(User, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)
    insta_image = models.ImageField(upload_to='picha/',null=True)
    caption = models.TextField(null=True)

    @classmethod
    def get_user_images(cls, profile_id):
        images=Image.objects.filter(profile_id=user.id)

    @classmethod
    def get_images(cls):
        image = Image.objects.all()
        return image

    def __str__(self):
       return str(self.caption)

class Comment(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments',null=True)
    comment = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.comment

    def save_comment(self):
        self.save()

    @classmethod
    def get_comment(cls):
        comment = Comment.objects.all()
        return comment

class Likes(models.Model):
    image = models.ForeignKey(Image, related_name='likes',null=True)
    liked_by = models.ForeignKey(User, related_name='liked_images',null=True)
