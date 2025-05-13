from django import forms
from .models import Card,Income,Expense,Category

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['name', 'card_number', 'expiry_date', 'initial_balance']
        labels = {
            'name': 'Card name',
            'card_number': 'Card Number',
            'expiry_date': 'Expiration Date',
            'initial_balance': 'Initial Balance',
        }
        widgets = {
            'card_number': forms.TextInput(attrs={
                'placeholder': 'XXXX-XXXX-XXXX-XXXX',
                'id': 'id_card_number',
                'maxlength': '19'
            }),
            'expiration_date': forms.DateInput(attrs={
                'type': 'date'
            }),
        }


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['card', 'category', 'amount', 'comment']
        labels = {
            'card': 'Card',
            'category': 'Category',
            'amount': 'Amount',
            'comment': 'Comment',
        }

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['card', 'category', 'amount', 'comment']
        labels = {
            'card': 'Card',
            'category': 'Category',
            'amount': 'Amount',
            'comment': 'Comment',
        }
        category = forms.CharField(max_length=255, required=True)
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'type']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-select'}),
        }
