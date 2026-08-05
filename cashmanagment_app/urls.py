from django.urls import path
from cashmanagment_app.views import *

urlpatterns = [
    path('',register_page,name='register_page'),
    path('login-page/',login_page,name='login_page'),
    path('logout-page/',logout_page,name='logout_page'),

    path('dashboard-page/',dashboard_page,name='dashboard_page'),

    path('cash-list/',cash_list,name='cash_list'),
    path('add-cash/',add_cash,name='add_cash'),
    path('edit-page/<str:id>/',edit_page,name='edit_page'),
    path('delete_page/<str:id>/',delete_page,name='delete_page'),

    path('expense-list/',expense_list,name='expense_list'),
    path('add-expense/',add_expense,name='add_expense'),
    path('edit-expense/<str:id>/',edit_expense,name='edit_expense'),
    path('delete-expense/<str:id>/',delete_expense,name='delete_expense'),
    

]