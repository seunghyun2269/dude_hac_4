from django.db import models
from accounts.models import Signup
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    pub_date = models.DateTimeField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)