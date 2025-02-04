from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_bookings(request):
    """Displays the bookings page with a booking form."""
    return render(request, 'bookings/bookings.html')


def menus_view(request):
    """Displays a simple placeholder for the menus page."""
    return HttpResponse("<h1>Menus Page</h1>")