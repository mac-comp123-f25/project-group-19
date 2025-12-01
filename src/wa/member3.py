"""This is where Helen will try to figure out how to save stuff."""
import csv
#I think this works?
def save_tasks(task_list):
    with open('tasks.csv','w',newline='') as my_csv:
        writer=csv.writer(my_csv)
        for task in task_list:
            writer.writerow([task[0],task[1]])