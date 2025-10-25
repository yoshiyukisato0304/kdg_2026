from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('student', '生徒'),
        ('teacher', '教師'),
        ('staff', 'スタッフ'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
    xp = models.IntegerField(default=0)
    approved = models.BooleanField(default=False)
    last_reset = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username
