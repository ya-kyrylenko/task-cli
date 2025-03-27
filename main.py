#!/usr/bin/env python3

import sys
from decorators import clear_tasks
from config import TASK_FILE_NAME
from task_manager import TaskManager
import constants

def _no_id_notice(id):
    print(f"There are no task with ID {id}")

def _number_notice():
    print("Error: ID must be a number.")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    args = sys.argv[1:]
    task_manager = TaskManager(TASK_FILE_NAME)
    if len(args) == 0:
        print("Please add some info, example: add 'Task description'")
        print("You also can update, delete, list tasks")
    elif len(args) >= 1:
        if args[0] == 'add':
            try:
                task_message = args[1]
                task_id = task_manager.add_new_task(task_message)
                print(constants.TASK_ADDED.format(task_id))
            except IndexError:
                print("After 'add' command you should specify task message")
                print("Example: add 'Visit grandma'")
                print("Notice you should add quotes at start and end of the message")
        elif args[0] == 'list':
            if len(args) > 1:
                status = args[1]
                task_manager.list_tasks(status)
            else:
                task_manager.list_tasks()
        elif args[0] == 'update':
            try:
                index = int(args[1])
                description = args[2]
                task_id = task_manager.update_task(index, description)
                if task_id:
                    print(constants.TASK_UPDATED.format(task_id))
                else:
                    print(constants.TASK_NOT_FOUND.format(index))
            except ValueError:
                print("Error: ID must be a number.")
            except IndexError:
                print("After 'update' command you should specify id for desired task and updated task message")
                print("Example: update 1 'Visit grandma and grandfather'")
        elif args[0] == 'delete':
            try:
                index = int(args[1])
                task_id = task_manager.delete_task(index)
                if task_id:
                    print(constants.TASK_REMOVED.format(task_id))
                else:
                    print(constants.TASK_NOT_FOUND.format(index))
            except ValueError:
                _number_notice()
            except IndexError:
                print("After 'delete' command you should specify id for desired task")
                print("Example: delete 1")
        elif args[0] in ['mark-in-progress', 'mark-done']:
            try:
                _, _, status = args[0].partition('-')
                id = int(args[1])
                task_id = task_manager.change_status(status, id)
                print(constants.TASK_STATUS_CHANGED.format(task_id, status))
            except IndexError:
                print("After 'mark-in-progress' or 'mark-done' commands you should specify desired id")
                print('Example: mark-done 2')
            except ValueError:
                _number_notice()
        elif args[0] == 'clear':
            clear_tasks()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
