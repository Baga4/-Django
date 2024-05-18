from django.db import models

# Create your models here.

class post(models.Model):
    auther=models.CharField(max_length=150)
    title = models.CharField(max_length=450)
    description = models.TextField()
    
    def __str__(self):
       return self.title