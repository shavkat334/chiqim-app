from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):


    bio = models.TextField()
    date_joined = models.DateTimeField(auto_now_add=True)
    monthly_budjet = models.IntegerField(default=0)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    consent = models.BooleanField(default=False)


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    user_account = models.ForeignKey(User, on_delete=models.CASCADE)


class Expanse(models.Model):
    amount = models.IntegerField(default=0)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    date_created = models.DateField()
    description = models.TextField()
    payment_method = models.CharField(max_length=10)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
