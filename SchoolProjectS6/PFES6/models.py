from django.db import models

# Create your models here.


class Users(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='profile_pics', blank=True)
    roles = [
        ('s', 'student'),
        ('t', 'teacher')
    ]
    role = models.CharField(
        max_length=2,
        choices=roles,
    )
