from django.shortcuts import render
from apps.posts.models import Post
from apps.categories.models import Category

# Create your views here.

def Publication(request, id):
    post = Post.objects.get(id = id)
    categories = Category.objects.all()
    context = {
        'post' : post,
        'categories' : categories,
    }
    return render(request, 'single.html', context)