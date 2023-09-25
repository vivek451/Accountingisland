from django.urls import path
from . import views

urlpatterns = [
    # Application urls
    # path('', views.DashboardView.as_view(), name='dashboard'),
    path('',views.AddTransactionView.as_view(), name='dashboard'),

    path('transactions/list/', views.TransactionListView.as_view(), name='transaction_list'),

    path('transactions/add', views.AddTransactionView.as_view(), name='add_transaction'),

    # path('transactions/profit-loss/', views.ProfitLossView.as_view(), name='profit_loss'),

    path('transactions/calculate_profit_loss/', views.calculate_profit_loss_function, name='calculate_profit_loss'),

    path('transactions/get_balance_sheet/', views.get_balance_sheet, name='get_balance_sheet'),

    path('transactions/balance-sheet/', views.BalanceSheetView.as_view(), name='balance-sheet'),

    path('transactions/cashflow/', views.CashflowView.as_view(), name='cashflow'),

    path('transactions/cash_flow_data/', views.get_cash_flow, name='get_cashflow_data'),

    path('reset_transactions/', views.reset_transactions, name='reset_transactions'),
]
