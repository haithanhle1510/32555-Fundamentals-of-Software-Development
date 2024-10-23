from utils.helpers import print_errors_message, print_information_message, print_list_in_table
from utils.helpers import is_valid_password, print_errors_message, generate_hash_password, print_information_message, print_successful_message
import random
from utils.file_operation import read_file_and_convert_to_list, update_data_to_file


def update_password(student_id, new_password):
    studentList = read_file_and_convert_to_list('student.data')
    # Update password directly in dictionary
    for idx in range(len(studentList)):
        if studentList[idx]['student_id'] == student_id:
            studentList[idx]['password'] = generate_hash_password(new_password)

    # Write the new data to the file
    update_data_to_file('student.data', studentList)
    print_successful_message(f"Your password has been updated.")


def modify_password(student_id):
    while True:
        new_password = input(
            "Please enter a new password (requirements: start with a capital letter, at least 5 letters, followed by 3 or more numbers): ")

        if is_valid_password(new_password):
            update_password(student_id, new_password)
            break
        else:
            print_errors_message("Invalid password, please try again.")
            retry = input(
                "Would you like to try again? (Y/N): ").strip().upper()
            if retry == 'N':
                print_information_message("Exiting password modification.")
                return
            elif retry != 'Y':
                print_errors_message(
                    "Invalid input. Exiting password modification.")
                return


# Use a collection to store existing course IDs
existing_ids = set()

# Randomly generate course ID
def generate_subject_id():
    while True:
        subject_id = str(random.randint(1, 999)).zfill(
            3)  # Convert to string and fill with 3 digits
        if subject_id not in existing_ids:
            existing_ids.add(subject_id)  # Add a new ID to the collection
            return subject_id

# Generate ratings based on scores
def get_grade(score):
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

# Enroll subject function


def enrol_subjects(student_id):
    max_courses = 4
    studentList = read_file_and_convert_to_list('student.data')
    available_courses = [
        {"subject_name": "Math", "subject_id": generate_subject_id()},
        {"subject_name": "Science", "subject_id": generate_subject_id()},
        {"subject_name": "History", "subject_id": generate_subject_id()},
        {"subject_name": "Art", "subject_id": generate_subject_id()},
        {"subject_name": "Physics", "subject_id": generate_subject_id()},
        {"subject_name": "Chemistry", "subject_id": generate_subject_id()},
        {"subject_name": "English", "subject_id": generate_subject_id()},
        {"subject_name": "Programming", "subject_id": generate_subject_id()}
    ]

    for idx in range(len(studentList)):
        if studentList[idx]['student_id'] == student_id:
            if 'enrollment_list' not in studentList[idx]:
                studentList[idx]['enrollment_list'] = []

            existing_enrollment_list = studentList[idx]['enrollment_list']
            break

    if len(existing_enrollment_list) >= max_courses:
        print_errors_message(
            "You have already registered for the maximum number of courses.")
        return

    while len(existing_enrollment_list) < max_courses:
        select_course = random.choice(available_courses)

        if not any(course['subject_id'] == select_course['subject_id'] for course in existing_enrollment_list):
            mark = random.randint(25, 100)  # Randomly generate scores
            grade = get_grade(mark)  # Get ratings based on scores
            existing_enrollment_list.append({
                "subject_id": select_course["subject_id"],
                "subject_name": select_course["subject_name"],
                "mark": mark,
                "grade": grade
            })
            print(f"Registered course {select_course['subject_name']} ({
                  select_course['subject_id']}) with mark {mark} and grade {grade}.")

    # Update the new data to the file
    update_data_to_file('student.data', studentList)


def display_enrollment_list(student_id):
    studentList = read_file_and_convert_to_list('student.data')

    for idx in range(len(studentList)):
        if studentList[idx]['student_id'] == student_id:
            if 'enrollment_list' not in studentList[idx]:
                studentList[idx]['enrollment_list'] = []

            enrollment_list = studentList[idx]['enrollment_list']
            break

    if not enrollment_list:
        print_errors_message("You have not registered for any courses.")
        return

    print_information_message("ENROLLED SUBJECT:")
    headers = ["Subject ID", "Subject Name", "Mark", "Grade"]
    print_list_in_table(enrollment_list, headers)


# Delete enrollment feature
def delete_subject(student_id):
    studentList = read_file_and_convert_to_list('student.data')
    for idx in range(len(studentList)):
        if studentList[idx]['student_id'] == student_id:
            if 'enrollment_list' not in studentList[idx]:
                studentList[idx]['enrollment_list'] = []

            existing_enrollment_list = studentList[idx]['enrollment_list']
            break

    if not existing_enrollment_list:
        print_errors_message("You have no registered courses to delete.")
        return

    # Show enrolled subject
    print_information_message("ENROLLED SUBJECT:")
    headers = ["Subject ID", "Subject Name", "Mark", "Grade"]
    print_list_in_table(existing_enrollment_list, headers)
    # Print an existing subject ID
    print(f"Available subject IDs: {
          [enrollment_record['subject_id'] for enrollment_record in existing_enrollment_list]}")

    # Remove leading and trailing spaces
    subject_id = input("Enter the course ID to delete: ").strip()

    enrollment_record_found = False
    # Check if the subject ID exists
    for enrollment_record in existing_enrollment_list:
        if enrollment_record['subject_id'] == subject_id:
            existing_enrollment_list.remove(enrollment_record)
            enrollment_record_found = True
            print(
                f"Subject {subject_id}-{enrollment_record['subject_name']} deleted successfully from enrollment list.")
            update_data_to_file('student.data', studentList)  # Update data
            break  # Exit the loop after deletion

    if not enrollment_record_found:
        print_errors_message("Subject ID not found.")
