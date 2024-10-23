from authentication_controller import process_student_register, process_student_login
from admin_controller import categorise_student, get_students_by_grade, remove_student_by_id, view_all_students
from utils.helpers import print_errors_message, print_successful_message, get_warning_message, print_information_message, print_option_message
from classes.User import Student
from classes.Database import Database


def main():
    while True:
        print_information_message("Please choose an option:")
        print_option_message("  1) Go to student system")
        print_option_message("  2) Go to admin system")
        print_option_message("  3) Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print_information_message("Navigating to student system...")
            student_system()
        elif choice == '2':
            print_information_message("Navigating to admin system...")
            admin_system()
        elif choice == '3':
            print_information_message("Exiting the system. Goodbye!")
            break
        else:
            print_errors_message("Invalid choice. Please try again.")


def student_system():
    while True:
        print_information_message("STUDENT SYSTEM")
        print_option_message("  1) Log in")
        print_option_message("  2) Register")
        print_option_message("  3) Back to main menu")

        choice = input("Enter your choice: ")
        is_user_authed = False
        student_info = False

        if choice == '1':
            login_result = process_student_login()
            is_user_authed = login_result['is_login_successfully']
            student_info = login_result['student']

        elif choice == '2':
            register_result = process_student_register()
            is_user_authed = register_result['is_registered_successfully']
            student_info = register_result['student']

        elif choice == '3':
            print_information_message("Returning to main menu...")
            break
        else:
            print_errors_message("Invalid choice. Please try again.")

        if is_user_authed == True:
            student = Student(
                student_info['name'],
                student_info['email'],
                student_info['password'],
                student_info['student_id'],
                student_info['enrollment_list']
            )
            student_system_menu(student)


def admin_system():
    while True:
        database = Database()
        print_information_message("ADMIN SYSTEM")
        print_option_message("  1) Clear database")
        print_option_message("  2) View all students")
        print_option_message("  3) Get students by grade")
        print_option_message("  4) Categories students by PASS/FAIL")
        print_option_message("  5) Remove students by id")
        print_option_message("  6) Back to main menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            choice = input(get_warning_message(
                "Are you sure to clear system's data?(Y/N):"))
            if choice == 'Y':
                database.clear_file('student.data')
                print_successful_message("System's data has been cleared.")
        elif choice == '2':
            print_information_message("View all students...")
            view_all_students()
        elif choice == '3':
            print_information_message("Get students by grade...")
            get_students_by_grade()
        elif choice == '4':
            print_information_message("Categories students by PASS/FAIL...")
            categorise_student()
        elif choice == '5':
            print_information_message("Remove students by id...")
            print_information_message("STUDENTS LISTS")
            view_all_students()
            while True:
                student_id = input("Enter student id to remove: ")
                choice = input(get_warning_message(
                    "Are you sure to remove this student?(Y/N):"))
                if choice == 'Y':
                    remove_successful = remove_student_by_id(student_id)
                    if remove_successful:
                        break
                    else:
                        retry = input("Do you want to try again?(Y/N):")
                        if retry == "N":
                            break
                else:
                    print_information_message("Back to menu")
                    break

        elif choice == '6':
            print_information_message("Returning to main menu...")
            break
        else:
            print_errors_message("Invalid choice. Please try again.")


def student_system_menu(student: Student):
    while True:
        print_information_message("STUDENT SYSTEM MENU")
        print_option_message("  1) Change password")
        print_option_message("  2) Enrol in subject")
        print_option_message("  3) Remove a subject")
        print_option_message("  4) Show enrolled subject")
        print_option_message("  5) Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print_information_message("Change password...")
            student.change_password()
        elif choice == '2':
            print_information_message("Enrol in subject...")
            student.enroll_subject()
        elif choice == '3':
            print_information_message("Remove a subject...")
            student.remove_subject()
        elif choice == '4':
            print_information_message("Show enrolled subject...")
            student.view_enrollment_list()
        elif choice == '5':
            print_information_message("Exiting...")
            break
        else:
            print_errors_message("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
