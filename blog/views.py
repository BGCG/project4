from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Recipe


class RecipeList(generic.ListView):

    model = Recipe
    queryset = Recipe.objects.filter(article_approved=True, status=1).order_by('-publication_date')
    template_name = 'index.html'
    paginate_by = 4


def recipe_detail(request, slug):
    
    recipe = get_object_or_404(Recipe, slug=slug)
    comments = recipe.comments.filter(approved=True)

    liked = False
    
    if recipe.likes.filter(id=request.user.id).exists():
        liked = True
 
    context = {
        'recipe': recipe,
        'comments': comments,
        'liked': liked
    }
    
    return render(request, 'recipe_detail.html', context)
