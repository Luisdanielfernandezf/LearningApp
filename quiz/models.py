from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default='No description provided.')

    def __str__(self):
        return self.name

class Topic(models.Model):
    subject = models.ForeignKey(Subject, related_name='topics', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

class Question(models.Model):
    subject = models.ForeignKey(Subject, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    QUESTION_TYPE_CHOICES = [
        ('text', 'Text'),
        ('multiple_choice', 'Multiple Choice'),
    ]
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPE_CHOICES)

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
