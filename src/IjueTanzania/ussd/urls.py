from django.urls import path
from .views import index
app_name = "ussd"
urlpatterns = [
    path('ussd', index),
]