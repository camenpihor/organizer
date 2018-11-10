from datetime import datetime

from django.db import models
import pytz

from .core_models import Question, Book, Fact, Word, Topic


class SupportingObject(models.Model):
    created_at_utc = models.DateTimeField(auto_now_add=True)
    updated_at_utc = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        self.updated_at_utc = datetime.now(tz=pytz.timezone("UTC"))
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class Resource(SupportingObject):
    resource = models.TextField()
    notes = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)

    class Meta(SupportingObject.Meta):
        db_table = "supporting_resources"


class Thought(SupportingObject):
    thought = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta(SupportingObject.Meta):
        db_table = "supporting_thoughts"


class Answer(SupportingObject):
    answer = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta(SupportingObject.Meta):
        db_table = "supporting_answers"


class Review(SupportingObject):
    review = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta(SupportingObject.Meta):
        db_table = "supporting_reviews"


class Notebook(SupportingObject):
    notebook = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)

    class Meta(SupportingObject.Meta):
        db_table = "supporting_notebooks"


class Quote(SupportingObject):
    quote = models.TextField()
    location = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta(SupportingObject.Meta):
        db_table = "supporting_quotes"


class Concept(SupportingObject):
    concept = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    fact = models.ForeignKey(Fact, on_delete=models.CASCADE)

    class Meta(SupportingObject.Meta):
        db_table = "supporting_concepts"
