from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_bookings, name='bookings'),
    path('book_table/', views.book_table, name='book_table'),
]