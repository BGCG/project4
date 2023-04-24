from . import views
from django.urls import path


urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('posts/<slug:slug>', views.recipe_detail, name='recipe-detail'),
]