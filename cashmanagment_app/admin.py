from django.contrib import admin
from cashmanagment_app.models import *

# Register your models here.
admin.site.register([UserModel,AddCashModel,ExpenseModel])
