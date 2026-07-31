from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .models import Transaction, User, Category
from django import forms
from datetime import datetime

class CustomUserCreationForm(UserCreationForm):
	email = forms.EmailField(
		required=True,
		label='Электронная почта',
		widget=forms.EmailInput(attrs={
			'class': 'form-control',
			'placeholder': 'your@email.com'
		})
	)
	username = forms.CharField(
		required=True,
		max_length=100,
		label='Логин',
		widget=forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Ваш логин'
		})
	)
	first_name = forms.CharField(
		required=False,
		label='Имя',
		widget=forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Ваше имя'
		})
	)

	last_name = forms.CharField(
		required=False,
		label='Фамилия',
		widget=forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Ваша фамилия'
		})
	)

	password1 = forms.CharField(
		required=True,
		max_length=100,
		label='Пароль',
		widget=forms.PasswordInput(attrs={
			'class': 'form-control',
			'placeholder': 'Придумайте пароль',
			'autocomplete': 'new-password'
		}),
		help_text='Пароль должен содержать минимум 8 символов, включая буквы и цифры'
	)
	password2 = forms.CharField(
		required=True,
		max_length=100,
		label='Пароль',
		widget=forms.PasswordInput(attrs={
			'class': 'form-control',
			'placeholder': 'Повторите пароль',
			'autocomplete': 'new-password'
		}),
		
	)

	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

# class TransactionForm(forms.ModelForm):
# 	class Meta:
# 		model = Transaction
# 		fields = ['title', 'amount', 'category', 'description', 'type_transaction']
# 		widgets = {
# 			'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
# 			'description': forms.Textarea(attrs={'rows': 3}),
# 		}

# 	def __init__(self, user=None, *args, **kwargs):
# 		super().__init__(*args, **kwargs)
# 		if user:
# 			self.fields['category'].queryset = Category.objects.filter(user=user)


