from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Blog(models.Model):
    class Meta:
        ordering = '-created_at',

    title = models.CharField(max_length=250)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super().save()

    def get_absolute_url(self):
        return reverse("blog", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


class Subscription(models.Model):
    email = models.EmailField(null=True, blank=True, unique=True)

    def __str__(self):
        return self.email
