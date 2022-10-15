from django.db import models
from datetime import datetime
from django.utils.text import slugify
# Create your models here.

class Topic(models.Model):
    topic_name = models.CharField(max_length=30)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.topic_name = str(self.topic_name).capitalize()
        self.slug = slugify(self.topic_name)
        super().save(*args,**kwargs)

    def __str__(self):
        return f"{self.topic_name}"


class Reporter(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="reporters", null=True)
    biography = models.TextField()
    slug = models.SlugField(null=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.full_name)
        self.first_name = str(self.first_name).capitalize()
        self.last_name = str(self.last_name).capitalize()
        super().save(*args,**kwargs)

    def __str__(self):
        return f"{self.full_name}"

class News(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    details = models.TextField()
    slug = models.SlugField(null=True)
    image = models.ImageField(upload_to="news")
    topics = models.ManyToManyField(Topic, related_name="news")
    date = models.DateTimeField()
    reporter = models.ManyToManyField(Reporter, related_name="news")
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.date = datetime.now()
        super().save(*args,**kwargs)

    def __str__(self):
        return f"{self.title}"
