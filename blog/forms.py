from .models import Recipe, Comment
from django import forms


class PostForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ('title', 'ingredients', 'instructions', 'taste_type', 'skill_level', 'preparation_time', 'status')
        #labels = {'prepartion_time' : 'Prepartion Time (mins)',}


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('body',)
