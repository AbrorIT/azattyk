from apps.categories.models import Category
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    post_image = models.ImageField(upload_to = 'post_image/', blank = True, null = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="post_category", null=True)
  
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

class Post_image(models.Model):
    public = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="public_image", null=True)
    public_image = models.ImageField(upload_to = "public_image/", null = True, blank = True)

    class Meta:
        verbose_name = " Фото новостей "
        verbose_name_plural = "Фотки новостей "

