from django import forms
from main.models import Transaction, Category

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['title', 'amount', 'category', 'description', 'type_transaction']
    #     widgets = {
    #         'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название'}),
    #         'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Сумма'}),
    #         'category': forms.Select(attrs={'class': 'form-control'}),
    #         'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
    #         'type_transaction': forms.Select(attrs={'class': 'form-control'}),
    #     }

    # def __init__(self, user=None, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if user:
    #         self.fields['category'].queryset = Category.objects.filter(user=user)
    #         self.fields['category'].empty_label = 'Выберите категорию'
