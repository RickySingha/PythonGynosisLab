

class MarksProcessor:
    
    
    def __init__(self):
        self.student_marks = {}
    
    def add_student_marks(self, roll_no, subjects_marks):
       
        self.student_marks[roll_no] = subjects_marks
    
    def calculate_average(self, roll_no):
        
        if roll_no not in self.student_marks:
            return 0
        
        marks = self.student_marks[roll_no].values()
        return sum(marks) / len(marks) if marks else 0
    
    def calculate_total(self, roll_no):
        
        if roll_no not in self.student_marks:
            return 0
        
        return sum(self.student_marks[roll_no].values())
    
    def get_grade(self, average):
       
        if average >= 90:
            return 'A+'
        elif average >= 80:
            return 'A'
        elif average >= 70:
            return 'B+'
        elif average >= 60:
            return 'B'
        elif average >= 50:
            return 'C'
        elif average >= 40:
            return 'D'
        else:
            return 'F'
    
    def get_student_statistics(self, roll_no):
        if roll_no not in self.student_marks:
            return None
        
        average = self.calculate_average(roll_no)
        total = self.calculate_total(roll_no)
        grade = self.get_grade(average)
        
        return {
            'average': average,
            'total': total,
            'grade': grade,
            'subjects': self.student_marks[roll_no]
        }
    
    def get_highest_marks(self, roll_no):
       
        if roll_no not in self.student_marks:
            return None
        
        subjects = self.student_marks[roll_no]
        return max(subjects.items(), key=lambda x: x[1])
    
    def get_lowest_marks(self, roll_no):
       
        if roll_no not in self.student_marks:
            return None
        
        subjects = self.student_marks[roll_no]
        return min(subjects.items(), key=lambda x: x[1])

def calculate_class_average(marks_processor):
    
    all_averages = []
    for roll_no in marks_processor.student_marks.keys():
        all_averages.append(marks_processor.calculate_average(roll_no))
    
    return sum(all_averages) / len(all_averages) if all_averages else 0