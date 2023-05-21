from django.contrib import admin
from .models import Recipe, Comment, ContactRequest
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    summernote_fields = ('ingredients', 'instructions',)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('status', 'edited_date')
    list_display = ('title', 'author', 'edited_date',
                    'publication_date', 'article_approved')
    search_fields = ['title', 'instructions', 'ingredients']

    actions = ['approve_recipe']

    def approve_recipe(self, request, queryset):
        queryset.update(article_approved=True)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'created_on', 'approved', 'recipe')
    list_filter = ('created_on', 'approved')
    search_fields = ('body', 'recipe')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(ContactRequest)
class ContactAdmin(admin.ModelAdmin):

    list_display = ('email', 'question_type', 'subject', 'message', 'contact_date')
    list_filter = ('contact_date',)
    search_fields = ('email', 'subject', 'message')
