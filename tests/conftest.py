import pytest
import copy

from unittest.mock import patch
from task_manager import TaskManager

@pytest.fixture
def test_data():
    return [{"id": 1, "title": "Test Task"}]

@pytest.fixture
def sample_tasks():
    return [
        {
            "id": 1,
            "desc": "Task 1",
            "status": "todo",
            "createdAt": "2025-02-13#22:36:43",
            "updatedAt": "2025-02-13#22:36:43"
        },
        {
            "id": 2,
            "desc": "Task 2",
            "status": "in-progress",
            "createdAt": "2025-02-13#22:36:44",
            "updatedAt": "2025-02-13#22:36:44"
        },
        {
            "id": 3,
            "desc": "Task 3",
            "status": "done",
            "createdAt": "2025-02-13#22:36:46",
            "updatedAt": "2025-02-13#22:36:46"
        }
    ]

@pytest.fixture
def tasks(sample_tasks):
    return copy.deepcopy(sample_tasks)

@pytest.fixture
def mock_save():
    with patch("decorators.save_to_file") as mock:
        yield mock

@pytest.fixture
def test_path(tmp_path):
    return tmp_path / "test_tasks.json"

@pytest.fixture
def manager_with_tasks(test_path, tasks):
    with patch("task_manager.read_tasks", return_value=tasks):
        return TaskManager(str(test_path))
