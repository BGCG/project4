from .models import Recipe, Comment, ContactRequest
from django import forms


class PostForm(forms.ModelForm):

    """
    Create a post and edit post form
    """

    class Meta:
        model = Recipe
        fields = ('title', 'recipe_image', 'ingredients', 'instructions',
                  'taste_type', 'skill_level', 'preparation_time', 'status')
        labels = {'preparation_time': 'Preparation Time (minutes)'}


class CommentForm(forms.ModelForm):

    """
    Comment form
    """

    class Meta:
        model = Comment
        fields = ('body',)


class ContactForm(forms.ModelForm):

    """
    Comment form
    """

    class Meta:
        model = ContactRequest
        fields = ('first_name', 'last_name', 'email', 'subject', 'message')
        labels = {'first_name': 'First name (optional)',
                  'last_name': 'Last name (optional)'}
