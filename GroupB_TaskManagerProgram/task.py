from datetime import date

class Task:

    def __init__(self, task_name, description, due_date, priority_level=0, completion_status="Not Started"):
        self.task_name = task_name
        self.description =  description
        self.due_date = due_date
        self.set_priority(priority_level)           #This is used to print out the Priority Level into Words 
        self.priority_level_num = 0                 #This will be used for Sorting out the Priorities in TaskManager
        self.completion_status = completion_status  #Ongoing or Completed ganern
        self.completion_status_num = 0              #This will be used for Sorting out the Status in TaskManager
    #update the name of the task
    def set_task_name (self, new_task_name):
        #Checks if the input is a string.
        if isinstance(new_task_name,str):
            return self.task_name
        else:
            print("Error Occured, Please Type the Description in Strings")

    #update the description of the task
    def set_description (self, new_description):
        #Checks if the input is a string.
        if isinstance(new_description,str):
            return self.description
        else:
            print("Error Occured, Please Type the Description in Strings")

    def set_due_date (self, new_date):
        #Checks if the input is in datetime.
        current_date = date.today()
        if isinstance(new_date, date.datetime):
            #Checks if the New Due Date is already passed the Current Day. 
            if new_date <= current_date:
                return self.due_date
        else:
            print("Error Occured, Please Type the New Due Date")
   
    def set_priority(self, new_priority_level):
         #Checks if the input is in numbers(integers)
        if isinstance(new_priority_level, int):
            # Mapping the numbers in the the Priority Levels.         
            priority_mapping = {
                0: "LOW PRIORITY",
                1: "MID PRIORITY",
                2: "HIGH PRIORITY"
            }
            if new_priority_level in priority_mapping:
                self.priority_level = priority_mapping[new_priority_level]
                self.priority_level_num = new_priority_level
            #Else, prints out error
            else:
                print("Error Occured, Please pick from 0-2")

    #update the completion status of the task 
    def set_completion_status (self, new_completion_status):
        status_mapping = {
                "Not Started": 2,
                "In Progress": 1,
                "Completed" : 0 
            }
        if isinstance(new_completion_status,str):
            if new_completion_status in status_mapping: #only changes value if its any of the valid statuses
                self.completion_status = new_completion_status
                self.completion_status_num = status_mapping[new_completion_status]
        else: 
            print('Error Occured, Please pick from "Not Started", "In Progress", and "Completed"')

    #Info of Tasks, and used for checking the Attributes.
    def task_info (self):
            task_details = {
                "Name": self.task_name,
                "Description": self.description,
                "Due Date": self.due_date,
                "Priority": self.priority_level,
                "Priority in Number": self.priority_level_num,
                "Completion Status": self.completion_status,
                "Completion Status in Number": self.completion_status_num

            }
            return task_details

task1 = Task("Fortnite", "Gaming", "2024,9,1")
task1.task_info()
task1.set_completion_status("In Progress")
print(task1.task_info())
