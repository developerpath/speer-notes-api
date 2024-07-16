from authentication.models import User
from django.db import models

class Note(models.Model):
    """Note model."""

    title = models.CharField(max_length=250, db_index=True)
    body = models.TextField(blank=True, db_index=True)
    owner = models.ForeignKey(User, related_name='notes', on_delete=models.CASCADE, null=False)
    shared_with = models.ManyToManyField(User, related_name='shared_notes', blank=True)
    created = models.DateTimeField(auto_now_add=True, null=False)
    updated = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return self.title
