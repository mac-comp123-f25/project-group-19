
TASKLIST = []

class Task:
    def __init__(self, name, due, work_date, cat):
        self.name = name
        self.due = due
        self.work_date = work_date
        self.cat = cat

def make_task(name, due, work_date, cat):
    task = Task(name, due, work_date, cat)
    return task

def get_task_name(task):
    return task.name

def get_task_due(task):
    return task.due

def get_task_work_date(task):
    return task.work_date

def get_task_cat(task):
    return task.cat

def get_task_all(task):
    return task

def add_to_tasklist(tasklist, task):
    tasklist.append(task)
