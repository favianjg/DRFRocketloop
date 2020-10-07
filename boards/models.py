from django.db import models
from pygments.lexers import get_all_lexers

LEXERS = [item for item in get_all_lexers() if item[1]]


class Boards(models.Model):
    name = models.CharField(max_length=100, blank=True, default='nonameboard')

    class Meta:
        ordering = ['created']

class Todos(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='nonametodo')
    done = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']