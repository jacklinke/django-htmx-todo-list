from django import forms
from django.utils.text import slugify
from tasker.tasks.models import TaskList, Task


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


class TaskCreateForm(forms.ModelForm):
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


class TaskEditForm(forms.ModelForm):
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
