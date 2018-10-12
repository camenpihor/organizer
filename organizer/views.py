from django.shortcuts import get_object_or_404, render
import numpy as np

from organizer.models import Question


def home(request):
    context = {'page_name': 'Home'}
    context['questions'] = np.random.choice(Question.objects.all(), size=5, replace=False)
    return render(request, 'home.html', context)


def questions(request):
    context = {'page_name': 'Questions'}
    context['questions'] = Question.objects.all()
    return render(request, 'questions.html', context)


def stats(request):
    context = {'page_name': 'Stats'}
    return render(request, 'base.html', context)


def create(request):
    context = {'page_name': 'Create'}
    return render(request, 'base.html', context)


def question(request, question_id):
    get_object_or_404(Question, pk=question_id)
    context = {'page_name': 'Question', 'question_id': question_id}
    return render(request, 'question.html', context)
