from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    #One to many relationship between Post and User tables
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title