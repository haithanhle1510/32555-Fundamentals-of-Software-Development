from classes.Database import Database
from utils.helpers import print_errors_message, print_information_message, print_list_in_table, print_successful_message


def view_all_students():
    database = Database()
    studentList = database.read_file_and_convert_to_list('student.data')

    student_data = [{'student_id': student['student_id'], 'name': student['name'], 'email': student['email']}
                    for student in studentList]

    headers = ["Student Id", "Student Name", "Email"]

    print_list_in_table(student_data, headers)


def remove_student_by_id(student_id: str):
    database = Database()
    studentList = database.read_file_and_convert_to_list('student.data')

    if any(student['student_id'] == student_id for student in studentList):
        database.remove_data_from_file('student.data', student_id)

        print_successful_message(
            f"Student {student_id} have been removed from the system.")
        return True
    else:
        print_errors_message(
            "This student_id does not exist. Please check again.")


def get_students_by_grade():
    database = Database()
    studentList = database.read_file_and_convert_to_list('student.data')

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
                'student_email': student['email'],
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

    headers = ["Student Id", "Student Name", "Student Email",
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
    database = Database()
    studentList = database.read_file_and_convert_to_list('student.data')

    student_enrolled = [
        student for student in studentList if len(student['enrollment_list']) > 0
    ]
    fail_students = []
    pass_students = []
    
  # Only select students who are registered for the course
    student_enrolled = [student for student in studentList if len(student['enrollment_list']) > 0]

    fail_students = []
    pass_students = []

    for student in student_enrolled:
        marks = []  
        all_passed = True  # Assuming that the student passes all courses
        failed_courses = []  
        
        # Check each course of the student
        for enrollment_record in student['enrollment_list']:
            mark = enrollment_record['mark']
            marks.append(mark)
            
            # If any course score is below 50, set it to fail
            if mark < 50:
                all_passed = False
                failed_courses.append([
                    student['student_id'], 
                    student['name'], 
                    student['email'], 
                    enrollment_record['subject_name'], 
                    enrollment_record['mark'], 
            ])
        
        # Calculate average score
        average_mark = sum(marks) / len(marks)
        def calculate_grade(score):
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
        
        
        if all_passed:
            
            pass_students.append([
                student['student_id'], 
                student['name'], 
                student['email'], 
                average_mark, 
                calculate_grade(average_mark)
            ])
        else:
            # Record the failed course information
            fail_students.extend(failed_courses)
            
    
    # Defines the mapping between column names and dictionary keys
    keys_pass = ["student_id", "name", "email", "average_mark", "overall_grade"]
    keys_fail = ["student_id", "name", "email", "mark", "grade"]
    # Convert a 2D list to a list of dictionaries
    pass_students_dict = [dict(zip(keys_pass, student)) for student in pass_students]
    fail_students_dict = [dict(zip(keys_fail, student)) for student in fail_students]    
    headers_pass = ["Student Id", "Student Name", "Student Email", "Average Mark", "Overall Grade"]
    headers_fail = ["Student Id", "Student Name", "Student Email", "Subject Name", "Mark"]

    # old headers = ["Student Id", "Student Name", "Student Email", "Subject Name", "Mark", 'Grade']

    print_successful_message("PASS STUDENT:")
    if (len(pass_students) > 0):
        print_list_in_table(pass_students_dict, headers_pass)
    else:
        print_information_message("  NOTHING TO SHOW \n")

    print_errors_message("FAIL STUDENT:")
    if (len(fail_students) > 0):
        print_list_in_table(fail_students_dict, headers_fail)
    else:
        print_information_message("  NOTHING TO SHOW \n")
