from django.shortcuts import get_object_or_404, render
from organizer import models


def home(request):
    context = {'page_type': 'Question'}
    context['questions'] = models.Question.objects.all()
    return render(request, 'home.html', context)


def question(request, question_id):
    question = get_object_or_404(models.Question, pk=question_id)
    context = {'page_type': 'Question', 'question': question, 'status_bar': True}
    return render(request, 'question.html', context)
