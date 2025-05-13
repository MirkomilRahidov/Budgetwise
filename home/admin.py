from django.contrib import admin
from .models import Category, Card, Income, Expense
from django.contrib.auth.models import User

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'user')
    list_filter = ('type', 'user')
    search_fields = ['name']

class CardAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'initial_balance', 'created_at')
    list_filter = ('user',)
    search_fields = ['name', 'user__username']
    
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('card', 'amount', 'category', 'comment', 'date', 'user')
    list_filter = ('category', 'card', 'user')
    search_fields = ['card__name', 'category__name', 'user__username']
    
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('card', 'amount', 'category', 'comment', 'date', 'user')
    list_filter = ('category', 'card', 'user')
    search_fields = ['card__name', 'category__name', 'user__username']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Income, IncomeAdmin)
admin.site.register(Expense, ExpenseAdmin)
