from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Recipe
from .forms import CommentForm
from django.contrib import messages


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
    
    comment = None
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.name = request.user.username
            comment = form.save(commit=False)
            comment.recipe = recipe
            comment.save()
            # messages.info(request, "Your comment is awaiting approval!")
            # return redirect('recipe-detail', slug=recipe.slug)
    else:
        form = CommentForm()
 
    context = {
        'recipe': recipe,
        'comments': comments,
        'comment': comment,
        'liked': liked,
        'comment_form': form,
    }
    
    return render(request, 'recipe_detail.html', context)
