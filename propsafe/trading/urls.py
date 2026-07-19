from django.urls import path
from . import views

app_name = "trading"

urlpatterns = [
    path('dashboard/', views.dashboard, name="prop_dashboard"),
    path('new_trade/', views.new_trade, name="new_trade"),
    path('trades/', views.trades, name="trades")
]