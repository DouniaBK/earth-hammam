from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_items, name='items'),
    path('treatments', views.all_treatments, name='treatments'),
    path('tickets', views.all_tickets, name='tickets'),
]