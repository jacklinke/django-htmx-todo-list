from django.contrib import admin

from tasker2.tasks.models import Task, TaskList


@admin.register(TaskList)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "slug"]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "is_done"]
