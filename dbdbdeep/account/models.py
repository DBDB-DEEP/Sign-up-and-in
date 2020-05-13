from django.db import models

class Account(models.Model):

    email = models.CharField(max_length = 100, unique=True)
    password = models.CharField(max_length = 12)
    name = models.CharField(max_length=10)
    nickname = models.CharField(max_length = 12, unique=True)

    class Meta:
        db_table = "accounts"

# Create your models here.
