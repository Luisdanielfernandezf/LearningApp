from django import forms
from .models import Answer, Question
from django import forms


class MultipleChoiceAnswerForm(forms.Form):
    answer = forms.ModelChoiceField(queryset=Answer.objects.none(), widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question')
        super(MultipleChoiceAnswerForm, self).__init__(*args, **kwargs)
        self.fields['answer'].queryset = question.answers.all()

class TextAnswerForm(forms.Form):
    answer = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}), label='Your Answer', max_length=400)
