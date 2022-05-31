from unicodedata import category
from django.shortcuts import render
from apps.categories.models import Category

# Create your views here.
def Category(request, id):
    category = Category.objects.all()
    context = {
        'category' : category,
    }
    return render(request, 'categories.html', context)
    


