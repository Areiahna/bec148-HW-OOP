# Task 2: Event Management System Enhancement

# Problem Statement: Use the existing Event class by adding an instance attribute to keep track of the number of participants. Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.
# Code Example: Basic Event class without participant tracking.

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participants = 0

    def add_participant(self,x):
        self.participants +=x
    
    def get_participant_count(self):
        print(self.participants)

party = Event("Friendsgiving","Nov 16th")
party.add_participant(2)
party.add_participant(3)

#Expecting 5

party.get_participant_count()
