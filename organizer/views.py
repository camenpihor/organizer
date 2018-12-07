"""Backend for pages of the website.

The website is organized into five (5) core objects:
1. Questions
2. Books
3. Facts
4. Words
5. Topics

Each core object has four (4) pages:
1. Home
2. Archive
3. Stats
4. Item

This module contains the backends for the four (4) pages of the five (5) core objects,
which have been factored to contain similar information so that the pages of the core
objects can be served by the same functions.
"""

from django.http import Http404
from django.shortcuts import render

CORE_OBJECT_TYPES = ["questions", "books", "facts", "words", "topics"]


def check_core_object_type(core_object_type):
    """Validates the core object type.

    Parameters
    ----------
    core_object_type : str
        Type of core object for the request. Must be one of `CORE_OBJECT_TYPES`.

    Raises
    ------
    Http404
        If the `core_object_type` is not in `CORE_OBJECT_TYPES`.

    """
    if core_object_type not in CORE_OBJECT_TYPES:
        raise Http404


def home(request, core_object_type="questions"):
    """The home page of the website.

    Parameters
    ----------
    request : HttpRequest
        Metadata about the request.
    core_object_type : str, optional
        Type of core object for the request, must be one of `CORE_OBJECT_TYPES` (the
        default is `"questions"`, which is considered the primary core object).

    Returns
    -------
    HttpResponse
        Content is from `template_name`, and context is from `context`.

    """
    check_core_object_type(core_object_type)

    context = {"core_object_type": core_object_type.capitalize(), "page_name": "Home"}
    return render(request, template_name="home.html", context=context)


def archive(request, core_object_type):
    """A list of all historical content.

    Parameters
    ----------
    request : HttpRequest
        Metadata about the request.
    core_object_type : str, optional
        Type of core object for the request, must be one of `CORE_OBJECT_TYPES`.

    Returns
    -------
    HttpResponse
        Content is from `template_name`, and context is from `context`.

    """
    check_core_object_type(core_object_type)

    context = {"core_object_type": core_object_type.capitalize(), "page_name": "Archive"}
    return render(request, template_name="archive.html", context=context)


def stats(request, core_object_type):
    """Useful statatistics about usage.

    Parameters
    ----------
    request : HttpRequest
        Metadata about the request.
    core_object_type : str, optional
        Type of core object for the request, must be one of `CORE_OBJECT_TYPES`.

    Returns
    -------
    HttpResponse
        Content is from `template_name`, and context is from `context`.

    """
    check_core_object_type(core_object_type)

    context = {"core_object_type": core_object_type.capitalize(), "page_name": "Stats"}
    return render(request, template_name="stats.html", context=context)


def item(request, core_object_type, object_id):
    """Read and edit information about a core object.

    Parameters
    ----------
    request : HttpRequest
        Metadata about the request.
    core_object_type : str, optional
        Type of core object for the request, must be one of `CORE_OBJECT_TYPES`.
    object_id : int
        ID of ther corresponding core object.

    Returns
    -------
    HttpResponse
        Content is from `template_name`, and context is from `context`.

    """
    check_core_object_type(core_object_type)

    object_id = object_id

    context = {"core_object_type": core_object_type.capitalize(), "page_name": "Item"}
    return render(request, template_name="item.html", context=context)
