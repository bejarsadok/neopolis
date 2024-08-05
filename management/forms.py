

from django import forms
from .models import Project, Task


# creating a form
class ProjectForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = Project

        # specify fields to be used
        fields = [
            "name",
            "description",
            "members"
        ]


class TaskForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = Task

        # specify fields to be used
        fields = [
            "title",
            "description",
            "due_date",
            "completed",
            "project",
            "assiged_to"
        ]
