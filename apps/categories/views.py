from unicodedata import category
from django.shortcuts import render
from apps.categories.models import Category
from apps.posts.models import Post

# Create your views here.
def category(request, id):
    category = Category.objects.get(id = id)
    context = {
        'category' : category,
    }
    return render(request, 'categories.html', context)
    


