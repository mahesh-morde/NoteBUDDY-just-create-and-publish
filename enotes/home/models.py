from django.db import models

from authh.models import Signup


# Create your models here.
class Notes(models.Model):
    signup = models.ForeignKey(Signup, on_delete=models.CASCADE)
    Title = models.CharField(max_length=200, null=True)
    Content = models.CharField(max_length=450, null=True)
    CreationDate = models.DateTimeField(auto_now_add=True)
    UpdationDate = models.DateField(null=True)
    publish = models.BooleanField(default=False) 

    def __str__(self):
        return self.Title
