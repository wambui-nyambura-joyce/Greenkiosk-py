from django.db import models

# Create your models here.
class CustomerSystem(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    def __str__(self):
        return self.name