from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
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

    favourited = False

    if recipe.favourites.filter(id=request.user.id).exists():
        favourited = True

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
        'comment_form': form,
        'liked': liked,
        'favourited': favourited,
    }

    return render(request, 'recipe_detail.html', context)


class LikeToggle(View):

    def post(self, request, slug, *args, **kwargs):

        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe-detail', args=[slug]))


class FavouriteToggle(View):

    def post(self, request, slug, *args, **kwargs):

        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.favourites.filter(id=request.user.id).exists():
            recipe.favourites.remove(request.user)
        else:
            recipe.favourites.add(request.user)

        return HttpResponseRedirect(reverse('recipe-detail', args=[slug]))
