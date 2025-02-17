from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    """ Displays the profile page for logged-in users. """
    return render(request, "profiles/profile.html")