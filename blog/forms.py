from .models import Comment, UserSuggestion, Post
from django import forms


class PostForm(forms.ModelForm):
    """
    Form for creating or editing a blog post.
    """
    title = forms.CharField(max_length=200,
                            required=True,
                            help_text="The title of the blog post.")
    slug = forms.SlugField(max_length=200,
                           required=True,
                           help_text="A URL-friendly version of the title.")
    content = forms.CharField(widget=forms.Textarea,
                              required=True,
                              help_text="The content of the blog post.")

    class Meta:
        model = Post
        fields = ['title', 'slug',
                  'featured_image', 'excerpt', 'content']
        # The fields to include in the form, based on the 'Post' model.


class CommentForm(forms.ModelForm):
    """
    Form for adding a comment to a blog post.
    """
    class Meta:
        model = Comment
        fields = ('body',)
        # The 'body' field is where the user enters their comment.


class UserSuggestionForm(forms.ModelForm):
    """
    Form for users to provide suggestions.
    """
    class Meta:
        model = UserSuggestion
        fields = ['suggestion_text']
        # The 'suggestion_text' field is where users input their suggestions.

    def clean_suggestion_text(self):
        """
        Clean and validate the user's suggestion text.
        """
        suggestion_text = self.cleaned_data.get('suggestion_text')
        return suggestion_text


class SuggestionForm(forms.ModelForm):
    """
    A simplified form for user suggestions.
    """
    class Meta:
        model = UserSuggestion
        fields = ['suggestion_text']
    # The 'suggestion_text' field for a simplified user suggestion form.


class SponsorshipContactForm(forms.Form):
    """
    Contact form for sponsorship inquiries.
    """
    name = forms.CharField(label='Name',
                           max_length=100,
                           required=True, help_text="Your name.")
    email = forms.EmailField(label='Email Address',
                             required=True,
                             help_text="Your email address.")
    business_type = forms.CharField(
        label='Type of Business', max_length=100,
        required=True,
        help_text="Type of business you represent or inquire on behalf of.")
    # Fields for collecting contact information for sponsorship inquiries.
