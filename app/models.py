from django.db import models
from django.db.models import UniqueConstraint

class User(models.Model):
    class UserTypes(models.TextChoices):
    #    Admin = 'Admin'
        Owner = 'Owner'

    accountID = models.AutoField(primary_key=True, auto_created=True)
    email = models.EmailField(max_length=30, unique=True, blank=False, null=False)
    userName = models.CharField(max_length=30, unique=True, blank=False, null=False, db_index=True)
    # Need to validate password - do at form level, unsure if we need to salt for security
    password = models.CharField(max_length=30, blank=False, null=False)
    firstName = models.CharField(max_length=30, blank=False, null=False, db_index=True)
    lastName = models.CharField(max_length=30, blank=False, null=False)
    checkings = models.CharField(max_length=10, default="0", null=False)
    savings = models.CharField(max_length=10, default="0", null=False)
    #phone_number = models.CharField(max_length=10, unique=True, blank=True, null=True)
    #home_address = models.CharField(max_length=70, blank=True, null=True)
    accountNumber = models.CharField(max_length=12, unique=True, blank=False)

#class Admin(models.Model):
#    account_ID = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)


class Owner(models.Model):
    accountID = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)