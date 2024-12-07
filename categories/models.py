from django.db import models

class categories(models.Model):
    cat_fixas =[
        ('lazer', 'Lazer'),
        ('trabalho', 'Trabalho'),
        ('pessoal', 'Pessoal'),
        ('estudos', 'Estudos'),
        ('saude', 'Saúde'),
        ('economia', 'Economia'),
    ]
    
    cat_opcional = models.CharField(max_length=20),
    choices = cat_fixas,
    blank = True,
    null = True
    
    cat_personalizada = models.CharField(max_length=20),
    blank = True,
    null= True
    
def __str__(self):
    return self.cat_opcional or self.cat_personalizada
