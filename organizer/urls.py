from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('questions', views.questions, name='questions'),
    path('question/<int:question_id>/', views.question, name='question'),
    path('create', views.create, name='create'),
    path('stats', views.stats, name='stats'),
]
