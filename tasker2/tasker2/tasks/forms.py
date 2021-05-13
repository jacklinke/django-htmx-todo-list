from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Div, Field, Layout, Row, Submit
from django import forms
from django.utils.text import slugify

from tasker2.tasks.models import Task, TaskList


class TaskListCreateForm(forms.ModelForm):
    slug = forms.CharField(required=False, widget=forms.widgets.HiddenInput())

    class Meta:
        model = TaskList
        fields = ("name", "slug")

    def clean_name(self) -> str:
        name: str = self.cleaned_data["name"]
        slug = slugify(name)
        if TaskList.objects.filter(slug=slug).exists():
            raise forms.ValidationError(f"A Task List with the name {name} exists")
        return name

    def save(self, commit: bool = True) -> TaskList:
        task_list: TaskList = super().save(commit)
        task_list.slug = slugify(task_list.name)
        task_list.save()
        return task_list

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field("name", css_class="col-sm-12", placeholder="Name"),
        )
        self.helper.form_show_labels = False


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("name", "is_done")

    def clean_name(self) -> str:
        name: str = self.cleaned_data["name"]
        if Task.objects.filter(name=name).exclude(id=self.instance.id).exists():
            raise forms.ValidationError(f"A Task with the name {name} exists")
        return name

    def save(self, commit: bool = True) -> Task:
        task: Task = super().save(commit)
        task.save()
        return task

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(Column("name", css_class="col-sm-6"), Column("is_done", css_class="col-sm-6"), css_class="col-sm-8"),
        )