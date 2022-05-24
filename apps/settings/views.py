from django.shortcuts import render
from apps.settings.models import Settings

def index(request):
    home = Settings.objects.latest('id')
    context = {
        'homes' : home
    }
    return render(request, 'index.html', context)
