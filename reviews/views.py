from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Review
from .forms import ReviewForm


def menus_view(request):
    """
    Displays the menu page with approved reviews.
    Users also see their pending reviews.
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
    Redirects back to the menus page after submission.
    """
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.status = "pending"
            review.save()
            messages.success(
                request,
                "Thanks for your feedback! "
                "Your review is pending approval."
            )
        else:
            messages.error(request, "There was an error submitting your review.")

    return redirect("menus")


@login_required
def edit_review(request, review_id):
    """
    Allows the user to edit their submitted review.
    """
    review = get_object_or_404(Review, id=review_id, user=request.user)

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Your review has been updated successfully.")
            return redirect("profile")
    else:
        form = ReviewForm(instance=review)

    return render(
        request,
        "reviews/edit_review.html",
        {"form": form, "review": review},
    )


@login_required
def delete_review(request, review_id):
    """
    Deletes a user's review after confirmation.
    """
    review = get_object_or_404(Review, id=review_id, user=request.user)

    if request.method == "POST":
        review.delete()
        messages.success(request, "Your review has been deleted.")
        return redirect("profile")

    return redirect("profile")