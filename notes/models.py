from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)

    image = models.ImageField(
        upload_to='notes/images', 
        blank=True, 
        null=True,
    )

    is_active = models.BooleanField(blank=True, default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    