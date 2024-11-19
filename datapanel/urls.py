from django.urls import path
from datapanel import views

urlpatterns = [
    path('', views.datapanel, name ="datapanel")  ### Chama a função de DATA de views.py/datapanel
]