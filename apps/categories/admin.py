import site
from django.contrib import admin

# Register your models here.
from apps.categories.models import Category

admin.site.register(Category),