from django.urls import path
from tasker.tasks.views import (
    tasklist_create_view,
    tasklist_add_task_view,
    tasklist_detail_view,
    tasklist_list_view,
    TaskListFilterView,
    task_create_view,
    task_edit_view,
    task_detail_view,
    task_delete_view,
)

urlpatterns = [
    path("task/<id>/create/", task_create_view, name="task-create"),
    path("task/<id>/edit/", task_edit_view, name="task-edit"),
    path("task/<id>/delete/", task_delete_view, name="task-delete"),
    path("task/<id>/", task_detail_view, name="task-detail"),
    path("filter/", TaskListFilterView.as_view(), name="tasklist-filter"),
    path("create/", tasklist_create_view, name="tasklist-create"),
    path("<slug:slug>/add_task/", tasklist_add_task_view, name="tasklist-add-task"),
    path("<slug:slug>/", tasklist_detail_view, name="tasklist-detail"),
    path("", tasklist_list_view, name="tasklist-list"),
]
