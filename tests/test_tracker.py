from file_utils import save_to_file

import copy
import json
from task_manager import TaskManager

def test_save_to_file(test_data, test_path):
    save_to_file(test_data, test_path)

    with open(test_path, "r") as f:
        saved_data = json.load(f)

    assert saved_data == test_data

def test_add_new_task(mock_save, test_path):
    manager = TaskManager(test_path)
    new_task = "Test add new task"
    manager.add_new_task(new_task)

    assert any(task["desc"] == new_task and task["status"] == 'todo' for task in manager.tasks)

def test_add_task_save_to_file_called(mock_save, test_path):
    manager = TaskManager(test_path)
    new_task = "Test task"
    manager.add_new_task(new_task)
    mock_save.assert_called_once()

def test_successful_update_task(manager_with_tasks, mock_save):
    initial_tasks = copy.deepcopy(manager_with_tasks.   tasks)

    updated_task = "Updated task"
    updated_id = 1
    manager_with_tasks.update_task(updated_id, updated_task)

    assert any(task["desc"] == updated_task and task["id"] == updated_id for task in manager_with_tasks.tasks)
    assert sum(task["id"]==updated_id for task in manager_with_tasks.tasks) == 1
    assert manager_with_tasks.tasks != initial_tasks

def test_update_task_save_to_file_called(manager_with_tasks, mock_save):
    manager_with_tasks.update_task(1, "Updated task")
    mock_save.assert_called_once()

def test_unsuccessful_update_task(manager_with_tasks, mock_save):
    initial_tasks = copy.deepcopy(manager_with_tasks.tasks)
    updated_task = "Updated task"
    wrong_id = 99
    manager_with_tasks.update_task(wrong_id, updated_task)

    assert not any(task["id"] == wrong_id for task in manager_with_tasks.tasks)
    assert manager_with_tasks.tasks == initial_tasks

def test_update_task_save_to_file_not_called(manager_with_tasks, mock_save):
    updated_task = "Updated task"
    wrong_id = 99
    manager_with_tasks.update_task(wrong_id, updated_task)
    mock_save.assert_not_called()