from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import TodoItem

class TodoList(ListView):
    model = TodoItem
    template_name = 'tasks/todo_list.html'
    context_object_name = 'tasks'
    ordering = ['completed', 'due_date']

class TodoCreate(CreateView):
    model = TodoItem
    fields = ['title', 'description', 'due_date', 'priority']
    success_url = reverse_lazy('todo-list')
    template_name = 'tasks/todo_form.html'

class TodoUpdate(UpdateView):
    model = TodoItem
    fields = ['title', 'description', 'due_date', 'priority', 'completed']
    success_url = reverse_lazy('todo-list')
    template_name = 'tasks/todo_form.html'

class TodoDelete(DeleteView):
    model = TodoItem
    success_url = reverse_lazy('todo-list')
    template_name = 'tasks/todo_confirm_delete.html'

def toggle_complete(request, pk):
    task = get_object_or_404(TodoItem, pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect('todo-list')
