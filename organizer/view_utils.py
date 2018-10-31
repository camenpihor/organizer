from django.contrib import messages
from django.shortcuts import get_object_or_404
from organizer import models


def decide_form_type(form_type):
    if form_type == "resource":
        return models.Resource

    elif form_type == "thought":
        return models.Thought

    elif form_type == "answer":
        return models.Answer
    raise AssertionError(f"No form type selected")


def persist_model_object(form, question):
    form_type, form_text = form['form-type'], form['text-input']
    model_object = decide_form_type(form_type)
    if form['edit-object-id']:
        model_object = get_object_or_404(model_object, pk=form['edit-object-id'])
    else:
        model_object = model_object()
        model_object.question = question
    model_object.save_from_form(form_text)
