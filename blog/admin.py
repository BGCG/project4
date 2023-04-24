from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    summernote_fields = ('ingredients', 'instructions',)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('status', 'edited_date')
    list_display = ('title', 'author', 'edited_date',
                    'publication_date', 'article_approved')
    search_fields = ['title', 'instructions', 'ingredients']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'created_on', 'approved', 'recipe')
    list_filter = ('created_on', 'approved')
    search_fields = ('name', 'body', 'recipe')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

