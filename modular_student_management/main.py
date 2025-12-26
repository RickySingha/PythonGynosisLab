
from student_module import Student, create_student, display_student
from marks_module import MarksProcessor
from attendance_module import AttendanceTracker
from fees_module import FeeManager
from report_module import ReportGenerator
import math
import datetime
import random

def print_separator():
    print("\n" + "="*60 + "\n")

def demonstrate_builtin_modules():
    
    print_separator()
    print("SYSTEM INFORMATION")
    print("-" * 60)
    
    # Math module
    print(f"Mathematical Constants:")
    print(f"  Pi value: {math.pi}")
    print(f"  Square root of 16: {math.sqrt(16)}")
    print(f"  Random calculation: {math.pow(2, 8)}")
    
   
    today = datetime.date.today()
    print(f"\nDate Information:")
    print(f"  Current date: {today}")
    print(f"  Day of week: {today.strftime('%A')}")
    
    
    print(f"\nRandom Data:")
    print(f"  Generated ID: {random.randint(1000, 9999)}")

def demonstrate_module_properties():
    
    print_separator()
    print("MODULE INFORMATION")
    print("-" * 60)
    
    import marks_module
    print(f"Marks Module Name: {marks_module.__name__}")
    print(f"Marks Module Location: {marks_module.__file__}")
    print(f"Available Functions: {[name for name in dir(marks_module) if not name.startswith('_')]}")

def main():
   
    print("="*60)
    print("STUDENT MANAGEMENT SYSTEM")
    print("="*60)
    
    # Create student using user-defined module
    print_separator()
    print("STUDENT REGISTRATION")
    print("-" * 60)
    
    num_students = int(input("How many students do you want to add? "))
    students = []
    
    for i in range(num_students):
        print(f"\n--- Student {i+1} ---")
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        roll_no = input("Enter roll number: ")
        
        student = create_student(name, age, roll_no)
        students.append(student)
        display_student(student)
    
    # Marks processing system
    print_separator()
    print("MARKS ENTRY & PROCESSING")
    print("-" * 60)
    
    marks_processor = MarksProcessor()
    
    for student in students:
        print(f"\nEnter marks for {student.name}:")
        subjects = {}
        for subject in ["Math", "Science", "English"]:
            marks = float(input(f"  {subject}: "))
            subjects[subject] = marks
        
        marks_processor.add_student_marks(student.roll_no, subjects)
    
    # Display marks statistics
    for student in students:
        stats = marks_processor.get_student_statistics(student.roll_no)
        print(f"\n{student.name}'s Performance:")
        print(f"  Average: {stats['average']:.2f}")
        print(f"  Grade: {stats['grade']}")
    
    # Report generation with classes
    print_separator()
    print("GENERATING STUDENT REPORTS")
    print("-" * 60)
    
    report_gen = ReportGenerator()
    
    for student in students:
        stats = marks_processor.get_student_statistics(student.roll_no)
        report_gen.generate_student_report(student, stats)
    
    # Separate modules integration
    print_separator()
    print("ATTENDANCE & FEE MANAGEMENT")
    print("-" * 60)
    
    attendance_tracker = AttendanceTracker()
    fee_manager = FeeManager()
    
    for student in students:
        # Attendance
        present_days = int(input(f"\nPresent days for {student.name}: "))
        total_days = int(input(f"Total days: "))
        attendance_tracker.mark_attendance(student.roll_no, present_days, total_days)
        
        # Fees
        total_fee = float(input(f"Total fee for {student.name}: "))
        paid_fee = float(input(f"Paid amount: "))
        fee_manager.add_fee_record(student.roll_no, total_fee, paid_fee)
    
    # Display integrated data
    print("\n--- Complete Student Records ---")
    for student in students:
        print(f"\n{student.name} ({student.roll_no}):")
        
        attendance_tracker.display_attendance(student.roll_no)
        fee_manager.display_fee_status(student.roll_no)
    
    # Built-in modules
    demonstrate_builtin_modules()
    
    # Module properties
    demonstrate_module_properties()
    
    print_separator()
    print("Thank you for using the Student Management System!")
    print("="*60)

if __name__ == "__main__":
    main()