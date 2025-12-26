

class AttendanceRecord:
    
    
    def __init__(self, roll_no, present_days, total_days):
        self.roll_no = roll_no
        self.present_days = present_days
        self.total_days = total_days
    
    def calculate_percentage(self):
        
        if self.total_days == 0:
            return 0
        return (self.present_days / self.total_days) * 100
    
    def get_status(self):
        
        percentage = self.calculate_percentage()
        if percentage >= 75:
            return "Good"
        elif percentage >= 50:
            return "Average"
        else:
            return "Poor"

class AttendanceTracker:
    
    
    def __init__(self):
        self.attendance_records = {}
    
    def mark_attendance(self, roll_no, present_days, total_days):
        
        record = AttendanceRecord(roll_no, present_days, total_days)
        self.attendance_records[roll_no] = record
    
    def get_attendance(self, roll_no):
        
        return self.attendance_records.get(roll_no)
    
    def display_attendance(self, roll_no):
        
        record = self.get_attendance(roll_no)
        if record:
            percentage = record.calculate_percentage()
            status = record.get_status()
            print(f"  Attendance: {record.present_days}/{record.total_days} days")
            print(f"  Percentage: {percentage:.2f}%")
            print(f"  Status: {status}")
        else:
            print("  No attendance record found")
    
    def get_low_attendance_students(self, threshold=75):
        
        low_attendance = []
        for roll_no, record in self.attendance_records.items():
            if record.calculate_percentage() < threshold:
                low_attendance.append(roll_no)
        return low_attendance