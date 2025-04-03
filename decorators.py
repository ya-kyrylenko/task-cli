import functools
import copy
from file_utils import save_to_file

def auto_save(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        tasks_before = copy.deepcopy(self.tasks)
        result = func(self, *args, **kwargs)
        if tasks_before != self.tasks:
            save_to_file(self.tasks, self.file_name)
        return result
    return wrapper

def clear_tasks():
    save_to_file([])
    print("Tasks file cleared")