from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Question(models.Model):
    TEXT = 'T'
    MULTIPLE_CHOICE = 'M'
    QUESTION_TYPES = [
        (TEXT, 'Text'),
        (MULTIPLE_CHOICE, 'Multiple Choice'),
    ]

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    text = models.TextField()
    question_type = models.CharField(max_length=1, choices=QUESTION_TYPES, default=TEXT)

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
