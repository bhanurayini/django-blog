from django.db import models
from django.utils import timezone

# Create your models here.

# post model with title,description,author,created at, published at as properties
class Post(models.Model):
    title = models.CharField(max_length = 20)
    description = models.TextField()
    author = models.ForeignKey('auth.User')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def publishe(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
