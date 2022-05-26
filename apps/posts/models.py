from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    post_image = models.ImageField(upload_to = 'post_image/', blank = True, null = True)
    # NEWS_CHOICES = [
    #     ('Политика', 'Политика'),
    #     ('Бизнес', 'Бизнес'),
    #     ('Спорт', 'Спорт'),
    # ]
    # news = models.CharField(choices='NEWS_CHOICES', default='Политика', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
