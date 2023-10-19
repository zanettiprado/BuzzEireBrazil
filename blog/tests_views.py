from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Comment, UserSuggestion


class TestViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            excerpt='Test excerpt',
            content='Test content',
            author=self.user,
            status=1,
        )
        self.comment = Comment.objects.create(
            name=self.user,
            email=self.user.email,
            body='Test comment body',
            post=self.post,
        )
        self.suggestion = UserSuggestion.objects.create(
            user=self.user,
            suggestion_text='Test suggestion',
        )

    def test_create_post_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('create_post'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_post.html')

    def test_post_like_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('post_like', args=[self.post.slug]))
        self.assertEqual(response.status_code, 302)

    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_edit_post_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('edit_post', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_post.html')

    def test_delete_post_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('delete_post', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_post.html')

    def test_suggestion_dislike_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('suggestion_dislike', args=[self.suggestion.id]))
        self.assertEqual(response.status_code, 302)

    def test_edit_suggestion_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('edit_suggestion', args=[self.suggestion.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_suggestion.html')
