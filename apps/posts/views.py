from django.shortcuts import render
from apps.posts.models import Post
from apps.categories.models import Category
from apps.settings.models import Settings
from django.db.models import Q


# Create your views here.

def Publication(request, id):
    post = Post.objects.get(id = id)
    categories = Category.objects.all()
    context = {
        'post' : post,
        'categories' : categories,
    }
    return render(request, 'single.html', context)

def post_search(request):
    posts = Post.objects.all()
    qury_obj = request.GET.get('key')
    home = Settings.objects.latest('id')
    if qury_obj:
        posts = Post.objects.filter(Q(title__icontains = qury_obj))
    context = {
        'home' : home, 
        'posts' : posts,
    }
    return render(request, 'index.html', context)
