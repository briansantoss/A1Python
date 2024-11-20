from django.urls import path
from datapanel import views

urlpatterns = [
    path('', views.data_panel, name='data_panel')  # Chama a função de DATA de views.py/data_panel
]
