import random
from classes.Database import Database
from utils.helpers import generate_hash_password, is_valid_password, print_errors_message, print_information_message, print_list_in_table, print_successful_message
from .Subject import Subject


class User:
    def __init__(self, name: str, email: str, password: str) -> None:
        self.name = name
        self.email = email
        self.password = password


class Student(User):
    def __init__(self, name: str, email: str,  password: str, student_id: str, enrollment_list=[]) -> None:
        super().__init__(name, email, password)
        self.student_id: str = student_id
        self.enrollment_list = enrollment_list
        self.database = Database()

    def change_password(self) -> str:
        while True:
            new_password = input(
                "Please enter a new password (requirements: start with a capital letter, at least 5 letters, followed by 3 or more numbers): ")

            if is_valid_password(new_password):
                self.password = generate_hash_password(new_password)
                self.database.update_data_to_file(
                    'student.data', self.read_student_information())
                print_successful_message(f"Your password has been updated.")

                break
            else:
                print_errors_message("Invalid password, please try again.")
                retry = input(
                    "Would you like to try again? (Y/N): ").strip().upper()
                if retry == 'N':
                    print_information_message(
                        "Exiting password modification.")
                    return
                elif retry != 'Y':
                    print_errors_message(
                        "Invalid input. Exiting password modification.")
                    return

    def get_grade(self, score):
        if score < 50:
            return 'Z'
        elif 50 <= score < 65:
            return 'P'
        elif 65 <= score < 75:
            return 'C'
        elif 75 <= score < 85:
            return 'D'
        else:
            return 'HD'

    def enroll_subject(self):
        max_courses = 4
        available_subject = [
            Subject("001", "Math"),
            Subject("002", "Science"),
            Subject("003", "History"),
            Subject("004", "Art"),
            Subject("005", "Physics"),
            Subject("006", "Chemistry"),
            Subject("007", "English"),
            Subject("008", "Programming"),
        ]

        if len(self.enrollment_list) >= max_courses:
            print_errors_message(
                "You have already registered for the maximum number of subjects.")
            return

        if len(self.enrollment_list) < max_courses:
            select_subject = random.choice(
                available_subject).read_subject_detail()

            if not any(subject['subject_id'] == select_subject['subject_id'] for subject in self.enrollment_list):
                mark = random.randint(25, 100)  # Randomly generate scores
                grade = self.get_grade(mark)  # Get ratings based on scores
                self.enrollment_list.append({
                    "subject_id": select_subject["subject_id"],
                    "subject_name": select_subject["subject_name"],
                    "mark": mark,
                    "grade": grade
                })
                print(f"""Registered subject {select_subject['subject_name']} ({
                    select_subject['subject_id']})  with mark {mark} and grade {grade}.""")

        # Update the new data to the file
        self.database.update_data_to_file(
            'student.data', self.read_student_information())

    def view_enrollment_list(self):
        if len(self.enrollment_list) == 0:
            print_errors_message("You have not registered for any courses.")
            return

        print_information_message("ENROLLED SUBJECT:")
        headers = ["Subject ID", "Subject Name", "Mark", "Grade"]
        print_list_in_table(self.enrollment_list, headers)

    def read_student_information(self):
        return {
            'name': self.name,
            'email': self.email,
            'student_id': self.student_id,
            'password': self.password,
            'enrollment_list': self.enrollment_list
        }

    def remove_subject(self):
        existing_enrollment_list = self.enrollment_list
        if len(existing_enrollment_list) == 0:
            print_errors_message("You have not registered for any courses.")
            return

        # Show enrolled subject
        print_information_message("ENROLLED SUBJECT:")
        headers = ["Subject ID", "Subject Name", "Mark", "Grade"]
        print_list_in_table(existing_enrollment_list, headers)
        # Print an existing subject ID
        print(f"""Available subject IDs: {
            [enrollment_record['subject_id'] for enrollment_record in existing_enrollment_list]}""")

        # Remove leading and trailing spaces
        subject_id = input("Enter the course ID to delete: ").strip()

        enrollment_record_found = False
        # Check if the subject ID exists
        for enrollment_record in existing_enrollment_list:
            if enrollment_record['subject_id'] == subject_id:
                self.enrollment_list.remove(enrollment_record)
                enrollment_record_found = True
                print_successful_message(
                    f"Subject {subject_id}-{enrollment_record['subject_name']} deleted successfully from enrollment list.")
                self.database.update_data_to_file(
                    'student.data', self.read_student_information())  # Update data
                break  # Exit the loop after deletion

        if not enrollment_record_found:
            print_errors_message("Subject ID not found.")
