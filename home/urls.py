from django.urls import path
from .views import CardListView, CardCreateView, CardUpdateView, CardDeleteView,IncomeCreateView, ExpenseCreateView,CardDetailsView
    

urlpatterns = [
    path('', CardListView.as_view(), name='card_list'),
    path('card/create/', CardCreateView.as_view(), name='card_create'),
    path('card/edit/<int:pk>/', CardUpdateView.as_view(), name='card_edit'),
    path('card/delete/<int:pk>/', CardDeleteView.as_view(), name='card_delete'),
    path('income/add/', IncomeCreateView.as_view(), name='income_add'),
    path('expense/add/', ExpenseCreateView.as_view(), name='expense_add'),
    path('card/details/<int:pk>/',CardDetailsView.as_view(), name='card_details')
]
