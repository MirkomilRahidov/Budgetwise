from modeltranslation.translator import translator, TranslationOptions
from .models import Category, Card, Income, Expense

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

class CardTranslationOptions(TranslationOptions):
    fields = ('name',)

class IncomeTranslationOptions(TranslationOptions):
    fields = ('comment',)

class ExpenseTranslationOptions(TranslationOptions):
    fields = ('comment',)

translator.register(Category, CategoryTranslationOptions)
translator.register(Card, CardTranslationOptions)
translator.register(Income, IncomeTranslationOptions)
translator.register(Expense, ExpenseTranslationOptions)
