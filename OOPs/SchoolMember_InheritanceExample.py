class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name}. I am {self.age} years old."

class Student(SchoolMember):
    def __init__(self, name, age, my_class, roll_no):
        super().__init__(name, age)
        self.my_class = my_class
        self.roll_no = roll_no
    # Overriding the introduce method
    def introduce(self):
        super().introduce()
        return f"I am in {self.my_class} class. My roll number is {self.roll_no}."
    
class Teacher(SchoolMember):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary

    def introduce(self):
        super().introduce()
        return f"I Teach {self.subject} subject. My salary is {self.salary}."
        