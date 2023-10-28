from django.db import models

# Create your models here.
class Task(models.Model):
    def __str__(self):
        return self.title
    title =  models.CharField(max_length=25)
    completed = models.BooleanField(default=False)