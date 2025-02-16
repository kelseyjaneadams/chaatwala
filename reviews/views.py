from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from reviews.models import Review
from reviews.forms import ReviewForm


def menus_view(request):
    """
    Display the menus page with approved reviews.
    Users see their own pending reviews.
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
def submit_review(request):
    """
    Handles the submission of a new review.
    Redirects back to the menus page upon completion.
    """
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.status = "pending"
            review.save()
            messages.success(request, "Thanks for your feedback! Your review is pending approval.")
        else:
            messages.error(request, "There was an error submitting your review.")

    return redirect("menus")