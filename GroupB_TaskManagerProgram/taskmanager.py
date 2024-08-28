from task import Task
from datetime import date

class TaskManager(Task):
    task_list = []
    def __init__(self, task_name, description, due_date):
        super().__init__(task_name, description, due_date)

    def add_task (self, task_name):
       if self.task_name == task_name:
           task_info = {
                "Task Name": self.task_name,
                "Description": self.description,
                "Due Date": self.due_date,
                "Priority Level": self.priority_level,
                "Completion Status": self.completion_status
            }
           TaskManager.task_list.append(task_info)
           print(f"Task '{task_name}' added!")

    #Not final, the code should look something like this (uses the functions of the task class for the edit_task function)
    def edit_task (self, cls, task_name, new_task_name=None, new_description=None, new_priority_level=None, new_completion_status=None, new_due_date=None):
        for task in cls.task_list: #finished edit method HIHI
            if task["Task Name"] == task_name:
                if new_task_name:
                    self.set_task_name()
                if new_description:
                    self.set_description()
                if new_priority_level:
                    self.set_priority()
                if new_completion_status:
                    self.set_completion_status()
                if new_due_date:
                    self.set_due_date()

    def delete_task (task_name):
        TaskManager.task_list = [task for task in TaskManager.task_list if task["Task Name"] != task_name]

    @classmethod
    def view_all_tasks(cls): #this is like flawless very nyamers this will stay
        print(cls.task_list)

    def sort_tasks_by_priority ():
        pass
    def get_overdue_tasks ():
        pass

task1 = TaskManager(
    task_name = "Task Manager Group Project",
    due_date=date(2024,9,1),
    description ="Reminder: Submit the group project!"
)
task1.add_task("Task Manager Group Project")
TaskManager.view_all_tasks()

task1.edit_task("Task Manager Group Project", new_task_name="Slay", new_description="Time to DTI!")

TaskManager.view_all_tasks()
