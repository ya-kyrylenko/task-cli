#!/usr/bin/env python3

import json
import os
import sys

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

    new_task = {
        'id': len(tasks) + 1,
        'desc': description,
        'status': status,
    }
    tasks.append(new_task)
    save_to_file(tasks)
    print(f"Task added successfully (ID: {new_task['id']})")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    args = sys.argv[1:]
    if args[0] == 'add':
        print("Adding new task")
        add_new_task(args[1])


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
