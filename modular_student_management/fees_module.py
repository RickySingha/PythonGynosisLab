# fees_module.py
"""
Fee Management Module
Requirement 7: Separate module for fee management
"""

class FeeRecord:
    """Individual fee record"""
    
    def __init__(self, roll_no, total_fee, paid_fee):
        self.roll_no = roll_no
        self.total_fee = total_fee
        self.paid_fee = paid_fee
    
    def calculate_balance(self):
        """Calculate remaining fee balance"""
        return self.total_fee - self.paid_fee
    
    def calculate_paid_percentage(self):
        """Calculate percentage of fee paid"""
        if self.total_fee == 0:
            return 0
        return (self.paid_fee / self.total_fee) * 100
    
    def is_fully_paid(self):
        """Check if fee is fully paid"""
        return self.paid_fee >= self.total_fee
    
    def get_payment_status(self):
        """Get payment status"""
        if self.is_fully_paid():
            return "Paid"
        elif self.paid_fee > 0:
            return "Partial"
        else:
            return "Unpaid"

class FeeManager:
    """Manage fees for multiple students"""
    
    def __init__(self):
        self.fee_records = {}
    
    def add_fee_record(self, roll_no, total_fee, paid_fee):
        """Add fee record for a student"""
        record = FeeRecord(roll_no, total_fee, paid_fee)
        self.fee_records[roll_no] = record
    
    def make_payment(self, roll_no, amount):
        """Process a payment"""
        if roll_no in self.fee_records:
            self.fee_records[roll_no].paid_fee += amount
            return True
        return False
    
    def get_fee_record(self, roll_no):
        """Get fee record for a student"""
        return self.fee_records.get(roll_no)
    
    def display_fee_status(self, roll_no):
        """Display fee status for a student"""
        record = self.get_fee_record(roll_no)
        if record:
            balance = record.calculate_balance()
            percentage = record.calculate_paid_percentage()
            status = record.get_payment_status()
            
            print(f"  Total Fee: ₹{record.total_fee:.2f}")
            print(f"  Paid Fee: ₹{record.paid_fee:.2f}")
            print(f"  Balance: ₹{balance:.2f}")
            print(f"  Payment Status: {status} ({percentage:.2f}%)")
        else:
            print("  No fee record found")
    
    def get_defaulters(self):
        """Get list of students with unpaid fees"""
        defaulters = []
        for roll_no, record in self.fee_records.items():
            if not record.is_fully_paid():
                defaulters.append(roll_no)
        return defaulters
    
    def calculate_total_collected(self):
        """Calculate total fees collected"""
        return sum(record.paid_fee for record in self.fee_records.values())
    
    def calculate_total_pending(self):
        """Calculate total pending fees"""
        return sum(record.calculate_balance() for record in self.fee_records.values())