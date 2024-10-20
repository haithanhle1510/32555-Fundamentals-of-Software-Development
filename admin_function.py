from utils.file_operation import write_new_data_to_file, read_file_and_convert_to_list
from tabulate import tabulate


def view_all_students():
    studentList = read_file_and_convert_to_list('student.data')

    student_data = [[student['student_id'], student['name'], student['email']]
                    for student in studentList]

    headers = ["Student Id", "Student Name", "Email"]

    print(tabulate(student_data, headers, tablefmt="grid"))
