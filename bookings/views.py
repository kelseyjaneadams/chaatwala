from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from reviews.models import Review

# Create your views here.
@login_required
def my_bookings(request):
    """Displays the bookings page with a booking form."""
    form = BookingForm()
    return render(request, 'bookings/bookings.html', {'form': form})


def menus_view(request):
    """
    Display the menus page with approved reviews.

    Retrieves reviews that are approved and orders them 
    by the most recent creation date.
    """
    reviews = (
        Review.objects.filter(status="approved")
        .order_by("-created_on")
    )

    return render(request, "bookings/menus.html", {"reviews": reviews})



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
            booking = form.save(commit=False)
            booking.user = request.user
            booking.status = Booking.STATUS_PENDING
            booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm()

    return render(request, 'booking_form.html', {'form': form})