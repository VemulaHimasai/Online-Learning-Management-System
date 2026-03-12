from django import forms
from .models import Submission, Assignment

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['file']

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'file', 'deadline']