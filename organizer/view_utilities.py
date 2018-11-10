from django.http import Http404

from organizer import views


def check_core_object_match(observed_type):
    if observed_type not in views.CORE_OBJECT_TYPES:
        raise Http404
