import json
import functools
import copy
from config import TASK_FILE_NAME

def _save_to_file(content, filename=TASK_FILE_NAME):
    with open(filename, 'w') as out_file:
        json.dump(content, out_file, indent=4)

def auto_save(func):
    @functools.wraps(func)
    def wrapper(tasks, *args, **kwargs):
        tasks_before = copy.deepcopy(tasks)
        result = func(tasks, *args, **kwargs)
        if tasks_before != tasks:
            _save_to_file(tasks)
        return result
    return wrapper

def clear_tasks():
    _save_to_file([])
    print("Tasks file cleared")