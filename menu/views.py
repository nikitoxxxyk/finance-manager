from django.shortcuts import render, redirect
from main.models import Category, Transaction
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import TransactionForm
from django.db import models

@login_required
def menu(request):
	title_trans = '💰 Транзакции'
	content_trans = 'Сюда ты можешь добавить любой уход, либо наоборот приход денежных средств'
	title_budget = '🏦 Мой бюджет'
	content_budget = 'Задай свой бюджет, прям все, что имеется у тебя в кармане :)'
	title_cat = '📚 Категорию'
	content_cat = 'Добавляй категории, чтобы каждой транзакции было своё место!'
	title_debt = '💸 Долги'
	content_debt = 'Тут ты можешь фиксировать сколько ты одолжил, либо сколько тебе заняли'
	title_account = '💲Счета'
	content_account = 'Сюда вы можете добавлять счета своих банков или оставить один общий'

	context = {
		'title_trans': title_trans,
		'content_trans': content_trans,
		'title_budget': title_budget,
		'content_budget': content_budget,
		'title_cat': title_cat,
		'content_cat': content_cat,
		'title_debt': title_debt,
		'content_debt': content_debt,
		'title_account': title_account,
		'content_account': content_account
	}

	return render(request, 'menu/menu.html', context)

@login_required
def transaction_add(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            messages.success(request, '✅ Транзакция добавлена!')
            return redirect('menu:transaction_list')
    else:
        form = TransactionForm()
    
    return render(request, 'menu/add_transaction.html', {'form': form})

@login_required
def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    
    total_income = transactions.filter(type_transaction='income').aggregate(
        total=models.Sum('amount')
    )['total'] or 0
    
    total_expense = transactions.filter(type_transaction='expense').aggregate(
        total=models.Sum('amount')
    )['total'] or 0
    
    total_balance = total_income - total_expense
    
    context = {
        'transactions': transactions,
        'total_income': total_income,
        'total_expense': total_expense,
        'total_balance': total_balance, 
    }
    
    return render(request, 'menu/transaction_list.html', context)

@login_required
def category_list(request):
    categories = Category.objects.filter(user=request.user)
    context = {'categories': categories}
    return render(request, 'menu/category_list.html', context)

# @login_required
# def add_budget(request):
# 	pass
# @login_required
# def add_cat(request):
# 	pass
# @login_required
# def add_debt(request):
# 	pass
# @login_required
# def add_account(request):
# 	pass
