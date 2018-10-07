from django.test import TestCase
from .models import *
# Create your tests here.
class ImageTest(TestCase):

    # def class instance setup for the project
    def setUp(self):
        self.profile= Profile.object.create(user="zyzu", profile_photo="image.jpg", bio="twins")
        self.comment = Comment.objects.create(comment='one',poster="zyzu")

        self.snap = Image.objects.create(
            posted_by='zyzu', profile="self.profile",  caption='picture of a twins', likes= 0)

        self.snap.comments.add(self.comment)

    # def a testcase for instance of the snap
    def test_instance(self):
        self.snap.save()
        self.assertTrue(isinstance(self.snap, Image))

    def test_all_images(self):
        self.snap.save()
        images = Image.all_images()
        self.assertTrue(len(images) > 0)


class ProfileTest(TestCase):
    def setUp(self):
        self.user = Profile(user="zyzu", profile_photo="image.jpg", bio="twins")

    def test_instance(self):
        self.zyzu.save()
        self.assertTrue(isinstance(self.zyzu, Profile))

class CommentTest(TestCase):
    def setUp(self):
        self.nairobi = Comment(comment='one',poster="zyzu",image="")

    def test_instance(self):
        self.nairobi.save()
        self.assertTrue(isinstance(self.nairobi, Comment))
