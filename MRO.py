
class Person:
    def greet(self):
        print("Hello from Person")

class Employee(Person):
    def greet(self):
        print("Hello from Employee")

class Manager(Employee):
    def greet(self):
        print("Hello from Manager")

class TeamLead(Employee, Person):  # Multiple Inheritance
    pass

# Check MRO
print(TeamLead._mro_)  
# Output: (<class '_main.TeamLead'>, <class 'main.Employee'>, <class 'main_.Person'>, <class 'object'>)

# Usage
tl = TeamLead()
tl.greet()  # Output: "Hello from Employee" (since Employee comes before Person in MRO)