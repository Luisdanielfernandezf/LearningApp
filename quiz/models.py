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
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # Add image field

    def __str__(self):
        return self.title


class Question(models.Model):
    TEXT = 'T'
    MULTIPLE_CHOICE = 'M'
    SELF_CHECK = 'S'
    QUESTION_TYPES = [
        (TEXT, 'Text'),
        (MULTIPLE_CHOICE, 'Multiple Choice'),
        (SELF_CHECK, 'Self Check'),
    ]
    
    question_type = models.CharField(max_length=1, choices=QUESTION_TYPES)
    text = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    # other fields


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
