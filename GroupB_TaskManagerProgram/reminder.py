from datetime import date
from task import Task
'''
    Reminder class object based on the task class:
       - also creates tasks
       - has attributes... padagdag nalang arghhhh
    '''
class Reminder(Task):
    def __init__(self, task: Task, notifications=""): #This does something ganito
        self.task = task
        self.time_until_deadline = self.calculate_time_until_deadline()
        self.notifications = notifications

    def calculate_time_until_deadline(self):#This does something ganire
        current_date = date.today()
        return self.task.due_date - current_date 

    def generate_reminder (self):
        difference = self.time_until_deadline
        if difference.days >= 0:
            print(f"The task is due in {difference.days} days")
        else: 
            print(f"The task {self.task_name} was due {-difference.days} days ago.")

    def display_notif(self):
        print(self.notifications)
