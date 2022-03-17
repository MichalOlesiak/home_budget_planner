from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Creating class of post
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
# When user will be deleted his posts will be deleted too 
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title