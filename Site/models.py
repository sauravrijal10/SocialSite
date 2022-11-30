from django.db import models
from django.contrib.auth.models import User

class account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

