from AdaStudent import AdaStudent


class Cohort:
    def __init__(self, cohort_code):
        self.cohort_code = cohort_code
        self.students = []  # List to store AdaStudent objects
    
    def add_student(self, student):
        if isinstance(student, AdaStudent):
            self.students.append(student)
            print(f"Added {student.name} to {self.cohort_code}")
        else:
            print("Can only add AdaStudent objects to cohort")
    
    def remove_student(self, student_name):
        for student in self.students:
            if student.name == student_name:
                self.students.remove(student)
                print(f"Removed {student_name} from {self.cohort_code}")
                return
        print(f"Student {student_name} not found in {self.cohort_code}")
    
    def list_students(self):
        if not self.students:
            return f"No students in {self.cohort_code}"
        
        result = f"Students in {self.cohort_code}:\n"
        for student in self.students:
            result += f"- {student.name} ({student.course})\n"
        return result
    
    def search_student(self, student_name):
        for student in self.students:
            if student.name.lower() == student_name.lower():
                return student
        return None
    
    def get_cohort_average(self):
        if not self.students:
            return 0
        
        total_average = 0
        students_with_grades = 0
        
        for student in self.students:
            avg = student.get_average_grade()
            if avg > 0:
                total_average += avg
                students_with_grades += 1
        
        return total_average / students_with_grades if students_with_grades > 0 else 0

# Create a cohort and add students
cohort1 = Cohort("DEV2024A")

student1 = AdaStudent("Emma Wilson", "12/03/2002", "Manchester", "STU001", "Software Development")
student2 = AdaStudent("James Brown", "08/11/2001", "London", "STU002", "Data Science")

# Test the functionality
print(student1.talk())  # Inherited from Person
print(student1.study())  # New method in AdaStudent

# Add some grades
student1.add_grade(85)
student1.add_grade(92)
student1.add_grade(78)

print(student1.get_student_info())


# Add our existing students
cohort1.add_student(student1)
cohort1.add_student(student2)

# Create and add more students to reach our goal of 10+ objects
student3 = AdaStudent("Sarah Davis", "25/07/2002", "Liverpool", "STU003", "Software Development")
student4 = AdaStudent("Michael Johnson", "14/12/2001", "Newcastle", "STU004", "Cybersecurity")

cohort1.add_student(student3)
cohort1.add_student(student4)

# Test the cohort functionality
print(cohort1.list_students())

# Add some grades to the new students
student3.add_grade(88)
student3.add_grade(91)
student4.add_grade(76)
student4.add_grade(84)
student4.add_grade(89)

print(f"Cohort average: {cohort1.get_cohort_average():.1f}")