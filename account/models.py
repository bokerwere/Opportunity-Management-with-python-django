from django.db import models
from  django.contrib.auth.models import User


# Create your models here.

class Account(models.Model):
  name=models.CharField(max_length=200,null=True)
  address=models.CharField(max_length=200)
  user=models.ForeignKey(User ,null=True,on_delete=models.CASCADE ,unique=False)
  date_created = models.DateTimeField(auto_now_add=True, null=True)


  def __str__(self):
    return self.name



class Stage(models.Model):
    title=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.title


class Opportunity(models.Model):
    name=models.CharField(max_length=200)
    amount=models.FloatField(max_length=200)
    account=models.ForeignKey(Account,on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE )


    def __str__(self):
        return self.name





