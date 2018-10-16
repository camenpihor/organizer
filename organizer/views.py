from django.shortcuts import get_object_or_404, redirect, render
from django.forms import formset_factory
import numpy as np

from organizer import models
from organizer import forms


def home(request):
    context = {'page_name': 'Home'}
    all_questions = models.Question.objects.all()
    if all_questions:
        context['questions'] = np.random.choice(all_questions, size=5, replace=False)
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
    ResourceFormSet = formset_factory(forms.ResourceForm, extra=0, min_num=0, can_delete=True)
    RandomFormSet = formset_factory(forms.RandomForm, extra=0, min_num=0, can_delete=True)
    ThoughtFormSet = formset_factory(forms.ThoughtForm, extra=0, min_num=0, can_delete=True)
    AnswerFormSet = formset_factory(forms.AnswerForm, extra=0, min_num=0, can_delete=True)

    if request.method == 'POST':
        question_form = forms.QuestionForm(request.POST)
        resource_formset = ResourceFormSet(request.POST, prefix='resource')
        random_formset = RandomFormSet(request.POST, prefix='random')
        thought_formset = ThoughtFormSet(request.POST, prefix='thought')
        answer_formset = AnswerFormSet(request.POST, prefix='answer')

        if question_form.is_valid() and resource_formset.is_valid() and random_formset.is_valid() and \
                thought_formset.is_valid() and answer_formset.is_valid():

            question = question_form.save()

            for resource_form in resource_formset:
                resource = resource_form.save(commit=False)
                resource.question = question
                resource.save()

            for random_form in random_formset:
                random = random_form.save(commit=False)
                random.question = question
                random.save()

            for thought_form in thought_formset:
                thought = thought_form.save(commit=False)
                thought.question = question
                thought.save()

            for answer_form in answer_formset:
                answer = answer_form.save(commit=False)
                answer.question = question
                answer.save()

            return redirect('question', question_id=question.id)

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
