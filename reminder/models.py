from django.db import models
from pygments.lexers import get_all_lexers

LEXERS = [item for item in get_all_lexers() if item[1]]

class Reminders(models.Model):
    email = models.EmailField()
    text = models.TextField()
    delay = models.IntegerField()

    class Meta:
        ordering = ['email']