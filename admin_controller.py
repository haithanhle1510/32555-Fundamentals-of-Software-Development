from utils.file_operation import update_data_to_file, read_file_and_convert_to_list
from utils.helpers import print_errors_message, print_information_message, print_list_in_table, print_successful_message


def view_all_students():
    studentList = read_file_and_convert_to_list('student.data')

    student_data = [{'student_id': student['student_id'], 'name': student['name'], 'email': student['email']}
                    for student in studentList]

    headers = ["Student Id", "Student Name", "Email"]

    print_list_in_table(student_data, headers)


def remove_student_by_id(student_id: str):
    studentList = read_file_and_convert_to_list('student.data')

    if any(student['student_id'] == student_id for student in studentList):
        newStudentList = [
            student for student in studentList if not student['student_id'] == student_id]

        update_data_to_file("student.data", newStudentList)

        print_successful_message(
            f"Student {student_id} have been removed from the system.")
        return True
    else:
        print_errors_message(
            "This student_id does not exist. Please check again.")


def get_students_by_grade():
    studentList = read_file_and_convert_to_list('student.data')

    student_enrolled = [
        student for student in studentList if len(student['enrollment_list']) > 0]

    z_mark_student = []
    p_mark_student = []
    c_mark_student = []
    d_mark_student = []
    hd_mark_student = []

    for student in student_enrolled:
        for enrollment_record in student['enrollment_list']:
            student_record_with_enrollment_details = {
                'student_id': student['student_id'],
                'student_name': student['name'],
                'subject_name': enrollment_record['subject_name'],
                'mark': enrollment_record['mark'],
                'grade': enrollment_record['grade'],
            }

            if enrollment_record['grade'] == 'Z':
                z_mark_student.append(student_record_with_enrollment_details)
            elif enrollment_record['grade'] == 'P':
                p_mark_student.append(student_record_with_enrollment_details)
            elif enrollment_record['grade'] == 'C':
                c_mark_student.append(student_record_with_enrollment_details)
            elif enrollment_record['grade'] == 'D':
                d_mark_student.append(student_record_with_enrollment_details)
            elif enrollment_record['grade'] == 'HD':
                hd_mark_student.append(student_record_with_enrollment_details)

    headers = ["Student Id", "Student Name",
               "Subject Name", "Mark", 'Grade']

    print("Z GRADE: \n")
    if (len(z_mark_student) > 0):
        print_list_in_table(z_mark_student, headers)
    else:
        print_information_message("  NOTHING TO SHOW \n")

    print("P GRADE: \n")
    if (len(p_mark_student) > 0):
        print_list_in_table(p_mark_student, headers)
    else:
        print_information_message("  NOTHING TO SHOW \n")

    print("C GRADE: \n")
    if (len(c_mark_student) > 0):
        print_list_in_table(c_mark_student, headers)
    else:
        print_information_message("  NOTHING TO SHOW \n")

    print("D GRADE: \n")
    if (len(d_mark_student) > 0):
        print_list_in_table(d_mark_student, headers)
    else:
        print_information_message("  NOTHING TO SHOW \n")

    print("HD GRADE: \n")
    if (len(hd_mark_student) > 0):
        print_list_in_table(hd_mark_student, headers)
    else:
        print_information_message("  NOTHING TO SHOW \n")


def categorise_student():
    studentList = read_file_and_convert_to_list('student.data')

    student_enrolled = [
        student for student in studentList if len(student['enrollment_list']) > 0
    ]
    fail_students = []
    pass_students = []

    for student in student_enrolled:
        for enrollment_record in student['enrollment_list']:
            student_record_with_enrollment_details = {
                'student_id': student['student_id'],
                'student_name': student['name'],
                'subject_name': enrollment_record['subject_name'],
                'mark': enrollment_record['mark'],
                'grade': enrollment_record['grade'],
            }

            if enrollment_record['mark'] >= 50:
                pass_students.append(student_record_with_enrollment_details)
            else:
                fail_students.append(student_record_with_enrollment_details)

    headers = ["Student Id", "Student Name",
               "Subject Name", "Mark", 'Grade']

    print_successful_message("PASS STUDENT: \n")
    if (len(pass_students) > 0):
        print_list_in_table(pass_students, headers)
    else:
        print_information_message("  NOTHING TO SHOW \n")

    print_errors_message("FAIL STUDENT: \n")
    if (len(fail_students) > 0):
        print_list_in_table(fail_students, headers)
    else:
        print_information_message("  NOTHING TO SHOW \n")
