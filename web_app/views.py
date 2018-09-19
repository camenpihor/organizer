from django.shortcuts import render

from web_app.models import Question, Resource, Random, Thought, Answer


def home(request):
    context = {'page_name': 'Home'}
    context['questions'] = Question.objects.all()
    context['resources'] = Resource.objects.all()
    context['random_thoughts'] = Random.objects.all()
    context['thoughts'] = Thought.objects.all()
    context['answers'] = Answer.objects.all()
    return render(request, 'base.html', context)
