from django.shortcuts import render
import numpy as np

from organizer.models import Question


def home(request):
    context = {'page_name': 'Home'}
    context['questions'] = np.random.choice(Question.objects.all(), size=5, replace=False)
    return render(request, 'base.html', context)


def questions(request):
    context = {'page_name': 'Questions'}
    context['questions'] = Question.objects.all()
    return render(request, 'base.html', context)
