from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from .forms import ProfileImageForm
from bookings.models import Booking
from reviews.models import Review


@login_required
def profile_view(request):
    """
    Displays the profile page and allows users to update their profile picture.
    Also shows the user's bookings and reviews.
    """
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = ProfileImageForm(request.POST, request.FILES, instance=profile)

        if not request.FILES.get('image'):
            messages.error(request, "No image selected. Please choose a file.")
        elif form.is_valid():
            form.save()
            messages.success(request, "Your profile picture has been updated.")
            return redirect('profile')

    else:
        form = ProfileImageForm(instance=profile)

    bookings = Booking.objects.filter(user=request.user).order_by(
        '-booking_date'
    )
    reviews = Review.objects.filter(user=request.user).order_by('-created_on')

    return render(
        request,
        "profiles/profile.html",
        {
            "form": form,
            "profile": profile,
            "bookings": bookings,
            "reviews": reviews,
        },
    )
