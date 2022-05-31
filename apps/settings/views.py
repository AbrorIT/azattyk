from django.shortcuts import render
from apps.settings.models import Settings
from apps.posts.models import Post

def index(request):
    home = Settings.objects.latest('id')
    slide_posts = Post.objects.all()[:3]
    posts = Post.objects.all()
    context = {
        'homes' : home,
        'posts' : posts,
        'slide_posts' : slide_posts,
    }
    return render(request, 'index.html', context)
