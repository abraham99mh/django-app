from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    rfc = models.CharField(max_length=15, blank=True)
    bithday = models.DateField(blank=True)
    sexo = models.CharField(max_length=1)

    def __str__(self):
        return str(self.user)