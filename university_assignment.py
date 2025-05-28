class Person:
    def __init__(self, name, age, email):  # Fixed: double underscores
        self.name = name
        self.age = age
        self.email = email

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Email: {self.email}")


class Student(Person):
    def __init__(self, name, age, email, student_id, major):  # Fixed: double underscores
        super().__init__(name, age, email)  # Fixed: double underscores
        self.student_id = student_id
        self.major = major

    def display_info(self):  # Overridden
        print(f"STUDENT: {self.name}, ID: {self.student_id}, Major: {self.major}")


class Lecturer(Person):
    def __init__(self, name, age, email, employee_id, department):  # Fixed
        super().__init__(name, age, email)  # Fixed
        self.employee_id = employee_id
        self.department = department

    def display_info(self):  # Overridden
        print(f"LECTURER: {self.name}, ID: {self.employee_id}, Dept: {self.department}")


class Staff(Person):
    def __init__(self, name, age, email, staff_id, role):  # Fixed
        super().__init__(name, age, email)  # Fixed
        self.staff_id = staff_id
        self.role = role

    def display_info(self):  # Overridden
        print(f"STAFF: {self.name}, ID: {self.staff_id}, Role: {self.role}")


# Create objects
people = [
    Student("Alice", 20, "alice@uni.edu", "S1001", "Computer Science"),
    Lecturer("Dr. Smith", 45, "smith@uni.edu", "L2001", "Engineering"),
    Staff("Bob", 30, "bob@uni.edu", "E3001", "Administrator")
]

# Polymorphic call to display_info()
for person in people:
    person.display_info()