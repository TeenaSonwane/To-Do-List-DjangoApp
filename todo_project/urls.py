# todo_project/urls.py
from django.contrib import admin
from django.urls import path, include
from todo_app.views import task_list  # Import the task_list view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('todo_app.urls')),
    path('', task_list, name='default_task_list'),  # Add this line for the default URL
]
