from django.urls import path
from file import views

urlpatterns = [
    path('', views.file, name='file')  # Chama a função de DATA de views.py/data_panel
]
