from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BookingForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def my_bookings(request):
    """Displays the bookings page with a booking form."""
    form = BookingForm()
    return render(request, 'bookings/bookings.html', {'form': form})


def menus_view(request):
    """Displays a simple placeholder for the menus page."""
    return HttpResponse("<h1>Menus Page</h1>")


@login_required
def book_table(request):
    """
    Handles the booking form submission.
    - GET request: Displays the form.
    - POST request: Validates and saves the booking.
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)  # Don't save yet
            booking.user = request.user  # Assign logged-in user
            booking.status = Booking.STATUS_PENDING  # Default status
            booking.save()
            return redirect('booking_success')  # Redirect after success
    else:
        form = BookingForm()

    return render(request, 'booking_form.html', {'form': form})