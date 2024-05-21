import random
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Subject, Question, Answer
from .forms import TextAnswerForm, MultipleChoiceAnswerForm

def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'quiz/subject_list.html', {'subjects': subjects})

def question_list(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    subjects = Subject.objects.all()
    questions = list(Question.objects.filter(subject=subject))
    random.shuffle(questions)
    forms = []
    results = {}

    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        for question in questions:
            question_id = str(question.id)
            if question.question_type == Question.TEXT:
                form = TextAnswerForm(request.POST, prefix=question_id)
                if form.is_valid():
                    user_answer = form.cleaned_data['answer']
                    results[question_id] = {
                        'result': 'self-check',
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
        return JsonResponse({'results': results})

    for question in questions:
        if question.question_type == Question.TEXT:
            form = TextAnswerForm(prefix=str(question.id))
        elif question.question_type == Question.MULTIPLE_CHOICE:
            form = MultipleChoiceAnswerForm(question=question, prefix=str(question.id))
        forms.append((question, form))

    return render(request, 'quiz/question_list.html', {'subject': subject, 'subjects': subjects, 'forms': forms, 'results': results})
