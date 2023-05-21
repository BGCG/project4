from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from .models import Recipe
from .forms import CommentForm, PostForm, ContactForm
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


class RecipeList(generic.ListView):
    """
    View paginated recipe list
    """
    model = Recipe
    queryset = Recipe.objects.filter(article_approved=True, status=1).order_by(
                                                           '-edited_date')
    template_name = 'index.html'
    paginate_by = 4


class AllRecipes(generic.ListView):
    """
    View all recipes in site
    """
    model = Recipe
    queryset = Recipe.objects.filter(article_approved=True, status=1)
    template_name = 'all_recipes.html'


def recipe_detail(request, slug):

    """
    View details of recipe and comments, as well as post a comment
    """

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

    """
    Toggling of the like button
    """

    def post(self, request, slug, *args, **kwargs):

        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe-detail', args=[slug]))


class FavouriteView(View):

    """
    Toggling of favourite button
    Get user's favourite recipe list
    """

    def post(self, request, slug, *args, **kwargs):

        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.favourites.filter(id=request.user.id).exists():
            recipe.favourites.remove(request.user)
        else:
            recipe.favourites.add(request.user)

        return HttpResponseRedirect(reverse('recipe-detail', args=[slug]))

    def get(self, request, *args, **kwargs):

        fav_recipes = Recipe.objects.filter(favourites=request.user,
                                            article_approved=True)

        return render(request, 'favourite_list.html',
                               {'fav_recipes': fav_recipes})


@login_required
def create_post(request):

    """
    Create new post on site
    """

    new_post = None

    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.author = request.user
            post_form.save()

            if new_post.status == 0:
                messages.info(request, "Your draft post has been saved in"
                              " 'Post management'!")
            elif new_post.status == 1:
                messages.info(request, "Your post is awaiting approval!")
            return redirect('home')
        else:
            request.session['new_post_data'] = request.POST
            return render(request, 'create_post.html',
                                   {'post_form': post_form})
    else:
        form_data = request.session.get('new_post_data')
        PostForm(form_data)

    post_form = PostForm()

    context = {
        'post_form': post_form,
        'new_post': new_post,
    }

    return render(request, 'create_post.html', context)


@login_required
def your_posts_view(request):

    """
    View your post list
    """

    your_published_posts = Recipe.objects.filter(author=request.user, status=1,
                                                 article_approved=True)
    your_draft_posts = Recipe.objects.filter(author=request.user, status=0)

    context = {
        'your_published_posts': your_published_posts,
        'your_draft_posts': your_draft_posts,
    }

    return render(request, 'your_posts.html', context)


@login_required
def edit_post(request, slug):

    """
    Edit a post
    """

    recipe = get_object_or_404(Recipe, slug=slug)

    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES, instance=recipe)

        if post_form.is_valid():
            recipe.article_approved = False
            post_form.save()
            if recipe.status == 0:
                messages.info(request, "Your draft post has been saved "
                                       "in 'Post management'!")
            elif recipe.status == 1:
                messages.info(request,
                              "Your edited post is awaiting approval!")
            return redirect('home')
        else:
            if IntegrityError:
                messages.error(request, "We could not create your post due to "
                               "invalid input. Please ensure your title"
                               "is unqiue.")
            else:
                messages.error(request, "Something went wrong"
                               "- please try to create your post again.")

    post_form = PostForm(instance=recipe)

    return render(request, 'edit_post.html', {'post_form': post_form,
                                              'recipe': recipe})


@login_required
def delete_post(request, slug):

    """
    Delete a post
    """

    recipe = get_object_or_404(Recipe, slug=slug)
    recipe.delete()
    messages.info(request, "Post successfully deleted")
    return redirect('home')


def contact_request(request):

    """
    Allow user to send contact request to admin
    """

    new_contact = None

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            new_contact = form.save(commit=False)
            new_contact.save()
    else:
        contact_form = ContactForm()

    context = {
        'contact_form': ContactForm(),
        'new_contact': new_contact,
    }

    return render(request, 'contact_us.html', context)
