from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title=models.CharField(max_length=100, unique='True', null=False)
    description=models.CharField(max_length=1000,null=False)

    def __str__(self):
        return self.user.username