import json
import os
from config import TASK_FILE_NAME

def read_tasks(file_name = TASK_FILE_NAME):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            data = json.load(file)
        return data
    else:
        return []

def save_to_file(content, filename = TASK_FILE_NAME):
    with open(filename, 'w') as out_file:
        json.dump(content, out_file, indent=4)
