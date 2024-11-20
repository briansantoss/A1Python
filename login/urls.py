from django.urls import path
from login import views

urlpatterns = [
    path('', views.login, name="login")  ### Chama a função de LOGIN de views.py/login
]