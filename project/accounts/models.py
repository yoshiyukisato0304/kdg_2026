from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    role = models.ForeignKey('Role',default=1,on_delete=models.CASCADE)
    xp = models.IntegerField(default=0)
    approved = models.BooleanField(default=False)
    last_reset = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username

class Role(models.Model):
    ROLE_CHOICES = [
        ('student', '生徒'),
        ('teacher', '教師'),
        ('staff', 'スタッフ'),
    ]
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return self.name
