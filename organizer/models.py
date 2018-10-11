from django.db import models


class Question(models.Model):
    # Base
    created_at_utc = models.DateTimeField(auto_now_add=True)
    question = models.TextField()

    def get_resources(self):
        return Resource.objects.filter(question=self)

    class Meta:
        db_table = "questions"


class Resource(models.Model):
    # one to many with Question
    created_at_utc = models.DateTimeField(auto_now_add=True)
    resource_title = models.TextField()
    url = models.URLField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    other = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        db_table = "resources"


class Random(models.Model):
    # one to many with Question
    created_at_utc = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        db_table = "random_thoughts"


class Thought(models.Model):
    # one to many with Question
    created_at_utc = models.DateTimeField(auto_now_add=True)
    title = models.TextField()
    thought = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        db_table = "thoughts"


class Answer(models.Model):
    # one to many with Question
    created_at_utc = models.DateTimeField(auto_now_add=True)
    answer = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        db_table = "answers"
