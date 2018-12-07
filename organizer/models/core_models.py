"""Models of the organizer's core objects.

"""

from datetime import datetime

from django.contrib.postgres import fields
from django.db import models
import pytz


class CoreObject(models.Model):
    created_at_utc = models.DateTimeField(auto_now_add=True)
    updated_at_utc = models.DateTimeField(blank=True)
    attributed_to = models.TextField(blank=True, null=True)
    num_views = models.PositiveIntegerField(default=0)
    rating = models.PositiveIntegerField(default=0)

    # Example: `Question.book_set.all()` or `Question.objects.filter(book_instance="x")`
    questions = models.ManyToManyField("Question", related_query_name="question_instance")
    books = models.ManyToManyField("Book", related_query_name="book_instance")
    topics = models.ManyToManyField("Topic", related_query_name="topic_instance")
    facts = models.ManyToManyField("Fact", related_query_name="fact_instance")
    words = models.ManyToManyField("Word", related_query_name="word_instance")

    def save(self, *args, **kwargs):
        self.updated_at_utc = datetime.now(tz=pytz.timezone("UTC"))
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class Question(CoreObject):
    question = models.TextField()
    questions = None

    class Meta(CoreObject.Meta):
        db_table = "core_questions"


class Book(CoreObject):
    author = models.TextField()
    title = models.TextField()
    url = models.URLField(null=True, blank=True)
    status = models.TextField(
        default="to_read",
        choices=(
            ("to_read", "To Read"),
            ("finished", "Finished"),
            ("currently_reading", "Currently Reading"),
            ("stopped", "Stopped"),
        ),
    )
    books = None

    class Meta(CoreObject.Meta):
        db_table = "core_books"


class Topic(CoreObject):
    topic = models.TextField()
    topics = None

    class Meta(CoreObject.Meta):
        db_table = "core_topics"


class Word(CoreObject):
    word = models.TextField()
    definition = models.TextField()
    examples = fields.ArrayField(
        base_field=models.TextField(blank=True, null=True), blank=True, null=True
    )
    words = None

    class Meta(CoreObject.Meta):
        db_table = "core_words"


class Fact(CoreObject):
    fact = models.TextField()
    status = models.TextField(
        default="not_verified",
        choices=(
            ("not_verified", "Not Verified"),
            ("confirmed", "confirmed"),
            ("false", "False"),
        ),
    )
    facts = None

    class Meta(CoreObject.Meta):
        db_table = "core_facts"
