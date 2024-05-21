from django.contrib import admin
from .models import Subject, Question, Answer

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3  # Number of extra forms to display
    can_delete = True  # Allow deletion of answers

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'subject', 'question_type']
    list_filter = ['subject', 'question_type']
    search_fields = ['text', 'subject__name']
    list_editable = ['subject']  # Make the subject field editable
    inlines = [AnswerInline]

admin.site.register(Subject)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
