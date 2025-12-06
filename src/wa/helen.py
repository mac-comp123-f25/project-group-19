"""This is where Helen will figure out how to save stuff."""
import csv

def save_tasks(task_list):
    with open('wa/tasks.csv','w',newline='') as my_csv:
        writer = csv.writer(my_csv)
        for task in task_list:
            writer.writerow([task[0],task[1]])

def get_tasks():
    saved_list=[]
    with open('wa/tasks.csv') as saved_tasks:
        reader = csv.reader(saved_tasks)
        for task_row in reader:
            # Each task_row is a list.
            # saved_list is a list of tuples
            saved_list.append(tuple(task_row))
        return saved_list