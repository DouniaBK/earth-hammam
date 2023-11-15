from django.urls import path
from . import views


urlpatterns = [
    path('', views.booking, name='booking'),
    path('cancel_session', views.cancel_session, name="cancel_session"),
]