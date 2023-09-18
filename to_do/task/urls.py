from django.urls import path
from django.urls import include
from django.contrib import admin
from . import views

urlpatterns = [
    path('createtask/', views.taskCreatView.as_view(), name='task-create'),
    path('', views.taskListView.as_view(), name='tasks-list'),
    
]
