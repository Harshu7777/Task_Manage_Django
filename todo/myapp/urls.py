from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index , name="indexfile"),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.create_task, name='create_task'),
    path('tasks/edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('tasks/delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('register/', views.register , name='register'),
]