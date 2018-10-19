from itertools import chain

from django.db import models


class Question(models.Model):
    # Base
    created_at_utc = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def count_attached_resources(self):
        return self.resource_set.count() + self.random_set.count() + self.thought_set.count() + self.answer_set.count()

    def get_all_connected_objects(self):
        return sorted(
            chain(self.resource_set.all(),
                  self.random_set.all(),
                  self.thought_set.all(),
                  self.answer_set.all()),
            key=lambda obj: obj.created_at_utc
        )

    class Meta:
        db_table = "questions"


class Resource(models.Model):
    # one to many with Questionp;
    created_at_utc = models.DateTimeField(auto_now_add=True)
    title = models.TextField()
    url = models.URLField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    other = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.title and (self.url or self.image or self.other):
            super().save(*args, **kwargs)
        return None

    @staticmethod
    def get_class_name():
        return "resource"

    class Meta:
        db_table = "resources"


class Random(models.Model):
    # one to many with Question
    created_at_utc = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.text:
            super().save(*args, **kwargs)
        return False

    @staticmethod
    def get_class_name():
        return "random"

    class Meta:
        db_table = "random_thoughts"


class Thought(models.Model):
    # one to many with Question
    created_at_utc = models.DateTimeField(auto_now_add=True)
    title = models.TextField()
    text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.title:
            super().save(*args, **kwargs)
        return False

    @staticmethod
    def get_class_name():
        return "thought"

    class Meta:
        db_table = "thoughts"


class Answer(models.Model):
    # one to many with Question
    created_at_utc = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.text:
            super().save(*args, **kwargs)
        return False

    @staticmethod
    def get_class_name():
        return "answer"

    class Meta:
        db_table = "answers"
