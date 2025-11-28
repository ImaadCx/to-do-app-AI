from django.urls import path
from .views import TodoList, TodoCreate, TodoUpdate, TodoDelete, toggle_complete

urlpatterns = [
    path('', TodoList.as_view(), name='todo-list'),
    path('add/', TodoCreate.as_view(), name='todo-add'),
    path('edit/<int:pk>/', TodoUpdate.as_view(), name='todo-edit'),
    path('delete/<int:pk>/', TodoDelete.as_view(), name='todo-delete'),
    path('toggle/<int:pk>/', toggle_complete, name='todo-toggle'),
]
