import random
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Subject, Question, Answer, Topic
from .forms import TextAnswerForm, MultipleChoiceAnswerForm

def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'quiz/subject_list.html', {'subjects': subjects})

def question_list(request, subject_id):
    print("question_list view called with subject_id:", subject_id)  # Debug line
    subject = get_object_or_404(Subject, pk=subject_id)
    subjects = Subject.objects.all()
    questions = list(Question.objects.filter(subject=subject))
    random.shuffle(questions)  # Shuffle questions
    forms = []
    results = {}

    print("Questions fetched:", questions)  # Debug line

    # Handle AJAX POST request
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        for question in questions:
            question_id = str(question.id)
            if question.question_type == Question.TEXT:
                form = TextAnswerForm(request.POST, prefix=question_id)
                if form.is_valid():
                    user_answer = form.cleaned_data['answer']
                    correct = any(answer.text.lower() == user_answer.lower() and answer.is_correct for answer in question.answers.all())
                    results[question_id] = {
                        'result': 'correct' if correct else 'incorrect',
                        'text': question.text
                    }
            elif question.question_type == Question.MULTIPLE_CHOICE:
                form = MultipleChoiceAnswerForm(request.POST, question=question, prefix=question_id)
                if form.is_valid():
                    selected_answer = form.cleaned_data['answer']
                    results[question_id] = {
                        'result': 'correct' if selected_answer.is_correct else 'incorrect',
                        'text': question.text
                    }
            elif question.question_type == Question.SELF_CHECK:
                results[question_id] = {
                    'result': 'self-check',
                    'text': question.text
                }
        return JsonResponse(results)

    # Prepare forms for GET request
    for question in questions:
        if question.question_type == 'T':  # Text
            form = TextAnswerForm(prefix=str(question.id))
            print(f"Created TextAnswerForm for question: {question.text}")  # Debug line
        elif question.question_type == 'M':  # Multiple Choice
            form = MultipleChoiceAnswerForm(question=question, prefix=str(question.id))
            print(f"Created MultipleChoiceAnswerForm for question: {question.text}")  # Debug line
        elif question.question_type == 'S':  # Self Check
            form = None  # You might want to handle this if needed
            print(f"Self Check type question found: {question.text}")  # Debug line
        else:
            form = None  # Ensure form is not None for unsupported types
            print(f"Question type not handled: {question.question_type} for question: {question.text}")  # Debug line
        if form:
            forms.append((question, form))
            print("Form appended for question:", question.text)  # Debug line

    print("Forms prepared:", forms)  # Debug line

    return render(request, 'quiz/question_list.html', {'subject': subject, 'subjects': subjects, 'forms': forms, 'results': results})

def topic_list(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    topics = Topic.objects.filter(subject=subject)
    return render(request, 'quiz/topic_list.html', {'subject': subject, 'topics': topics})

def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    return render(request, 'quiz/topic_detail.html', {'topic': topic})