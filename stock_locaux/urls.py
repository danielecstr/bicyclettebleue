from django.urls import path, include
from . import views

app_name='stock_locaux'

urlpatterns = [
    path('', views.stock_locaux, name='indexStockLocaux'),
]
