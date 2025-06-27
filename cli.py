import argparse
from config import TASK_FILE_NAME
from task_manager import TaskManager
import constants
from decorators import clear_tasks

def get_parser():
    parser = argparse.ArgumentParser(description='Task CLI Application')
    subparsers = parser.add_subparsers(dest='command', required=True)

    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('description', type=str, help='Description of the task')

    update_parser = subparsers.add_parser('update', help='Update an existing task')
    update_parser.add_argument('id', type=int, help='ID of the task to update')
    update_parser.add_argument('description', type=str, help='New description of the task')

    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('id', type=int, help='ID of the task to delete')

    list_parser = subparsers.add_parser('list', help='List tasks')
    list_parser.add_argument('status', type=str, nargs='?', choices=['todo', 'in-progress', 'done'], help ='Filter tasks by status')

    mark_parser = subparsers.add_parser('mark', help='Change status of a task')
    mark_parser.add_argument('status', type=str, choices=['in-progress', 'done'], help='New status of the task')
    mark_parser.add_argument('id', type=int, help="ID of the task to update")

    subparsers.add_parser('clear', help='Clear all tasks')

    return parser

def run_cli():
    parser = get_parser()
    args = parser.parse_args()
    task_manager = TaskManager(TASK_FILE_NAME)
    if args.command == 'add':
        task_id = task_manager.add_new_task(args.description)
        print(constants.TASK_ADDED.format(task_id))
    elif args.command == 'list':
        task_manager.list_tasks(args.status)
    elif args.command == 'update':
        task_id = task_manager.update_task(args.id, args.description)
        if task_id:
            print(constants.TASK_UPDATED.format(task_id))
        else:
            print(constants.TASK_NOT_FOUND.format(args.id))
    elif args.command == 'delete':
        task_id = task_manager.delete_task(args.id)
        if task_id:
            print(constants.TASK_REMOVED.format(task_id))
        else:
            print(constants.TASK_NOT_FOUND.format(args.id))
    elif args.command == 'mark':
        task_id = task_manager.change_status(args.status, args.id)
        if task_id:
            print(constants.TASK_STATUS_CHANGED.format(task_id, args.status))
        else:
            print(constants.TASK_NOT_FOUND.format(args.id))
    elif args.command == 'clear':
        clear_tasks()
