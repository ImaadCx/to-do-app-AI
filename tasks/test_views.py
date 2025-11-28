import pytest
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from tasks.models import TodoItem


@pytest.mark.django_db
class TestTodoViews:
    """Test cases for Todo views"""

    def test_todo_list_view_empty(self, client):
        """Test todo list view with no items"""
        url = reverse('todo-list')
        response = client.get(url)
        assert response.status_code == 200
        assert 'tasks' in response.context
        assert len(response.context['tasks']) == 0

    def test_todo_list_view_with_items(self, client):
        """Test todo list view with multiple items"""
        TodoItem.objects.create(title="Task 1", priority="HIGH")
        TodoItem.objects.create(title="Task 2", priority="MEDIUM")
        TodoItem.objects.create(title="Task 3", priority="LOW")
        
        url = reverse('todo-list')
        response = client.get(url)
        assert response.status_code == 200
        assert len(response.context['tasks']) == 3

    def test_todo_create_view_get(self, client):
        """Test GET request to create view"""
        url = reverse('todo-add')
        response = client.get(url)
        assert response.status_code == 200
        assert 'form' in response.context

    def test_todo_create_view_post_valid(self, client):
        """Test POST request to create view with valid data"""
        url = reverse('todo-add')
        data = {
            'title': 'New Task',
            'description': 'Test description',
            'priority': 'HIGH'
        }
        response = client.post(url, data)
        assert response.status_code == 302  # Redirect after success
        assert TodoItem.objects.count() == 1
        
        todo = TodoItem.objects.first()
        assert todo.title == 'New Task'
        assert todo.priority == 'HIGH'

    def test_todo_create_view_post_with_due_date(self, client):
        """Test creating a todo with due date"""
        url = reverse('todo-add')
        due_date = (timezone.now() + timedelta(days=1)).strftime('%Y-%m-%dT%H:%M')
        data = {
            'title': 'Task with Due Date',
            'due_date': due_date,
            'priority': 'MEDIUM'
        }
        response = client.post(url, data)
        assert response.status_code == 302
        assert TodoItem.objects.count() == 1

    def test_todo_update_view_get(self, client):
        """Test GET request to update view"""
        todo = TodoItem.objects.create(title="Original Title", priority="LOW")
        url = reverse('todo-edit', kwargs={'pk': todo.pk})
        response = client.get(url)
        assert response.status_code == 200
        assert 'form' in response.context
        assert response.context['object'] == todo

    def test_todo_update_view_post_valid(self, client):
        """Test POST request to update view with valid data"""
        todo = TodoItem.objects.create(title="Original Title", priority="LOW")
        url = reverse('todo-edit', kwargs={'pk': todo.pk})
        data = {
            'title': 'Updated Title',
            'description': 'Updated description',
            'priority': 'HIGH',
            'completed': True
        }
        response = client.post(url, data)
        assert response.status_code == 302
        
        todo.refresh_from_db()
        assert todo.title == 'Updated Title'
        assert todo.priority == 'HIGH'
        assert todo.completed is True

    def test_todo_delete_view_get(self, client):
        """Test GET request to delete view (confirmation page)"""
        todo = TodoItem.objects.create(title="To Delete")
        url = reverse('todo-delete', kwargs={'pk': todo.pk})
        response = client.get(url)
        assert response.status_code == 200
        assert response.context['object'] == todo

    def test_todo_delete_view_post(self, client):
        """Test POST request to delete view"""
        todo = TodoItem.objects.create(title="To Delete")
        url = reverse('todo-delete', kwargs={'pk': todo.pk})
        response = client.post(url)
        assert response.status_code == 302
        assert TodoItem.objects.count() == 0

    def test_toggle_complete_view(self, client):
        """Test toggling completion status"""
        todo = TodoItem.objects.create(title="Toggle Test", completed=False)
        url = reverse('todo-toggle', kwargs={'pk': todo.pk})
        
        # Toggle to completed
        response = client.get(url)
        assert response.status_code == 302
        todo.refresh_from_db()
        assert todo.completed is True
        
        # Toggle back to incomplete
        response = client.get(url)
        assert response.status_code == 302
        todo.refresh_from_db()
        assert todo.completed is False

    def test_todo_list_ordering(self, client):
        """Test that todo list is ordered by completed status and due date"""
        # Create tasks with different statuses and dates
        TodoItem.objects.create(
            title="Incomplete Task 1",
            completed=False,
            due_date=timezone.now() + timedelta(days=1)
        )
        TodoItem.objects.create(
            title="Completed Task",
            completed=True,
            due_date=timezone.now() + timedelta(days=2)
        )
        TodoItem.objects.create(
            title="Incomplete Task 2",
            completed=False,
            due_date=timezone.now() + timedelta(days=3)
        )
        
        url = reverse('todo-list')
        response = client.get(url)
        tasks = response.context['tasks']
        
        # Incomplete tasks should come before completed tasks
        assert tasks[0].completed is False
        assert tasks[1].completed is False
        assert tasks[2].completed is True

    def test_nonexistent_todo_update(self, client):
        """Test updating a non-existent todo returns 404"""
        url = reverse('todo-edit', kwargs={'pk': 9999})
        response = client.get(url)
        assert response.status_code == 404

    def test_nonexistent_todo_delete(self, client):
        """Test deleting a non-existent todo returns 404"""
        url = reverse('todo-delete', kwargs={'pk': 9999})
        response = client.get(url)
        assert response.status_code == 404

    def test_nonexistent_todo_toggle(self, client):
        """Test toggling a non-existent todo returns 404"""
        url = reverse('todo-toggle', kwargs={'pk': 9999})
        response = client.get(url)
        assert response.status_code == 404
