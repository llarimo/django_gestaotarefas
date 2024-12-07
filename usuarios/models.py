from django.db import models

class usuarios(models.Model):
    name = models.CharField(max_length=30)
    
