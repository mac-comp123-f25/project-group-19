

class Task:
    def __init__(self, name, due, work_date, bin):
        self.name = name
        self.due = due
        self.work_date = work_date
        self.bin = bin


def make_task(name, due, work_date, bin):
    return Task(name, due, work_date, bin)