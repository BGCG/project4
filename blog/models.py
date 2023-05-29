from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

# Create your models here.


class Recipe(models.Model):

    """
    Set choices for status, difficulty and taste fields
    """

    STATUS = ((0, "Draft"), (1, "Published"))
    DIFFICULTY = ((None, "Choose diffucluty level"), (0, "Easy"), (1, "Intermediate"), (2, "Advanced"),)
    TASTE = ((None, "Choose your taste"), (1, "Sweet"), (2, "Savoury"),)

    """
    Define Recipe model fields
    """

    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, null=False, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    publication_date = models.DateField('date published', auto_now_add=True)
    edited_date = models.DateField(auto_now=True)
    ingredients = models.TextField(default=None)
    instructions = models.TextField(default=None)
    recipe_image = CloudinaryField('image', default='placeholder')
    article_approved = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=0)
    taste_type = models.IntegerField(choices=TASTE)
    skill_level = models.IntegerField(choices=DIFFICULTY)
    preparation_time = models.PositiveIntegerField(blank=False)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    favourites = models.ManyToManyField(User, related_name='blog_favourites', blank=True)

    """
    order recipes by most recently published
    """

    class Meta:
        ordering = ['-edited_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("recipe-detail", kwargs={"slug": self.slug})

    """
    return total numbers of likes for each recipe
    """
    def num_of_likes(self):
        return self.likes.count()

    """
    return total numbers of favourites for each recipe
    """

    def num_of_favorites(self):
        return self.favourites.count()


class Comment(models.Model):

    """
    Define Comment model fields
    """

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    created_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    approved = models.BooleanField(default=False)

    """
    order based on which comment was created first
    """
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class ContactRequest(models.Model):

    """
    Define Contact model fields
    """

    QUESTION_CATEGORIES = [
        (None, "How can we help?"),
        ("Accounts", "There's something wrong with my account"),
        ("Feedback", "I would like to provide some feedback"),
        ("Complaint", "I would like to make a complaint"),
        ("Technical issue", "I would like to report a technical issue"),
        ("Other", "Other"),
    ]

    name = models.CharField(default='', null=True, blank=True, max_length=80)
    email = models.EmailField()
    question_type = models.CharField(choices=QUESTION_CATEGORIES, max_length=80)
    subject = models.CharField(max_length=180)
    message = models.TextField()
    contact_date = models.DateTimeField(auto_now_add=True)
