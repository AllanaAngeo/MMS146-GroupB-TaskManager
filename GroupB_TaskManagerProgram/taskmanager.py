from task import Task
from datetime import date

class TaskManager(Task):
    '''
    Task Manager class object based on the task class:
       - also creates tasks using the same attributes
       - adds, deletes, and edits tasks in a list
       - also allows to view task list, sort said list according to priority level,
         and display the overdue tasks
    '''
    task_list = [] #Task list for effective tasks
    def __init__(self, task_name, description, due_date):
        super().__init__(task_name, description, due_date) #Inherits Task class attributes and methods

    def add_task (self, task_name): 
       if self.task_name == task_name: #Checks if the task name is an attribute value of an instance
           task_info = {
                "Name": self.task_name,
                "Description": self.description,
                "Due Date": self.due_date,
                "Priority Level": self.priority_level,
                "Completion Status": self.completion_status #Creates a dictionary using the attributes of an instance
            } 
           TaskManager.task_list.append(task_info) #Adds dictionary to the task list
           print(f"Task '{self.task_name}' added!") #Notifies if the method has been executed successfully
           
    def edit_task (self, task_name, new_task_name=None, new_description=None, new_priority_level=None, new_completion_status=None, new_due_date=None):
        for task in TaskManager.task_list: #Use a for loop to go through each item (dictionary) of the task list
            if task["Name"] == task_name: #Checks if the task name is present in an item's (dictionary) key "Name" value
                TaskManager.delete_task(task_name) #Removes the matching dictionary
                if new_task_name:
                    self.set_task_name(new_task_name)
                if new_description:
                    self.set_description(new_description)
                if new_priority_level:
                    self.set_priority(new_priority_level)
                if new_completion_status:
                    self.set_completion_status(new_completion_status)
                if new_due_date:
                    self.set_due_date(new_due_date) #if any of the new_(attribute name) have value, it will call the method to change the attribute value
        updated_info = {
        "Name": self.task_name,
        "Description": self.description,
        "Due Date": self.due_date,
        "Priority Level": self.priority_level,
        "Completion Status": self.completion_status
        }
        TaskManager.task_list.append(updated_info) #Create new dictionary and add it again to the task list
        print(f"Task '{self.task_name}' updated!") #Notifies if the method is successful

    def delete_task (task_name):
        TaskManager.task_list = [task for task in TaskManager.task_list if task["Name"] != task_name]
        #Updates the task list to only include dictionaries whose key ["Name"] dont match with the task name
        print(f"Removed {task_name} from the list of tasks!")

    @classmethod
    def view_all_tasks(cls): #prints the contents of the list
        print(cls.task_list)

    @classmethod
    def sort_tasks_by_priority (cls):
        cls.task_list.sort(key=lambda task: task['Priority Level']) #Sorts the task list based on the dictionary key ["Priority Level"]
        print(f"Sorted tasks according to priority")

    def get_overdue_tasks ():
        overdue_tasks = [] #Create list for overdue tasks
        current_date = date.today() #Store today's date
        for task in TaskManager.task_list: #Checks if there are any due dates that are before today's date and adds them to the overdue list
            if task["Due Date"] < current_date:
                overdue_tasks.append(task)
        print("Here are the overdue tasks:")
        print(overdue_tasks)

task1 = TaskManager(
    task_name = "Task Manager Group Project",
    due_date=date(2024,9,1),
    description ="Reminder: Submit the group project!"
)

task2 = TaskManager(
    task_name = "MMS172",
    due_date=date(2024,8,25),
    description ="Recordd!"
)
task1.add_task("Task Manager Group Project")
TaskManager.view_all_tasks()
task2.add_task("MMS172")
TaskManager.view_all_tasks()

task1.edit_task("Task Manager Group Project", new_task_name="Slay", new_description="Time to DTI!", new_priority_level=0, new_due_date=date(2024,8,31))
task2.edit_task("MMS172", new_task_name="Final Project", new_description="Finish last methods", new_priority_level=2)

TaskManager.view_all_tasks()

TaskManager.sort_tasks_by_priority()

TaskManager.view_all_tasks()

TaskManager.get_overdue_tasks()

TaskManager.delete_task("Final Project")

TaskManager.view_all_tasks()
