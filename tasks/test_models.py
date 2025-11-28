import pytest
from django.utils import timezone
from datetime import timedelta
from tasks.models import TodoItem


@pytest.mark.django_db
class TestTodoItemModel:
    """Test cases for TodoItem model"""

    def test_create_todo_item_with_required_fields(self):
        """Test creating a todo item with only required fields"""
        todo = TodoItem.objects.create(title="Test Task")
        assert todo.title == "Test Task"
        assert todo.description is None
        assert todo.due_date is None
        assert todo.priority == "MEDIUM"  # Default priority
        assert todo.completed is False
        assert todo.created_at is not None
        assert todo.updated_at is not None

    def test_create_todo_item_with_all_fields(self):
        """Test creating a todo item with all fields"""
        due_date = timezone.now() + timedelta(days=1)
        todo = TodoItem.objects.create(
            title="Complete Task",
            description="This is a test description",
            due_date=due_date,
            priority="HIGH",
            completed=True
        )
        assert todo.title == "Complete Task"
        assert todo.description == "This is a test description"
        assert todo.due_date == due_date
        assert todo.priority == "HIGH"
        assert todo.completed is True

    def test_todo_item_str_method(self):
        """Test the string representation of TodoItem"""
        todo = TodoItem.objects.create(title="String Test")
        assert str(todo) == "String Test"

    def test_priority_choices(self):
        """Test all priority choices"""
        priorities = ["HIGH", "MEDIUM", "LOW"]
        for priority in priorities:
            todo = TodoItem.objects.create(
                title=f"Task with {priority} priority",
                priority=priority
            )
            assert todo.priority == priority

    def test_toggle_completed_status(self):
        """Test toggling the completed status"""
        todo = TodoItem.objects.create(title="Toggle Test")
        assert todo.completed is False
        
        todo.completed = True
        todo.save()
        assert todo.completed is True
        
        todo.completed = False
        todo.save()
        assert todo.completed is False

    def test_updated_at_changes_on_save(self):
        """Test that updated_at changes when the item is saved"""
        todo = TodoItem.objects.create(title="Update Test")
        original_updated_at = todo.updated_at
        
        # Small delay to ensure time difference
        import time
        time.sleep(0.1)
        
        todo.title = "Updated Title"
        todo.save()
        
        assert todo.updated_at > original_updated_at

    def test_multiple_todo_items(self):
        """Test creating multiple todo items"""
        TodoItem.objects.create(title="Task 1", priority="HIGH")
        TodoItem.objects.create(title="Task 2", priority="MEDIUM")
        TodoItem.objects.create(title="Task 3", priority="LOW")
        
        assert TodoItem.objects.count() == 3
        assert TodoItem.objects.filter(priority="HIGH").count() == 1
        assert TodoItem.objects.filter(priority="MEDIUM").count() == 1
        assert TodoItem.objects.filter(priority="LOW").count() == 1
