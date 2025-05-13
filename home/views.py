from django.views.generic import ListView, CreateView, UpdateView, DeleteView,DetailView,View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Card, Income, Expense, Category
from .forms import CardForm, IncomeForm, ExpenseForm,CategoryForm
from django.shortcuts import redirect,render

class CardListView(LoginRequiredMixin, ListView):
    model = Card
    template_name = 'home.html'  
    context_object_name = 'cards'
    paginate_by = 10

    def get_queryset(self):
        return Card.objects.filter(user=self.request.user)

class CardCreateView(LoginRequiredMixin, CreateView):
    model = Card
    form_class = CardForm
    template_name = 'card_add.html'
    success_url = reverse_lazy('card_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class CardDetailsView(LoginRequiredMixin, DetailView):
    model = Card
    template_name = 'card_details.html'
    context_object_name = 'card'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        card = self.object
        
        incomes = Income.objects.filter(card=card)
        expenses = Expense.objects.filter(card=card)
        
        total_income = sum(income.amount for income in incomes)
        total_expense = sum(expense.amount for expense in expenses)
        
        current_balance = card.initial_balance + total_income - total_expense
        
        expense_categories = {}
        for expense in expenses:
            category = expense.category
            if category not in expense_categories:
                expense_categories[category] = 0
            expense_categories[category] += expense.amount
        
        total_expenses = sum(expense_categories.values())
        expense_categories_percentage = {}
        if total_expenses > 0:
            for category, amount in expense_categories.items():
                expense_categories_percentage[category] = (amount / total_expenses) * 100
        
        context['income'] = total_income
        context['expense'] = total_expense
        context['current_balance'] = current_balance
        context['expense_categories'] = expense_categories
        context['expense_categories_percentage'] = expense_categories_percentage
        context['income_form'] = IncomeForm()
        context['expense_form'] = ExpenseForm()
        
        return context






class CardUpdateView(LoginRequiredMixin, UpdateView):
    model = Card
    form_class = CardForm
    template_name = 'card_update.html'
    success_url = reverse_lazy('card_list')

    def get_queryset(self):
        return Card.objects.filter(user=self.request.user)

class CardDeleteView(LoginRequiredMixin, DeleteView):
    model = Card
    template_name = 'card_delete.html'
    success_url = reverse_lazy('card_list')

    def get_queryset(self):
        return Card.objects.filter(user=self.request.user)

class IncomeCreateView(LoginRequiredMixin, CreateView):
    model = Income
    form_class = IncomeForm
    template_name = 'income_create.html'
    success_url = reverse_lazy('card_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['card'].queryset = Card.objects.filter(user=self.request.user)
        form.fields['category'].queryset = Category.objects.filter(user=self.request.user, type='income')
        return form

class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'expense_create.html'
    success_url = reverse_lazy('card_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['card'].queryset = Card.objects.filter(user=self.request.user)
        form.fields['category'].queryset = Category.objects.filter(user=self.request.user, type='expense')
        return form
