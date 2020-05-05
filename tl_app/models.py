from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.

class Task(models.Model):
    task_title = models.CharField(max_length = 200)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(blank=True, null=True)
    is_complete = models.BooleanField(default = False)



    def publish(self):
        self.created_date = timezone.now()
        self.save()


    def __str__(self):
        return self.task_title