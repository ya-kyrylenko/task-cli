import json
import os
from datetime import datetime
from decorators import auto_save
from config import VALID_STATUSES

class TaskManager:
    def __init__(self, file_name):
        self.file_name = file_name
        self.tasks = self._read_tasks()

    def _read_tasks(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                data = json.load(file)
            return data
        else:
            return []

    def _get_next_id(self):
        return max((task["id"] for task in self.tasks), default=0) + 1

    def _get_time(self):
        return datetime.now().isoformat('#', 'seconds')

    def _find_task_by_id(self, id):
        return next((task for task in self.tasks if task['id'] == id), None)

    @auto_save
    def add_new_task(self, description, status = 'todo'):
        date_time = self._get_time()
        id = self._get_next_id()

        new_task = {
            'id': id,
            'desc': description,
            'status': status,
            'createdAt': date_time,
            'updatedAt': date_time
        }
        self.tasks.append(new_task)
        return id

    @auto_save
    def update_task(self, id, new_desc):
        task = self._find_task_by_id(id)
        if task:
            task['desc'] = new_desc
            task['updatedAt'] = self._get_time()
            return id
        else:
            return None

    @auto_save
    def delete_task(self, id):
        task = self._find_task_by_id(id)
        if task:
            self.tasks.remove(task)
            return id
        else:
            return None

    @auto_save
    def change_status(self, status, id):
        task = self._find_task_by_id(id)
        if task:
            task['status'] = status
            return id
        else:
            return None

    def list_tasks(self, status = None):
        tasks = self.tasks
        if status and status in VALID_STATUSES:
            tasks = [task for task in self.tasks if task["status"] == status]
        elif status:
            print(f"Status should match one of this: {VALID_STATUSES}")
            return
        for task in tasks:
            print(f"Task id:{task["id"]}, description: '{task["desc"]}', status: {task['status']}")
