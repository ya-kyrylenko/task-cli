#!/usr/bin/env python3

import json
import os
import sys
from datetime import datetime

TASK_FILE_NAME = 'tasks.json'

def save_to_file(content):
    with open(TASK_FILE_NAME, 'w') as out_file:
        json.dump(content, out_file, indent=4)

def read_tasks(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            data = json.load(file)
        return data
    else:
        return []

def add_new_task(description, status = 'todo'):
    tasks = read_tasks(TASK_FILE_NAME)
    date_time = get_time()

    new_task = {
        'id': len(tasks) + 1,
        'desc': description,
        'status': status,
        'createdAt': date_time,
        'updatedAt': date_time
    }
    tasks.append(new_task)
    save_to_file(tasks)
    print(f"Task added successfully (ID: {new_task['id']})")

def update_task(index, new_desc):
    tasks = read_tasks(TASK_FILE_NAME)
    task = next((task for task in tasks if task['id'] == index), None)
    if task:
        task['desc'] = new_desc
        task['updatedAt'] = get_time()
        print(f"Task updated successfully (ID: {index})")
        save_to_file(tasks)
    else:
        print(f"There are no task with ID {index}")

def get_time():
    return datetime.now().isoformat()

def list_tasks():
    tasks = read_tasks(TASK_FILE_NAME)
    for task in tasks:
        print(f"Task id:{task["id"]}, description: '{task["desc"]}', status: {task['status']}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    args = sys.argv[1:]
    if args[0] == 'add':
        try:
            add_new_task(args[1])
        except IndexError:
            print("After 'add' command you should specify task message")
            print("Example: add 'Visit grandma'")
            print("Notice you should add quotes at start and end of the message")
    elif args[0] == 'list':
        list_tasks()
    elif args[0] == 'update':
        try:
            index = int(args[1])
            description = args[2]
            update_task(index, description)
        except ValueError:
            print("Error: ID must be a number.")
        except IndexError:
            print("After 'update' command you should specify id for desired task and updated task message")
            print("Example: update 1 'Visit grandma and grandfather'")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
