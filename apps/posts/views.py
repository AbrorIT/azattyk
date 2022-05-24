from django.shortcuts import render
from apps.posts.models import Post

# Create your views here.

def Publication(request, id):
    post = Post.objects.all().order_by('-id')
    context = {
        'post' : post,
    }
    return render(request, 'single.html', context)