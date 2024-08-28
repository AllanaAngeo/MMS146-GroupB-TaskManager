from datetime import date
from task import Task
"""
    Reminder class object based on the task class:
        - Generates reminders indicating how many days before or after a due date of a task
        - Calculates the time remaining until the task's due date.
        - Shows which task the reminder was for.
"""
class Reminder(Task):
    def __init__(self, task_name, description, due_date, notifications="", priority_level=0, completion_status="Not Started"):
        super().__init__(task_name, description, due_date, priority_level, completion_status)
        self.notifications = notifications

    def calculate_time_until_deadline(self):
        current_date = date.today()
        return self.due_date - current_date 

    def generate_reminder (self):
        difference = self.calculate_time_until_deadline()
        if difference.days >= 0:
            print(f"{self.task_name} is due in {difference.days} days")
        else: 
            print(f"{self.task_name} was due {-difference.days} days ago.")

    def display_notif(self):
        print(f"{self.task_name} Reminder: {self.notifications}")

#Reminder Class Case Testers
#Before Due Date
def reminder_test_before_due():
    reminder = Reminder(
        task_name= "MMS 146 Group Project",
        description= "Submit the repository",
        due_date=date(2024,8,31),
        notifications="Remember to check the code before submitting"
    )

    reminder.display_notif()
    reminder.generate_reminder()

#After Due Date
def reminder_test_after_due():
    reminder = Reminder(
        task_name="KAS 1 Final Exam",
        description= "Take the final exam",
        due_date=date(2024,8,25),
        notifications="Don't forget to take the exam!"
    )

    reminder.display_notif()
    reminder.generate_reminder()

#Tester Function Run
reminder_test_before_due()
reminder_test_after_due()
