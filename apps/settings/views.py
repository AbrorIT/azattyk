from django.shortcuts import render

# Create your views here.

from settings.models import Settings

def index(request):
    home = Settings.objects.latest('id')
    context = {
        'homes' : home
    }
    return render(request, 'index.html', context)
