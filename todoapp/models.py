from django.db import models
from django.utils import timezone

class ToDo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True)
    deadline = models.DateTimeField(default=timezone.now())



    def __str___(self):
        return self.title

