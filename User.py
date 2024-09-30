from typing import List
from utils.helpers import validate_email
from .Subject import Subject

class User:
    def __init__(self, name:str, email:str, password:str)-> None:
        self.name = name
        self.email = email
        self.password = password

    def login(self, email:str, password:str):
        if self.email == email and self.password == password:
            return True
        else:
            return False

class Student(User):
    def __init__(self, name:str, email:str, password:str, student_id:int)-> None:
        super().__init__(name, email, password)
        self.student_id:int = student_id
        self.enrollment_list:List[str] = []

    def register(self):
        # Registration logic here
        pass

    def change_password(self, new_password:str)->str:
        # Password change logic here
        self.password = new_password

    def enroll_subject(self, subject:List[str])->List[str]:
        self.enrollment_list.append(subject)

    def remove_subject(self, subject:List[str])->List[str]:
        self.enrollment_list.remove(subject)

    def view_enrollment_list(self)->List[str]:
        return self.enrollment_list

class Admin(User):
    def __init__(self, name, email, password, employee_id):
        super().__init__(name, email, password)
        self.employee_id = employee_id

    def view_all_students(self, students):
        return students

    def view_students_by_grade(self, students, grade):
        return [student for student in students if student.grade == grade]

    def categorize_students(self, students):
        pass_students = [student for student in students if student.grade >= 50]
        fail_students = [student for student in students if student.grade < 50]
        return pass_students, fail_students

    def remove_student(self, students, student_id):
        return [student for student in students if student.student_id != student_id]

    def clear_data(self):
        pass


        
        

# Test Case
if __name__ == "__main__":
    student1 = Student("John Doe", "john.doe@university.com", "Password123", "000001")
    subject1 = Subject("001", "Data Structures", "Spring")
    student1.enroll_subject(subject1)
    print(student1.view_enrollment_list())