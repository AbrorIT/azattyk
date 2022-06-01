from unicodedata import category
from django.shortcuts import render
from apps.categories.models import Category
from apps.posts.models import Post

# Create your views here.
def Category(request, id):
    category = Category.objects.all()
    post = Post.objects.get(id = id)
    context = {
        'category' : category,
        'post' : post
    }
    return render(request, 'categories.html', context)
    


