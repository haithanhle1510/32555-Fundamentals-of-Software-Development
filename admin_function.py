from utils.file_operation import update_data_to_file, write_new_data_to_file, read_file_and_convert_to_list
from tabulate import tabulate

from utils.helpers import print_errors_message, print_sucessfuly_message


def view_all_students():
    studentList = read_file_and_convert_to_list('student.data')

    student_data = [[student['student_id'], student['name'], student['email']]
                    for student in studentList]

    headers = ["Student Id", "Student Name", "Email"]

    print(tabulate(student_data, headers, tablefmt="grid"))


def remove_student_by_id(student_id: str):
    studentList = read_file_and_convert_to_list('student.data')

    if any(student['student_id'] == student_id for student in studentList):
        newStudentList = [
            student for student in studentList if not student['student_id'] == student_id]
        print(*newStudentList)

        update_data_to_file("student.data", newStudentList)

        print_sucessfuly_message(
            f"Student {student_id} have been removed from the system.")
        return True
    else:
        print_errors_message(
            "This student_id does not exist. Please check again.")
