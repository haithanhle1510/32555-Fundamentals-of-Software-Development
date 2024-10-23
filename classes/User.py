from typing import List
from .Subject import Subject


class User:
    def __init__(self, name: str, email: str, password: str) -> None:
        self.name = name
        self.email = email
        self.password = password


class Student(User):
    def __init__(self, email: str, password: str,  name: str, student_id: str, enrollment_list=[]) -> None:
        super().__init__(name, email, password)
        self.student_id: str = student_id
        self.enrollment_list = enrollment_list

    def change_password(self, new_password: str) -> str:
        # Password change logic here
        self.password = new_password

    def enroll_subject(self, subject: List[str]) -> List[str]:
        self.enrollment_list.append(subject)

    def remove_subject(self, subject: List[str]) -> List[str]:
        self.enrollment_list.remove(subject)

    def view_enrollment_list(self) -> List[str]:
        return self.enrollment_list

    def read_student_information(self):
        return {
            'name': self.name,
            'email': self.email,
            'student_id': self.student_id,
            'password': self.password,
            'enrollment_list': self.enrollment_list
        }
