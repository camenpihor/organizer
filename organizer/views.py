from django.shortcuts import get_object_or_404, render
from django.forms import formset_factory
import numpy as np

from organizer import models
from organizer import forms


def home(request):
    context = {'page_name': 'Home'}
    context['questions'] = np.random.choice(models.Question.objects.all(), size=5, replace=False)
    return render(request, 'home.html', context)


def questions(request):
    context = {'page_name': 'Questions'}
    context['questions'] = models.Question.objects.all()
    return render(request, 'questions.html', context)


def stats(request):
    context = {'page_name': 'Stats'}
    return render(request, 'base.html', context)


def create(request):
    context = {'page_name': 'Create'}
    ResourceFormSet = formset_factory(forms.ResourceForm, extra=0, min_num=0)
    RandomFormSet = formset_factory(forms.RandomForm, extra=0, min_num=0)
    ThoughtFormSet = formset_factory(forms.ThoughtForm, extra=0, min_num=0)
    AnswerFormSet = formset_factory(forms.AnswerForm, extra=0, min_num=0)

    if request.method == 'POST':
        question_form = forms.QuestionForm(request.POST)
        resource_formset = ResourceFormSet(request.POST, prefix='resource')
        random_formset = RandomFormSet(request.POST, prefix='random')
        thought_formset = ThoughtFormSet(request.POST, prefix='thought')
        answer_formset = AnswerFormSet(request.POST, prefix='answer')

    else:
        question_form = forms.QuestionForm()
        resource_formset = ResourceFormSet(prefix='resource')
        random_formset = RandomFormSet(prefix='random')
        thought_formset = ThoughtFormSet(prefix='thought')
        answer_formset = AnswerFormSet(prefix='answer')

    context['question_form'] = question_form
    context['resource_formset'] = resource_formset
    context['random_formset'] = random_formset
    context['thought_formset'] = thought_formset
    context['answer_formset'] = answer_formset
    return render(request, 'create.html', context)


def question(request, question_id):
    question = get_object_or_404(models.Question, pk=question_id)
    context = {'page_name': 'Question', 'question': question}
    return render(request, 'question.html', context)
