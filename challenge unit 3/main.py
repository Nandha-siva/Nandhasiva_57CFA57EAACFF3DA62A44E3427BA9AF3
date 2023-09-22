class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

students = [
    Student("Ajith", "A001", 3.9),
    Student("Bala", "B002", 3.7),
    Student("charen", "C003", 3.5),
    Student("Durai", "D004", 3.8),
]

sorted_students = sort_students(students)

for student in sorted_students:
    print(f"Name: {student.name},     Roll Number: {student.roll_number},    CGPA: {student.cgpa}")
  