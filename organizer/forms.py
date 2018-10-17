from django import forms

from organizer.models import Question, Resource, Random, Thought, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'placeholder': 'What is your question?',
                'autofocus': 'autofocus',
                'class': 'form-textarea'
            })
        }


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'url', 'image', 'other', 'notes']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form-input form-item'}),
            'url': forms.URLInput(attrs={'placeholder': 'URL', 'class': 'form-input form-item'}),
            'image': forms.FileInput(attrs={'accept': 'image/*', 'class': 'form-button form-item'}),
            'other': forms.Textarea(attrs={'placeholder': 'Other', 'class': 'form-textarea form-item'}),
            'notes': forms.Textarea(attrs={'placeholder': 'Notes', 'class': 'form-textarea form-item'})
        }


class RandomForm(forms.ModelForm):
    class Meta:
        model = Random
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Enter text here.'})
        }


class ThoughtForm(forms.ModelForm):
    class Meta:
        model = Thought
        fields = ['title', 'text']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'text': forms.Textarea(attrs={'placeholder': 'Enter text here.'})
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Enter text here.'})
        }
