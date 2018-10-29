from django import forms

from organizer import models


class QuestionForm(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = model.get_form_fields()


class ResourceForm(forms.ModelForm):
    class Meta:
        model = models.Resource
        fields = model.get_form_fields()


class ThoughtForm(forms.ModelForm):
    class Meta:
        model = models.Thought
        fields = model.get_form_fields()


class AnswerForm(forms.ModelForm):
    class Meta:
        model = models.Answer
        fields = model.get_form_fields()
