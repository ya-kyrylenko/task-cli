#!/usr/bin/env python3

import json
import os
import sys
from datetime import datetime

TASK_FILE_NAME = 'tasks.json'
VALID_STATUSES = {'todo', 'in-progress', 'done'}

def _save_to_file(content):
    with open(TASK_FILE_NAME, 'w') as out_file:
        json.dump(content, out_file, indent=4)

def read_tasks(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            data = json.load(file)
        return data
    else:
        return []

def _get_next_id(tasks):
    return max((task["id"] for task in tasks), default=0) + 1

def add_new_task(tasks, description, status = 'todo'):
    date_time = _get_time()

    new_task = {
        'id': _get_next_id(tasks),
        'desc': description,
        'status': status,
        'createdAt': date_time,
        'updatedAt': date_time
    }
    tasks.append(new_task)
    _save_to_file(tasks)
    print(f"Task added successfully (ID: {new_task['id']})")

def update_task(tasks, id, new_desc):
    task = _find_task_by_id(tasks, id)
    if task:
        task['desc'] = new_desc
        task['updatedAt'] = _get_time()
        print(f"Task updated successfully (ID: {id})")
        _save_to_file(tasks)
    else:
        _no_id_notice(id)

def delete_task(tasks, id):
    task = _find_task_by_id(tasks, id)
    if task:
        tasks.remove(task)
        print(f"Task removed successfully (ID: {id})")
        _save_to_file(tasks)
    else:
        _no_id_notice(id)

def change_status(tasks, status, id):
    task = _find_task_by_id(tasks, id)
    if task:
        task['status'] = status
        print(f'Task (ID: {id}) changed status to "{status}" successfully')
        _save_to_file(tasks)
    else:
        _no_id_notice(id)

def _find_task_by_id(tasks, id):
    return next((task for task in tasks if task['id'] == id), None)

def _get_time():
    return datetime.now().isoformat()

def _no_id_notice(id):
    print(f"There are no task with ID {id}")

def _number_notice():
    print("Error: ID must be a number.")

def list_tasks(tasks, status = None):
    if status and status in VALID_STATUSES:
        tasks = [task for task in tasks if task["status"] == status]
    elif status:
        print(f"Status should match one of this: {statuses}")
        return
    for task in tasks:
        print(f"Task id:{task["id"]}, description: '{task["desc"]}', status: {task['status']}")

def clear_tasks():
    _save_to_file([])
    print("Tasks file cleared")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    args = sys.argv[1:]
    tasks = read_tasks(TASK_FILE_NAME)
    if len(args) == 0:
        print("Please add some info, example: add 'Task description'")
        print("You also can update, delete, list tasks")
    elif len(args) >= 1:
        if args[0] == 'add':
            try:
                task_message = args[1]
                add_new_task(tasks, task_message)
            except IndexError:
                print("After 'add' command you should specify task message")
                print("Example: add 'Visit grandma'")
                print("Notice you should add quotes at start and end of the message")
        elif args[0] == 'list':
            if len(args) > 1:
                status = args[1]
                list_tasks(tasks, status)
            else:
                list_tasks(tasks)
        elif args[0] == 'update':
            try:
                index = int(args[1])
                description = args[2]
                update_task(tasks, index, description)
            except ValueError:
                print("Error: ID must be a number.")
            except IndexError:
                print("After 'update' command you should specify id for desired task and updated task message")
                print("Example: update 1 'Visit grandma and grandfather'")
        elif args[0] == 'delete':
            try:
                index = int(args[1])
                delete_task(tasks, index)
            except ValueError:
                _number_notice()
            except IndexError:
                print("After 'delete' command you should specify id for desired task")
                print("Example: delete 1")
        elif args[0] in ['mark-in-progress', 'mark-done']:
            try:
                _, _, status = args[0].partition('-')
                id = int(args[1])
                change_status(tasks, status, id)
            except IndexError:
                print("After 'mark-in-progress' or 'mark-done' commands you should specify desired id")
                print('Example: mark-done 2')
            except ValueError:
                _number_notice()
        elif args[0] == 'clear':
            clear_tasks()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
