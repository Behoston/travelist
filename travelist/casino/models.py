from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255, null=False, blank=False, unique=True)
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    balance = models.IntegerField(default=0, null=False)
    referrer_email = models.EmailField(default=None, null=True)

    def __str__(self):
        return f'{self.username} | {self.balance}'
