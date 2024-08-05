from django.urls import path
from . import views

urlpatterns = [
    path("project/add/", views.project_create_view, name='project_create'),
    path("project/list/", views.project_list_view, name='project_list'),
    path("project/update/<id>/", views.project_update_view, name='project_update'),
    path("project/delete/<id>/", views.project_delete_view, name='project_delete'),
    path("task/add/", views.task_create_view, name='task_create'),
    path("task/list/", views.task_list_view, name='task_list'),
    path("task/update/<id>/", views.task_update_view, name='task_update'),
    path("task/delete/<id>/", views.task_delete_view, name='task_delete'),
]
