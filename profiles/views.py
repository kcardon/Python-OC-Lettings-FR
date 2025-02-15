from django.shortcuts import render
from .models import Profile
from django.http import Http404
import logging

# This module defines the views for displaying a list of profiles and individual profile details.

logger = logging.getLogger(__name__)


def index(request):
    """
    View to display a list of all profiles.
    Fetches all the Profile objects
    and sends them to the 'profiles/index.html' template for rendering.
    Args:
        request: The incoming HTTP request.
    Returns:
        HttpResponse object with the rendered template
        and the context containing the profiles list.
    """
    try:
        profiles_list = Profile.objects.all()
    except Exception as e:
        logger.error(f"Error retrieving profiles: {e}")
        raise

    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """
    View to display a specific profile based on the provided username.
    Fetches a Profile object based on the provided username
    and sends it to the 'profiles/profile.html' template
    for rendering.
    Args:
        request: The incoming HTTP request.
        username (str): The username of the profile to be fetched.
    Returns:
        HttpResponse object with the rendered template
        and the context containing the specific profile.
    """
    try:
        profile = Profile.objects.get(user__username=username)
    except Profile.DoesNotExist:
        logger.warning(f"Profile with username {username} doesn't exist.")
        raise Http404("Profile not found")
    except Exception as e:
        logger.error(f"Error fetching profile with username {username}: {e}")
        raise
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
