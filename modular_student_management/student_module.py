

class Student:
    
    
    def __init__(self, name, age, roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no
    
    def show(self):
       
        print(f"Student Name: {self.name}")
        print(f"Student Age: {self.age}")
        print(f"Roll Number: {self.roll_no}")
    
    def get_details(self):
        
        return {
            'name': self.name,
            'age': self.age,
            'roll_no': self.roll_no
        }

def create_student(name, age, roll_no):
    
    return Student(name, age, roll_no)

def display_student(student):
    
    student.show()

def validate_age(age):
    
    return 5 <= age <= 100

def validate_roll_no(roll_no):
   
    return len(roll_no) > 0


STUDENT_COUNT = 0

def increment_student_count():
    """Increment global student count"""
    global STUDENT_COUNT
    STUDENT_COUNT += 1
    return STUDENT_COUNT