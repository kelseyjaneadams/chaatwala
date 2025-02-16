from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from reviews.models import Review
from django.contrib import messages
from .models import Booking
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
    Handle the booking form submission.

    - GET request: Display the form.
    - POST request: Validate and save the booking.
    """
    if request.method == "POST":
        form = BookingForm(request.POST)

        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.status = Booking.STATUS_PENDING
            booking.save()

            messages.success(
                request,
                "Your booking was successful. An email confirmation will be sent to your inbox shortly."
            )
            return redirect("bookings")

        messages.error(request, "There was an error with your booking.")

    else:
        form = BookingForm()

    return render(request, "bookings/bookings.html", {"form": form})