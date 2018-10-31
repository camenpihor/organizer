from django.shortcuts import get_object_or_404, render, redirect

from organizer import models, view_utils

def home(request):
    context = {'page_type': 'Question'}
    context['questions'] = models.Question.objects.all()
    return render(request, 'home.html', context)


def question(request, question_id):
    context = {
        'page_type': 'Question',
        'status_bar': True,
        'question': get_object_or_404(models.Question, pk=question_id)
    }
    if request.method == "POST":
        form = request.POST
        try:
            view_utils.persist_model_object(form, context['question'])
            return redirect('question', question_id=question_id)
        except AssertionError as e:
            context['error_message'] = str(e)
            context['form_text'] = form['text-input']
            context['form_type'] = form['form-type']
    return render(request, 'question.html', context)
