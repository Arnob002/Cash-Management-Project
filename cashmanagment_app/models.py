
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserModel(AbstractUser):
    def __str__(self):
        return f'{self.username}'

#AddCash (user (many to one User), source, datetime, amount, description) 
class AddCashModel(models.Model):
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='cash_info',null=True)
    source = models.CharField(max_length=100,null=True)
    datetime = models.DateTimeField(null=True)
    amount = models.FloatField(null=True)
    description = models.TextField(null=True)
    def __str__(self):
        return f'{self.user}'

#Expense (user {many to one User}, description, amount, datetime) 
class ExpenseModel(models.Model):
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='expense_info',null=True)
    datetime = models.DateTimeField(null=True)
    amount = models.FloatField(null=True)
    description = models.TextField(null=True)
    def __str__(self):
        return f'{self.user}'