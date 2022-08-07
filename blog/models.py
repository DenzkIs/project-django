from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User  # менее безопасный метод вызова модель User
from django.contrib.auth import get_user_model  # это более безопасный вызов модели User

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)  # или auto_now_add=True
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Post {self.title} by {self.author.username}'  # Откуда взяться username?