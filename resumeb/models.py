from django.db import models

# Create your models here.
class Forms(models.Model):
    myname=models.CharField(max_length=32)
    lname=models.CharField(max_length=32)
    no=models.IntegerField()
    email=models.CharField(max_length=323)
    comments=models.CharField(max_length=323)
    company=models.CharField(max_length=323)
    protext=models.TextField()
    indtext=models.TextField()
    
    def __str__(self):
        return self.myname + " " + self.lname
    
