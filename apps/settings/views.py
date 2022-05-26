from django.shortcuts import render
from apps.settings.models import Settings
from apps.posts.models import Post

def index(request):
    home = Settings.objects.latest('id')
    posts = Post.objects.all()
    context = {
        'homes' : home,
        'posts' : posts,
    }
    return render(request, 'index.html', context)
