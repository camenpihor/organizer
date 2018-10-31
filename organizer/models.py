import markdown
from datetime import datetime
from itertools import chain
import pytz

from django.contrib import messages
from django.db import models
from django.forms.models import model_to_dict


class Base(models.Model):
    # TODO can I get a list of foreignkey objects and save them so that I can factor out the save method?
    form_attributes = list()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.form_attributes:
            raise NotImplementedError("Model needs to initialize `form_attributes`")

    def create_form(self):
        form = ""
        for title, text in model_to_dict(self, fields=self.form_attributes).items():
            form += f"# {title.capitalize()}\n\n{text}\n\n"
        return form

    @staticmethod
    def find_attribute(attribute, form_sections):
        for section in form_sections:
            section = section.strip()
            if section.lower().startswith(attribute):
                return section[len(attribute):].strip()
        raise AssertionError(f'No section matches "{attribute.capitalize()}"')

    def save_from_form(self, form):
        form_sections = form.strip().split("#")
        form_attributes = {
            attribute: self.find_attribute(attribute, form_sections) for attribute in self.form_attributes
        }
        for attribute, value in form_attributes.items():
            setattr(self, attribute, value)
        self.save()

    def get_class_name(self):
        return self.__class__.__name__.lower()

    class Meta:
        abstract = True


class Question(models.Model):
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

    def save(self, *args, **kwargs):
        self.updated_at_utc = datetime.now(tz=pytz.timezone("UTC"))  # datetime.utcnow() returns a naive datetime
        super().save(*args, **kwargs)

    class Meta:
        db_table = "questions"


class Thought(Base):
    created_at_utc = models.DateTimeField(auto_now_add=True)
    updated_at_utc = models.DateTimeField(blank=True)
    summary = models.TextField()
    thought = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    form_attributes = ['summary', 'thought']

    def save(self, *args, **kwargs):
        if self.thought and self.summary:
            self.updated_at_utc = datetime.now(tz=pytz.timezone("UTC"))
            super().save(*args, **kwargs)
            self.question.save()  # update updated_at_utc
        else:
            raise AssertionError("Summary and/or Thought field is not filled out")

    class Meta(Base.Meta):
        db_table = "thoughts"


class Answer(Base):
    # one to many with Question
    created_at_utc = models.DateTimeField(auto_now_add=True)
    updated_at_utc = models.DateTimeField(blank=True)
    summary = models.TextField()
    answer = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    form_attributes = ['summary', 'answer']

    def save(self, *args, **kwargs):
        if self.answer and self.summary:
            self.updated_at_utc = datetime.now(tz=pytz.timezone("UTC"))
            super().save(*args, **kwargs)
            self.question.save()  # update updated_at_utc
        else:
            raise AssertionError("Summary and/or Answer field is not filled out")

    class Meta(Base.Meta):
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


class Resource(Base):
    # one to many with Question;
    created_at_utc = models.DateTimeField(auto_now_add=True)
    updated_at_utc = models.DateTimeField(blank=True)
    summary = models.TextField()
    resource = models.TextField()
    notes = models.TextField(blank=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=True, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, blank=True, null=True)
    fun_fact = models.ForeignKey(FunFact, on_delete=models.CASCADE, blank=True, null=True)
    form_attributes = ['summary', 'resource', 'notes']

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

    class Meta(Base.Meta):
        db_table = "resources"
