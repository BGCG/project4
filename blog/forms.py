from .models import Recipe, Comment
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
