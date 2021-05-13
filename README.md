# django-htmx-todo-list

Quick example of a todo list application using [Django](https://www.djangoproject.com/) and [HTMX](https://htmx.org/)

## Background

Modified & expanded from https://github.com/jaredlockhart/django-htmx-todo/

This project lets you build todo lists. It demonstrates functionality with django and HTMX, including use of modal forms, adding multiple forms to a list (an alternative to traditional django formsets), and deleting items from a list (or an entire list).

The original project used class-based Django views. That has been improved to use function-based views (see [Django Views — The Right Way](https://spookylukey.github.io/django-views-the-right-way/) to read why FBV is often the better approach!)

There are actually two example projects here which are the same in all respects except that `tasker` uses hard-coded html forms, and `tasker2` uses django forms with [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms) for formatting.

This project is very basic. It does not make use of authorization or other common important concerns. The focus is 100% on demonstrating some Django & HTMX concepts.

## Images

### Intitial Look at the app

![Intitial Look at the app](/images/0_initial_look.png)

### Adding a new TaskList

![Adding a new TaskList](/images/1_add_tasklist.png)

### The newly created TaskList

![The newly created TaskList](/images/2_new_tasklist.png)

### Adding Task instances

![Adding Task instances](/images/3_adding_tasks.png)

### Editing existing Task instances

![Editing existing Task instances](/images/4_editing_tasks.png)
