from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	def __str__(self):
		return self.username

class Category(models.Model):
	title = models.CharField(max_length=150, verbose_name='Категория')
	user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='categories')

	def __str__(self):
		return self.title


class Transaction(models.Model):
	title = models.CharField(max_length=150, verbose_name='Транзакция')
	amount = models.DecimalField(verbose_name='Сумма', max_digits=12, decimal_places=2)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transactions")
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True) # Чтобы с удалением категории не удалить все транзакции
	date = models.DateTimeField(auto_now_add=True)
	description = models.TextField(blank=True)
	# debt = models.ForeignKey('Debt', on_delete=models.SET_NULL, null=True, blank=True, related_name='payments')
	TYPE_TRANS = (
		('income', 'Доход'),
		('expense', 'Расход'),
	)
	type_transaction = models.CharField(max_length=10, choices=TYPE_TRANS)
	def __str__(self):
		return self.title

# class Debt(models.Model):
# 	title = models.CharField(max_length=150)
# 	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="debts")

# 	TYPE_DEBT = (
# 		('I am owed', 'мне должны'),
# 		('I owe', 'я должен')
# 	)
# 	type_debt = models.CharField(max_length=150, choices=TYPE_DEBT)

# 	TYPE_CATEGORY = (
# 		('personal', 'долг между людьми без %'),
# 		('loan', 'долг между людьми c %'),
# 		('credit', 'кредит'),
# 		('mortgage', 'ипотека'),
# 		('installment', 'рассрочка'),
# 		('microfinance', 'микрозайм')
# 	)

# 	debt_category = models.CharField(max_length=20, choices=TYPE_CATEGORY, default='personal')

# 	amount = models.DecimalField(max_digits=12, decimal_places=2)
# 	interest_rate = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

# 	TYPE_INTEREST = (
# 		('floating rate', 'плавающая ставка'),
# 		('fix rate', 'фиксированная ставка')
# 	)
# 	interest_type = models.CharField(max_length=150, choices=TYPE_INTEREST, null=True, blank=True)
# 	creditor_name = models.CharField(max_length=150, blank=True)
# 	CREDITOR_TYPE_CHOICES = (
# 		('person', 'человек'),
# 		('bank', 'банк'),
# 		('other', 'другое')
# 	)

# 	creditor_type = models.CharField(max_length=20, choices=CREDITOR_TYPE_CHOICES, default='person')

# 	def get_remaining_amount(self):
# 		from .models import Transaction
		
# 		total_paid = Transaction.objects.filter(debt=self, type_transaction='expense').aggregate(total=models.Sum('amount'))['total'] or 0

# 		if self.type_debt == 'I am owed':
# 			total_received = Transaction.objects.filter(debt=self, type_transaction='income').aggregate(total=models.Sum('amount'))['total'] or 0
# 			return total_received - total_paid
# 		else:
# 			return self.amount - total_paid

# 	def __str__(self):
# 		return self.title

# class Account(models.Model):
# 	title = models.CharField(max_length=150)
# 	user = models.ForeignKey(User, on_delete=models.CASCADE)

# 	def __str__(self):
# 		return self.title


# Интеграция инвестиций позже

# class Investment(models.Model):
# 	user = models.ForeignKey(User, on_delete=models.CASCADE)
# 	name = models.CharField(max_length=200, verbose_name='Актив')
# 	tiker = models.CharField(max_length=150, verbose_name='Тикер', blank=True)
# 	quantity = models.PositiveIntegerField(verbose_name='Количество в шт', null=True, blank=True, default=0)
# 	TYPE_INVEST = {
# 		('stock', 'акция'),
# 		('bonds', 'облигация'),
# 		('ETF', 'БПИФ'),
# 		('currency', 'валюта')
# 	}
# 	average_price = models.DecimalField(max_digits= 5, decimal_places=4)

# 	def __str__(self):
# 		return self.title

# class InvestTransaction()
