from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_items, name='item'),
    path('<item_id>', views.item_detail, name='item_detail'),
]