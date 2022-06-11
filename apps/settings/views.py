from unicodedata import category
from django.shortcuts import render
from apps.settings.models import Settings
from apps.posts.models import Post
from apps.categories.models import Category

def index(request):
    home = Settings.objects.latest('id')
    slide_posts = Post.objects.all()[:3]
    posts = Post.objects.all()
    categories = Category.objects.all().order_by("?")[:2]
    context = {
        'home' : home,
        'posts' : posts,
        'slide_posts' : slide_posts,
        'categories' : categories,
    }
    return render(request, 'index.html', context)
