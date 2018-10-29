from django.contrib import messages
from django.shortcuts import get_object_or_404
from organizer import models


def find_section(title, sections):
    for section in sections:
        section = section.strip()
        if section.lower().startswith(title):
            return section[len(title):].strip()
    raise AssertionError(f'No section matches "{title.capitalize()}"')


def decide_form_type(form_type):
    if form_type == "resource":
        return models.Resource

    elif form_type == "thought":
        return models.Thought

    elif form_type == "answer":
        return models.Answer
    raise AssertionError(f"No form type selected")


def persist_model_object(form, question_id):
    form_type, form_text = form['form-type'], form['text-input']
    model_object = decide_form_type(form_type)
    required_inputs = model_object.get_form_fields()

    form_sections = form_text.strip().split("#")
    form_inputs = {
        form_title: find_section(form_title, form_sections) for form_title in required_inputs
    }
    if form['edit-object-id']:
        print(form['edit-object-id'])
        obj = get_object_or_404(models.Question, pk=question_id)
        print(obj)
    obj = model_object(**form_inputs)
    obj.question = models.Question.objects.get(pk=question_id)
    obj.save()
