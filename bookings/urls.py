from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_bookings, name='bookings'),
    path('book_table/', views.book_table, name='book_table'),
    path("edit/<int:booking_id>/", views.edit_booking, name="edit_booking"),
    path(
        'delete/<int:booking_id>/',
        views.delete_booking,
        name='delete_booking',
    ),
]
