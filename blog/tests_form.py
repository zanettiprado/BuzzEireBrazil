from django.test import TestCase
from .forms import PostForm, CommentForm, UserSuggestionForm, SponsorshipContactForm


class FormsTestCase(TestCase):
    def test_post_form_valid_data(self):
        form_data = {
            'title': 'Test Post Title',
            'slug': 'test-post-slug',
            'content': 'This is a test post content.',
        }

        form = PostForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_comment_form_valid_data(self):
        form_data = {
            'body': 'This is a test comment.',
        }

        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_user_suggestion_form_valid_data(self):
        form_data = {
            'suggestion_text': 'This is a test suggestion.',
        }

        form = UserSuggestionForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_sponsorship_contact_form_valid_data(self):
        form_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'business_type': 'Test Business',
        }

        form = SponsorshipContactForm(data=form_data)
        self.assertTrue(form.is_valid())
