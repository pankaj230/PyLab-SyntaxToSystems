# ===============================================================================
# LAB: Task 3 Extension challenge
# Create a class called Student with:
#  Attributes: name, age, grades (a list).
#  Methods:
# add_grade(grade)
# average_grade()
# display_info()
# Try to create 3 students, add grades, and print their average.
# ===============================================================================


# --- Program Execution ---
print("\n" + "╔" + "═" * 12 + " STUDENT DASHBOARD " + "═" * 11 + "╗")

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def add_grade(self, grades):
        return self.grades.append(grades)

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        print(f"Hello {self.name}, Your Grade is {self.average_grade()}")

student_list=[
    Student('Jake', 20, [10, 20, 30]),
    Student('Loki', 20, [15, 25, 35]),
    Student('Bill', 20, [60, 70, 30]),
]

for student in student_list:
    student.display_info()