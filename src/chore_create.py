import json
import os
import datetime

'''
This section is focused on the chore class, which is used to create and manage chores.
The chore class has attributes for the name, description, frequency, length, area, start date, last completed date, and next due date of the chore. 
It also has methods for updating the chore's attributes, deleting the chore, getting the chore's information as a dictionary, and marking the chore as completed by updating the last completed date to the current date and time.
'''

class chore:
    def __init__(self, name, description, frequency, length, area, start_date = None, last_completed=None, next_due_date=None):
        self.name = name
        self.description = description
        self.frequency = frequency
        self.length = length
        self.area = area
        if start_date is None:
            self.start_date = datetime.datetime.now().strftime("%Y-%m-%d")
        else:
            self.start_date = start_date
        self.last_completed = last_completed
        self.next_due_date = next_due_date

    def __str__(self):
        return f"Chore: {self.name}\nDescription: {self.description}\nFrequency: {self.frequency}\nLength: {self.length}\nArea: {self.area}\nStart Date: {self.start_date}\nLast Completed: {self.last_completed}\nNext Due Date: {self.next_due_date}"

    def update(self, name=None, description=None, frequency=None, length=None, area=None, start_date=None, last_completed=None, next_due_date=None):
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if frequency is not None:
            self.frequency = frequency
        if length is not None:
            self.length = length
        if area is not None:
            self.area = area
        if start_date is not None:
            self.start_date = start_date
        if last_completed is not None:
            self.last_completed = last_completed
        if next_due_date is not None:
            self.next_due_date = next_due_date

    def delete(self):
        del self.name
        del self.description
        del self.frequency
        del self.length
        del self.area
        del self.start_date
        del self.last_completed
        del self.next_due_date

    def get_info(self):
            return {
                "name": self.name,
                "description": self.description,
                "frequency": self.frequency,
                "length": self.length,
                "area": self.area,
                "start_date": self.start_date,
                "last_completed": self.last_completed,
                "next_due_date": self.next_due_date
            }
        
    def mark_completed(self):
            self.last_completed = datetime.datetime.now()