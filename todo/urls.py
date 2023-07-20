from django.contrib import admin
from django.urls import path, include
from .views import taskView, deleteTask


urlpatterns = [
    path('', taskView, name="task-view"),
    path('<int:pk>', deleteTask, name="delete-task-view")
]