from myblog.models import Post
from django.test import TestCase
from django.contrib.auth.models import User


class PostTestCase(TestCase):
    fixtures = ['myblog_test_fixture.json',]

    def setUp(self):
        self.user= User.objects.get(pk=1)

    def  test_string_representation(self):
         expected ="This is title"
         p1 = Post(title = expected)
         actual = str(p1)
         self.assertNotEqual(expected,actual)


# Create your tests here.
