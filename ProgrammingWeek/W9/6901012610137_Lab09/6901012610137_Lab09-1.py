class Person:
    def __init__(self, name, address, weight, height):
        self.name = name
        self.address = address
        self.weight = weight      # กิโลกรัม
        self.height = height      # เซนติเมตร
 
    def getBMI(self):
        h_m = self.height / 100   # แปลงเป็นเมตร
        return self.weight / (h_m * h_m)
 
    def show(self):
        print("ชื่อ:", self.name)
        print("ที่อยู่:", self.address)
        print("น้ำหนัก:", self.weight, "kg")
        print("ส่วนสูง:", self.height, "cm")
 
 
class Student(Person):
    def __init__(self, name, address, weight, height, student_id, course, gpa):
        super().__init__(name, address, weight, height)
        self.student_id = student_id
        self.course = course
        self.gpa = gpa
 
    def show(self):
        super().show()                       # เรียก show() ของคลาสแม่
        print("รหัสนักเรียน:", self.student_id)
        print("หลักสูตร:", self.course)
        print("GPA:", self.gpa)
        print("BMI: %.2f" % super().getBMI())  # เรียก getBMI() ของคลาสแม่
 
 
class Employee(Person):
    def __init__(self, name, address, weight, height, employee_id, department, salary):
        super().__init__(name, address, weight, height)
        self.employee_id = employee_id
        self.department = department
        self.salary = salary
 
    def show(self):
        super().show()
        print("รหัสพนักงาน:", self.employee_id)
        print("แผนก:", self.department)
        print("เงินเดือน:", self.salary)
        print("BMI: %.2f" % super().getBMI())

s = Student("สมชาย", "กรุงเทพ", 60, 170, "6601", "Programming", 3.5)
e = Employee("สมหญิง", "ปทุมธานี", 50, 160, "E001", "IT", 30000)
s.show()
print()
e.show()
#6901012610137
#lab09-1