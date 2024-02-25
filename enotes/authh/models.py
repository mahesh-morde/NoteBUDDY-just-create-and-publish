from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Signup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ContactNo = models.CharField(max_length=10, null=True)
    About = models.CharField(max_length=450, null=True)
    Role = models.CharField(max_length=150, null=True)
    RegDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name