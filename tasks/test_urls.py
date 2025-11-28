import pytest
from django.urls import reverse, resolve
from tasks.views import TodoList, TodoCreate, TodoUpdate, TodoDelete, toggle_complete


class TestUrls:
    """Test cases for URL routing"""

    def test_todo_list_url(self):
        """Test todo list URL resolves correctly"""
        url = reverse('todo-list')
        assert url == '/'
        assert resolve(url).func.view_class == TodoList

    def test_todo_add_url(self):
        """Test todo add URL resolves correctly"""
        url = reverse('todo-add')
        assert url == '/add/'
        assert resolve(url).func.view_class == TodoCreate

    def test_todo_edit_url(self):
        """Test todo edit URL resolves correctly"""
        url = reverse('todo-edit', kwargs={'pk': 1})
        assert url == '/edit/1/'
        assert resolve(url).func.view_class == TodoUpdate

    def test_todo_delete_url(self):
        """Test todo delete URL resolves correctly"""
        url = reverse('todo-delete', kwargs={'pk': 1})
        assert url == '/delete/1/'
        assert resolve(url).func.view_class == TodoDelete

    def test_todo_toggle_url(self):
        """Test todo toggle URL resolves correctly"""
        url = reverse('todo-toggle', kwargs={'pk': 1})
        assert url == '/toggle/1/'
        assert resolve(url).func == toggle_complete
