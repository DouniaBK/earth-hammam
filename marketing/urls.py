from django.urls import path, include
from . import views

urlpatterns = [
    path('subscribe', views.subscribe, name='subscribe'),
    path('unsubscribe', views.unsubscribe, name='unsubscribe'),
    path("newsletter", views.newsletter, name="newsletter"),
    path('tinymce/', include('tinymce.urls')),
]
