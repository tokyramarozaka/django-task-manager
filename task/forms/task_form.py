from django import forms
from task.models import Task

class TaskForm(forms.ModelForm):
    """Form definition for Task."""

    class Meta:
        """Meta definition for Taskform."""

        model = Task
        fields = ('task_title','task_description', 'deadline', 'category')
