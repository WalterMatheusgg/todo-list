from django import forms

from tasks.models import Task, Tag


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        required=False,
        input_formats=["%Y-%m-%dT%H:%M"],
        widget=forms.DateTimeInput(
            format="%Y-%m-%dT%H:%M",
            attrs={
                "type": "datetime-local",
                "class": "form-control",
            },
        ),
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "is_completed", "tags"]
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Descreva a tarefa...",
                }
            ),
            "is_completed": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
            "tags": forms.SelectMultiple(
                attrs={
                    "class": "form-select",
                }
            ),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Nome da tag",
                }
            ),
        }
