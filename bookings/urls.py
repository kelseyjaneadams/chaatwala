from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_bookings, name='bookings'),
    path('menus/', views.menus_view, name='menus'),
]