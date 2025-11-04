from django.db import models

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.first_name
