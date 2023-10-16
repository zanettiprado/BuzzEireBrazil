from .models import Comment, UserSuggestion, Post
from django import forms

from django import forms
from .models import Comment, UserSuggestion, Post

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=200, required=True)
    slug = forms.SlugField(max_length=200, required=True)
    content = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = Post
        fields = ['title', 'slug', 'featured_image', 'excerpt', 'content']
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        
class UserSuggestionForm(forms.ModelForm):
    suggestion_text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Tell me what you are thinking...'}))

    class Meta:
        model = UserSuggestion
        fields = ['suggestion_text']

    def clean_suggestion_text(self):
        suggestion_text = self.cleaned_data.get('suggestion_text')
        if len(suggestion_text) < 10:
            raise forms.ValidationError("Suggestion must be at least 10 characters long.")
        return suggestion_text

class SuggestionForm(forms.ModelForm):
    class Meta:
        model = UserSuggestion
        fields = ['suggestion_text']