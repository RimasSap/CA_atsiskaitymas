from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('price_chart/', views.price_chart, name='price_chart'),
    # path('calculate_profit/', views.calculate_profit, name='calculate_profit'),
]