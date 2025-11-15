from django.db import models
from django.conf import settings   # <– import this

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    # CHANGE THIS:
    # author = models.CharField(max_length=100)

    # TO THIS:
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,          # usually auth.User
        on_delete=models.CASCADE,         # Deletes posts if user is deleted
        null=True,                         # allow temporary null during migration
        blank=True,
        related_name='blog_posts'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    organisation = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.full_name