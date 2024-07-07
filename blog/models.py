from django.db import models
from django.utils import timezone

# Create your models here.

class post(models.Model):
    auther=models.CharField(max_length=150)
    title = models.CharField(max_length=450)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
       return self.title