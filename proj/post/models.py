<<<<<<< HEAD

=======
from django.db import models
from accounts.models import Signup
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    comment = models.ForeignKey(Coment, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    pub_date = models.DateTimeField()
>>>>>>> b1985b34ad254adc5855ae64d6abd267a0430cd8
