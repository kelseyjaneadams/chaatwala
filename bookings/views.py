from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking
from .forms import BookingForm
from reviews.models import Review
from reviews.forms import ReviewForm


@login_required
def my_bookings(request):
    """
    Displays the user's bookings along with the booking form.
    """
    bookings = Booking.objects.filter(user=request.user).order_by("-booking_date")
    form = BookingForm()
    return render(
        request,
        "bookings/bookings.html",
        {"form": form, "bookings": bookings},
    )


def menus_view(request):
    """
    Displays the menu page along with approved reviews.
    Users also see their own pending reviews.
    """
    reviews = Review.objects.filter(status="approved").order_by("-created_on")

    if request.user.is_authenticated:
        user_pending_reviews = Review.objects.filter(
            user=request.user, status="pending"
        )
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
    Handles booking form submission.

    - GET request: Displays the booking form.
    - POST request: Validates and saves the booking.
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
                "Your booking was successful."
            )
            return redirect("bookings")

        messages.error(request, "There was an error with your booking.")

    else:
        form = BookingForm()

    return render(request, "bookings/bookings.html", {"form": form})


@login_required
def edit_booking(request, booking_id):
    """
    Allows the user to edit an existing booking.
    Updates the booking status to 'PENDING' upon modification.
    """
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            updated_booking = form.save(commit=False)
            updated_booking.status = "PENDING"
            updated_booking.save()
            messages.success(
                request, "Your booking has been updated and is now pending approval."
            )
            return redirect("profile")
    else:
        form = BookingForm(instance=booking)

    return render(
        request,
        "bookings/edit_booking.html",
        {"form": form, "booking": booking},
    )



@login_required
def delete_booking(request, booking_id):
    """
    Deletes a user's booking after confirmation.
    """
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == "POST":
        booking.delete()
        messages.success(request, "Your booking has been deleted.")
        return redirect("profile")

    return redirect("profile")