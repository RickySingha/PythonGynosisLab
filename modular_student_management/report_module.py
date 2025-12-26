

from datetime import datetime

class Report:
    
    def __init__(self, title):
        self.title = title
        self.generated_date = datetime.now()
    
    def print_header(self):
        print("\n" + "="*60)
        print(f"{self.title:^60}")
        print(f"Generated: {self.generated_date.strftime('%Y-%m-%d %H:%M:%S'):^60}")
        print("="*60)

class StudentReport(Report):
   
    
    def __init__(self, student, marks_stats):
        super().__init__("STUDENT PERFORMANCE REPORT")
        self.student = student
        self.marks_stats = marks_stats
    
    def generate(self):
        
        self.print_header()
        
        print(f"\nStudent Name: {self.student.name}")
        print(f"Roll Number: {self.student.roll_no}")
        print(f"Age: {self.student.age}")
        
        print("\n--- Academic Performance ---")
        print(f"Total Marks: {self.marks_stats['total']:.2f}")
        print(f"Average Marks: {self.marks_stats['average']:.2f}")
        print(f"Grade: {self.marks_stats['grade']}")
        
        print("\n--- Subject-wise Marks ---")
        for subject, marks in self.marks_stats['subjects'].items():
            print(f"{subject:.<20} {marks:.2f}")
        
        print("\n" + "="*60)

class ReportGenerator:
    
    
    def __init__(self):
        self.reports_generated = 0
    
    def generate_student_report(self, student, marks_stats):
        """Generate a student performance report"""
        report = StudentReport(student, marks_stats)
        report.generate()
        self.reports_generated += 1
    
    def generate_summary_report(self, students_data):
        
        report = Report("CLASS SUMMARY REPORT")
        report.print_header()
        
        print(f"\nTotal Students: {len(students_data)}")
        print("\n--- Student List ---")
        
        for i, student_data in enumerate(students_data, 1):
            print(f"{i}. {student_data['name']} - Roll No: {student_data['roll_no']}")
        
        print("\n" + "="*60)
        self.reports_generated += 1
    
    def get_report_count(self):
        
        return self.reports_generated