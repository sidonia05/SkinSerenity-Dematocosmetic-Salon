from django.urls import path
from tarife import views

urlpatterns = [
    path('tarife/', views.services, name='services'),
]
