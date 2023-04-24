from django.contrib import admin
from .models import Recipe
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    summernote_fields = ('ingredients', 'instructions',)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('status', 'edited_date')
    list_display = ('title', 'author', 'edited_date',
                    'publication_date', 'article_approved')
    search_fields = ['title', 'instructions', 'ingredients']

