from django.db import models
from django.db import IntegrityError, models, router, transaction


# Create your models here.
class Forms(models.Model):
    myname = models.CharField(max_length=32)
    lname = models.CharField(max_length=32)
    no = models.IntegerField()
    email = models.CharField(max_length=323)
    comments = models.CharField(max_length=323)
    company = models.CharField(max_length=323)
    protext = models.TextField()
    indtext = models.TextField()


class F(models.Model):
    # try:
    dname = models.CharField(
        max_length=32, default="aj", null=True)
    dsurname = models.CharField(
        max_length=32, default="aj", null=True)
    dpincode = models.IntegerField(default=9, null=True)
    dcity = models.CharField(
        max_length=32, default="aj", null=True)
    dcountry = models.CharField(
        max_length=32, default="aj", null=True)
    dphoneno = models.IntegerField(default=9, null=True)
    demail = models.CharField(
        max_length=323, default="aj", null=True)
    desc = models.CharField(
        max_length=323, default="aj", null=True)
    dschool = models.CharField(
        max_length=323, default="aj", null=True)
    dposition = models.CharField(
        max_length=323, default="aj", null=True)
    dcompany = models.CharField(
        max_length=323, default="aj", null=True)
    dc1 = models.CharField(max_length=323, default="aj", null=True)
    dcc1 = models.CharField(
        max_length=323, default="aj", null=True)
    dm1 = models.CharField(
        max_length=323, default="aj", null=True)
    dm2 = models.CharField(
        max_length=323, default="aj", null=True)
    dcollege = models.TextField(
        max_length=323, default="aj", null=True)
    ddegree = models.TextField(
        max_length=323, default="aj", null=True)
    dmonth = models.CharField(
        max_length=323, default="aj", null=True)
    # except IntegrityError:
    #     pass
