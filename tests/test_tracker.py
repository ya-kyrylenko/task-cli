from main import add_new_task, update_task
from decorators import _save_to_file
import json

def test_save_to_file(tmp_path):
    test_file = tmp_path / "test_tasks.json"
    test_data = [{"id": 1, "title": "Test Task"}]
    _save_to_file(test_data, test_file)

    with open(test_file, "r") as f:
        saved_data = json.load(f)

    assert saved_data == test_data

def test_add_new_task(tasks, mock_save):
    new_task = "Test task"
    add_new_task(tasks, new_task)

    assert any(task["desc"] == new_task and task["status"] == 'todo' for task in tasks)

def test_add_task_save_to_file_called(tasks, mock_save):
    add_new_task(tasks, "Test task")
    mock_save.assert_called_once()

def test_add_new_task_output(tasks, capfd, mock_save):
    add_new_task(tasks, "Test task")
    captured = capfd.readouterr()

    assert "Task added successfully (ID:" in captured.out

def test_successful_update_task(tasks, mock_save):
    updated_task = "Updated task"
    updated_id = 1
    update_task(tasks, updated_id, updated_task)

    assert tasks[0]["id"] == updated_id
    assert tasks[0]["desc"] == updated_task

def test_update_task_save_to_file_called(tasks, mock_save):
    update_task(tasks, 1, "Test task")
    mock_save.assert_called_once()

def test_unsuccessful_update_task(tasks, capfd, mock_save):
    wrong_id = 99
    update_task(tasks, wrong_id, "Updated task")
    captured = capfd.readouterr()

    assert f"There are no task with ID {wrong_id}" in captured.out

def test_update_task_save_to_file_not_called(tasks, mock_save):
    update_task(tasks, 99, "Test task")
    mock_save.assert_not_called()