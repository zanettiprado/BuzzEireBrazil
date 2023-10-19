from django.test import TestCase
from .models import Post, Comment, UserSuggestion, Suggestion
from django.contrib.auth.models import User


class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='testuser')
        Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=user,
            content='This is a test post content.'
        )

    def test_title_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_object_name_is_title(self):
        post = Post.objects.get(id=1)
        expected_object_name = post.title
        self.assertEqual(str(post), expected_object_name)
