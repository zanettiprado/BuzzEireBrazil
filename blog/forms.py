from .models import Comment, UserSuggestion
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        
class UserSuggestionForm(forms.ModelForm):
    class Meta:
        model = UserSuggestion
        fields = ['suggestion_text']
        
    def clean_suggestion_text(self):
        suggestion_text = self.cleaned_data.get('suggestion_text')
        if len(suggestion_text) < 10:
            raise forms.ValidationError("Suggestion must be at least 10 characters long.")
        return suggestion_text