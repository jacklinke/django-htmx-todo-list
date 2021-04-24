from django.contrib import admin
from tasker.tasks.models import Task, TaskList

# Register your models here.
admin.site.register(TaskList)
admin.site.register(Task)
