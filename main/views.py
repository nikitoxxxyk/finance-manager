from django.shortcuts import render, redirect
from .models import Category, Transaction, User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.db import models

def index(request):

	if request.user.is_authenticated:
		transactions = Transaction.objects.filter(user=request.user)
		total_income = transactions.filter(type_transaction='income').aggregate(total=models.Sum('amount'))['total'] or 0

		total_expense = transactions.filter(type_transaction='expense').aggregate(total=models.Sum('amount'))['total'] or 0

		total_balance = total_income - total_expense
	else:
		total_income = 0
		total_expense = 0
		total_balance = 0


	hello_text = 'Я твой финансовый помощник, записывай сюда свои доходы и расходы, разбивай их по категориям и прокачивай свою финансовую грамотность!'

	context = {
		'title': 'Finance Manager',
		'content': hello_text, 
		'total_income': total_income,
		'total_expense': total_expense,
		'total_balance': total_balance,
	}

	return render(request, 'main.html', context)

def register_view(request):
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, 'Регистрация прошла успешно!')
			return redirect('main:home')
	else:
		form = CustomUserCreationForm()
	
	context = {
		'form': form
	}

	return render(request, 'register/register.html', context)
		
def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('main:home')
	else:
		form = AuthenticationForm()
			
	context = {
				'form': form
			}
	
	return render(request, 'register/login.html', context)

@login_required
def logout_view(request):
	logout(request)
	return redirect('main:home')


