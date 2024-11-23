from django.urls import path
from graphic import views

urlpatterns = [
    path('', views.graphic, name='graphic')
]
