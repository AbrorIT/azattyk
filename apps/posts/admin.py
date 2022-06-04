import imp
from django.contrib import admin
from apps.posts.models import Post
from apps.posts.models import Post_image

# Register your models here.
admin.site.register(Post)
admin.site.register(Post_image)