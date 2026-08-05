from django.shortcuts import render,redirect
from cashmanagment_app.models import *
from cashmanagment_app.forms import *
from django.contrib import messages
from django.contrib.auth import login,logout
from django.db.models import Sum
from django.contrib.auth.decorators import login_required

# Create your views here.
def register_page(request):
    if request.method == 'POST':
        form_data = RegisterForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,'Registration Successfully')
            return redirect('login_page')

    form_data = RegisterForm()

    context = {
        'form_data' : form_data,
        'form_title' : 'Registration form',
        'form_btn' : 'Register',
    }
    return render(request,'master/base-form.html',context)

def login_page(request):
    if request.method == 'POST':
        form_data = LoginForm(request,request.POST)
        if form_data.is_valid():
            user = form_data.get_user()
            login(request,user)
            messages.success(request,'Login Successfully')
            return redirect('dashboard_page')

    form_data = LoginForm()

    context = {
        'form_data' : form_data,
        'form_title' : 'Login form',
        'form_btn' : 'Login',
    }
    return render(request,'master/base-form.html',context)

@login_required
def logout_page(request):
    logout(request)
    return redirect('login_page')

@login_required
def dashboard_page(request):
    cash_data = AddCashModel.objects.filter(user = request.user)
    expense_data = ExpenseModel.objects.filter(user = request.user)

    total_cash = cash_data.aggregate(
        total = Sum('amount') #for add cash model
    )['total'] or 0
    total_expense = expense_data.aggregate(
        total  = Sum('amount') # for expense model
    )['total'] or 0 # showing total value into dictionary

    current_balance = total_cash - total_expense

    context = {
        'total_cash' : total_cash,
        'total_expense' : total_expense,
        'current_balance' : current_balance,
        'cash_data' : cash_data,
        'expense_data' : expense_data,
    }
    return render(request,'dashboard-page.html',context)

@login_required
def cash_list(request):
    cash_data = AddCashModel.objects.filter(user = request.user)

    context = {
        'cash_data' : cash_data
    }
    return render(request,'cash-list.html',context)

@login_required
def add_cash(request):
    if request.method == 'POST':
        form_data = AddCashForm(request.POST)
        if form_data.is_valid():
            data = form_data.save(commit=False)
            data.user = request.user # there data.user(addcashmodel user) = request.user(login user) // request use for calling the user 
            data.save()
            messages.success(request,'Cash Added Successfully')
            return redirect('cash_list')

    form_data = AddCashForm()

    context = {
        'form_data' : form_data,
        'form_title' : 'Add Your Cash',
        'form_btn' : 'Added',
    }
    return render(request,'master/base-form.html',context)

@login_required
def edit_page(request,id):
    cash_data = AddCashModel.objects.get(id = id)
    if request.method == 'POST':
        form_data = AddCashForm(request.POST,instance= cash_data)
        if form_data.is_valid():
            data = form_data.save(commit=False)
            data.user = request.user # there data.user(addcashmodel user) = request.user(login user) // request use for calling the user 
            data.save()
            messages.success(request,'Added Successfully')
            return redirect('cash_list')

    form_data = AddCashForm(instance= cash_data)
    
    context = {
            'form_data' : form_data,
            'form_title' : 'Edit Your Cash',
            'form_btn' : 'Edited',
        }

    return render(request,'master/base-form.html',context)

@login_required
def delete_page(request,id):
    cash_data = AddCashModel.objects.get(id = id)
    cash_data.delete()
    return redirect('cash_list')

@login_required
def expense_list(request):
    expense_data = ExpenseModel.objects.filter(user = request.user)

    context = {
        'expense_data' : expense_data,
    }

    return render(request,'expense_list.html',context)

@login_required
def add_expense(request):
    if request.method == 'POST':
        form_data = ExpenseForm(request.POST)
        if form_data.is_valid():
            data = form_data.save(commit=False)
            data.user = request.user # there data.user(expensecashmodel user) = request.user(login user) // request use for calling the user
            data.save()
            messages.success(request,'Expense Added Successfully')
            return redirect('expense_list')

    form_data = ExpenseForm()

    context = {
        'form_data' : form_data,
        'form_title' : 'Add Your Expense',
        'form_btn' : 'Added',
    }
    return render(request,'master/base-form.html',context)

@login_required
def edit_expense(request,id):
    expense_data = ExpenseModel.objects.get(id = id)
    if request.method == 'POST':
        form_data = ExpenseForm(request.POST,instance=expense_data)
        if form_data.is_valid():
            data = form_data.save(commit=False)
            data.user = request.user # there data.user(expensecashmodel user) = request.user(login user) // request use for calling the user
            data.save()
            messages.success(request,'Expense Added Successfully')
            return redirect('expense_list')

    form_data = ExpenseForm(instance=expense_data)

    context = {
        'form_data' : form_data,
        'form_title' : 'Edit Your Expense',
        'form_btn' : 'Edited',
    }
    return render(request,'master/base-form.html',context)

@login_required
def delete_expense(request,id):
    expense_data = ExpenseModel.objects.get(id = id)
    expense_data.delete()
    return redirect('expense_list')

   
