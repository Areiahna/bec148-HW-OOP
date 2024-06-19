# Task 1: Vehicle Registration System

# Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. Implement a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle and demonstrate changing the owner.

# Expected Outcome: Completion of the Vehicle class with the update_owner method and a demonstration script showing the creation of Vehicle objects and updating their owners.

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self,new_owner):
        print(f'The previous owner of this vehicle was {self.owner}')
        self.owner = new_owner
        print (f'The current owner of this vehicle is now {self.owner}')

camry = Vehicle(27856,"sedan","Arei")
camry.update_owner("Travis")
