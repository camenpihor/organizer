import markdown
from datetime import datetime
from itertools import chain
import pytz

from django.contrib import messages
from django.db import models


class Question(models.Model):
    # Base
    created_at_utc = models.DateTimeField(auto_now_add=True)
    updated_at_utc = models.DateTimeField(blank=True)
    author = models.TextField()
    question = models.TextField()
    num_views = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)

    def count_attached_resources(self):
        return self.resource_set.count() + self.thought_set.count() + self.answer_set.count()

    def get_all_connected_objects(self):
        return sorted(
            chain(self.resource_set.all(),
                  self.thought_set.all(),
                  self.answer_set.all()),
            key=lambda obj: obj.created_at_utc
        )

    @staticmethod
    def get_form_fields():
        return ['author', 'question', 'rating']

    def save(self, *args, **kwargs):
        self.updated_at_utc = datetime.now(tz=pytz.timezone("UTC"))  # datetime.utcnow() returns a naive datetime
        super().save(*args, **kwargs)

    class Meta:
        db_table = "questions"


class Thought(models.Model):
    # one to many with Question
    created_at_utc = models.DateTimeField(auto_now_add=True)
    updated_at_utc = models.DateTimeField(blank=True)
    summary = models.TextField()
    thought = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.thought and self.summary:
            self.updated_at_utc = datetime.now(tz=pytz.timezone("UTC"))
            super().save(*args, **kwargs)
            self.question.save()  # update updated_at_utc
        else:
            raise AssertionError("Summary and/or Thought field is not filled out")

    @staticmethod
    def get_class_name():
        return "thought"

    @staticmethod
    def get_form_fields():
        return ['summary', 'thought']

    class Meta:
        db_table = "thoughts"


class Answer(models.Model):
    # one to many with Question
    created_at_utc = models.DateTimeField(auto_now_add=True)
    updated_at_utc = models.DateTimeField(blank=True)
    summary = models.TextField()
    answer = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.answer and self.summary:
            self.updated_at_utc = datetime.now(tz=pytz.timezone("UTC"))
            super().save(*args, **kwargs)
            self.question.save()  # update updated_at_utc
        else:
            raise AssertionError("Summary and/or Answer field is not filled out")

    @staticmethod
    def get_class_name():
        return "answer"

    @staticmethod
    def get_form_fields():
        return ['summary', 'answer']

    class Meta:
        db_table = "answers"


class Book(models.Model):
    created_at_utc = models.DateTimeField(auto_now_add=True)
    updated_at_utc = models.DateTimeField(blank=True)
    author = models.TextField()
    title = models.TextField()
    url = models.URLField(blank=True, null=True)
    read_status = models.TextField(choices=[('to_read', 'To Read'), ('read', 'Read'), ('reading', 'Reading')])
    rating = models.IntegerField(default=0)
    num_views = models.IntegerField(default=0)
    review = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.updated_at_utc = datetime.now(tz=pytz.timezone("UTC"))
        super().save(*args, **kwargs)

    class Meta:
        db_table = "books"


class BookReview(models.Model):
    created_at_utc = models.DateTimeField(auto_now_add=True)
    updated_at_utc = models.DateTimeField(blank=True)
    review = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.review:
            self.updated_at_utc = datetime.now(tz=pytz.timezone("UTC"))
            super().save(*args, **kwargs)
            self.book.save()  # update updated_at_utc

    class Meta:
        db_table = "book_reviews"


class FunFact(models.Model):
    created_at_utc = models.DateTimeField(auto_now_add=True)
    updated_at_utc = models.DateTimeField(blank=True)
    veracity_status = models.BooleanField(default=True)
    fact = models.TextField()
    justification = models.TextField(null=True, blank=True)
    rating = models.IntegerField(default=0)
    num_views = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.fact:
            self.updated_at_utc = datetime.now(tz=pytz.timezone("UTC"))
            super().save(*args, **kwargs)

    class Meta:
        db_table = "fun_facts"


class Topic(models.Model):
    created_at_utc = models.DateTimeField(auto_now_add=True)
    updated_at_utc = models.DateTimeField(blank=True)
    topic = models.TextField()
    review = models.TextField(blank=True, null=True)
    num_views = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.topic:
            self.updated_at_utc = datetime.now(tz=pytz.timezone("UTC"))
            super().save(*args, **kwargs)

    class Meta:
        db_table = "topics"


class TopicExplanation(models.Model):
    created_at_utc = models.DateTimeField(auto_now_add=True)
    updated_at_utc = models.DateTimeField()
    explanation = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.explanation:
            self.updated_at_utc = datetime.now(tz=pytz.timezone("UTC"))
            super().save(*args, **kwargs)
            self.topic.save()  # update updated_at_utc

    class Meta:
        db_table = "topic_explanation"


class Resource(models.Model):
    # one to many with Question;
    created_at_utc = models.DateTimeField(auto_now_add=True)
    updated_at_utc = models.DateTimeField(blank=True)
    summary = models.TextField()
    resource = models.TextField()
    notes = models.TextField(blank=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=True, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, blank=True, null=True)
    fun_fact = models.ForeignKey(FunFact, on_delete=models.CASCADE, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.summary and self.resource:
            self.updated_at_utc = datetime.now(tz=pytz.timezone("UTC"))
            super().save(*args, **kwargs)
            if self.question:
                self.question.save()  # update updated_at_utc
            if self.topic:
                self.topic.save()  # update updated_at_utc
            if self.fun_fact:
                self.fun_fact.save()  # update updated_at_utc
        else:
            raise AssertionError("Summary and/or Resource field is not filled out")

    @staticmethod
    def get_class_name():
        return "resource"

    @staticmethod
    def get_form_fields():
        return ['summary', 'resource', 'notes']

    class Meta:
        db_table = "resources"
