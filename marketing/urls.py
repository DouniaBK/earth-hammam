from django.urls import path, include
from . import views

urlpatterns = [
    path('subscribe', views.subscribe, name='subscribe'),
    path("newsletter", views.newsletter, name="newsletter"),
    path('tinymce/', include('tinymce.urls')),
]
