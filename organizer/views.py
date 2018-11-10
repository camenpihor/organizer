from django.shortcuts import render

from organizer import view_utilities

CORE_OBJECT_TYPES = ['questions', 'books', 'facts', 'words', 'topics']


def home(request, core_object_type='questions'):
    view_utilities.check_core_object_match(core_object_type)

    context = {'core_object_type': core_object_type.capitalize(), 'page_name': 'Home'}
    return render(request, 'home.html', context=context)


def archive(request, core_object_type):
    view_utilities.check_core_object_match(core_object_type)

    context = {'core_object_type': core_object_type.capitalize(), 'page_name': 'Archive'}
    return render(request, 'archive.html', context=context)


def stats(request, core_object_type):
    view_utilities.check_core_object_match(core_object_type)

    context = {'core_object_type': core_object_type.capitalize(), 'page_name': 'Stats'}
    return render(request, 'stats.html', context=context)


def item(request, core_object_type, object_id):
    view_utilities.check_core_object_match(core_object_type)

    context = {'core_object_type': core_object_type.capitalize(), 'page_name': 'Item'}
    return render(request, 'item.html', context=context)
