from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Faketrello(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    priority = models.CharField(max_length=10)
    # status = I think this needs to be a model, for a drop-down menu
