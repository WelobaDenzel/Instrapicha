from django.test import TestCase
from .models import *

# Create your tests here.

class ProfileTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(id = 1, user='zyzu')
        self.profile = Profile.objects.create(user = self.user,bio = 'blow away')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))
