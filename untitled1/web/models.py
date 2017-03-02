from django.db import models

# Create your models here.

class user(models.Model):
    first_name = models.CharField(max_length = 50, default="")
    last_name = models.CharField(max_length=50, default="")
    useremail = models.CharField(max_length=50, default="")
    username = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=50, default="")


    def __str__(self):
        return "{} : {}".format(self.first_name,self.user_name)