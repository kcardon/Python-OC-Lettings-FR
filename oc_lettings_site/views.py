from django.shortcuts import render
import logging

"""
This module defines the views for displaying an index page and the templates
handling 404 and 500 errors.
"""
logger = logging.getLogger(__name__)


def index(request):
    """
    View for the homepage. Renders the 'index.html' template.

    Args:
        request: The incoming HTTP request.

    Returns:
        HttpResponse object with the rendered template.
    """
    return render(request, "index.html")


def handler404(request, exception=None):
    """
    Custom handler for the 404 error (Page Not Found). Renders the '404.html' template.
    Args:
        request: The incoming HTTP request.
        exception (Optional): Exception that triggered the 404 error.
    Returns:
        HttpResponse object with the rendered template and status set to 404.
    """
    logger.warning(f"404 error: {request.path} | Exception: {exception}")
    return render(request, "404.html", status=404)


def handler500(request):
    """
    Custom handler for the 500 error (Internal Server Error). Renders the '500.html' template.
    Args:
        request: The incoming HTTP request.
    Returns:
        HttpResponse object with the rendered template and status set to 500.
    """
    logger.error("500 error encountered.")
    return render(request, "500.html", status=500)


def trigger_500_error(request):
    """This view raises an exception to trigger a 500 error for test cases."""
    raise Exception("500-error")
