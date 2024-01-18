from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    book_price = models.IntegerField(verbose_name='Kitob narixi')
    book_image = models.ImageField(verbose_name='Kitob surati')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
