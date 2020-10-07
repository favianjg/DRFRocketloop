from django.db import models
from pygments.lexers import get_all_lexers
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]


class Boards(models.Model):
    name = models.CharField(max_length=100, blank=True, default='nonameboard')

    class Meta:
        ordering = ['name']

class Todos(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='nonametodo')
    done = models.BooleanField(default=False)
    board = models.ForeignKey(Boards, related_name='todos', on_delete=models.CASCADE)

    class Meta:
        ordering = ['title']