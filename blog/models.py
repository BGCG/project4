from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Recipe(models.Model):

    STATUS = ((0, "Draft"), (1, "Published"))
    DIFFICULTY = ((None, "Choose diffucluty level"), (0, "Easy"), (1, "Intermediate"), (2, "Advanced"),)
    TASTE = ((None, "Choose your taste"), (1, "Sweet"), (2, "Savoury"),)

    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, null=False, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    publication_date = models.DateField('date published', auto_created=True)
    edited_date = models.DateField(auto_created=True)
    ingredients = models.TextField(default=None)
    instructions = models.TextField(default=None)
    recipe_image = CloudinaryField('image', default='placeholder')
    article_approved = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=0)
    taste_type = models.IntegerField(choices=TASTE)
    skill_level = models.IntegerField(choices=DIFFICULTY)
    preparation_time = models.PositiveIntegerField(blank=False, validators=[MinValueValidator(1), MaxValueValidator(2000)])
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    favourites = models.ManyToManyField(User, related_name='blog_favourites', blank=True)

    class Meta:
        ordering = ['-publication_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"slug": self.slug})

    def num_of_likes(self):
        return self.likes.count()
    
    def num_of_favorites(self):
        return self.favourites.count()


class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    created_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    approved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['created_on']
    
    def __str__(self):
        return f"Comment {self.body} by {self.name}"
