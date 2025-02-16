from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from reviews.models import Review
from .forms import BookingForm
from reviews.forms import ReviewForm


@login_required
def my_bookings(request):
    """
    Displays the bookings page with a booking form.
    """
    form = BookingForm()
    return render(request, "bookings/bookings.html", {"form": form})


def menus_view(request):
    """
    Display the menus page with approved reviews.
    Users see their own pending reviews.
    """
    reviews = Review.objects.filter(status="approved").order_by("-created_on")

    if request.user.is_authenticated:
        user_pending_reviews = Review.objects.filter(user=request.user, status="pending")
        reviews = list(reviews) + list(user_pending_reviews)

    
    form = ReviewForm()

    return render(
        request,
        "bookings/menus.html",
        {"reviews": reviews, "form": form},
    )


@login_required
def book_table(request):
    """
    Handles the booking form submission.

    - GET request: Displays the form.
    - POST request: Validates and saves the booking.
    """
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.status = Booking.STATUS_PENDING
            booking.save()
            return redirect("booking_success")
    else:
        form = BookingForm()

    return render(request, "booking_form.html", {"form": form})
