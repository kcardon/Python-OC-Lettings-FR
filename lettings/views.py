from django.shortcuts import render
from .models import Letting
from django.http import Http404

# This module defines the views for displaying a list of lettings and individual letting details.


def index(request):
    """
    View for displaying a list of all lettings.
    Retrieves all the Letting objects from the database
    and passes them to the 'lettings/index.html' template.
    Args:
        request: The incoming HTTP request.
    Returns:
        HttpResponse object with the rendered template.
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """
    View for displaying the details of a specific letting.
    Retrieves a Letting object based on the given `letting_id`
    and passes its details to the 'lettings/letting.html' template.
    Args:
        request: The incoming HTTP request.
        letting_id: ID of the Letting object to retrieve.
    Returns:
        HttpResponse object with the rendered template.
    """
    try:
        letting = Letting.objects.get(id=letting_id)

    except Letting.DoesNotExist:
        raise Http404("Letting not found")
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
