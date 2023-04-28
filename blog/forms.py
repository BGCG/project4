from .models import Recipe, Comment
from django import forms


class PostForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ('title', 'recipe_image', 'ingredients', 'instructions',
                  'taste_type', 'skill_level', 'preparation_time', 'status')
        labels = {'preparation_time': 'Preparation Time (minutes)'}


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('body',)
