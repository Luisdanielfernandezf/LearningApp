# models.py
from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=200)

class Theory(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='theories')
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

class Question(models.Model):
    TEXT = 'text'
    MULTIPLE_CHOICE = 'mc'
    QUESTION_TYPES = [
        (TEXT, 'Text'),
        (MULTIPLE_CHOICE, 'Multiple Choice'),
    ]
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=200)
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES)

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Topic(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='topics')

    def __str__(self):
        return self.title