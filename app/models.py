from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100,null=True)
    content = models.TextField(max_length=3000,null=True)

    def __str__(self):
        return self.title

