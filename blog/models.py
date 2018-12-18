from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    tags = models.ManyToManyField(Tag)
    category = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    comments = models.BooleanField(default=True)
    content = RichTextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-date',)