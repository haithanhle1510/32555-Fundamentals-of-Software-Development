from authentication import process_student_register, process_student_login
from utils.helpers import print_errors_message, print_sucessfuly_message, print_infomation_message, print_option_message
from colorama import Fore, Back, Style
from classes.User import Student


def main():
    while True:
        print_infomation_message("Please choose an option:")
        print_option_message("  1) Go to student system")
        print_option_message("  2) Go to admin system")
        print_option_message("  3) Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print_infomation_message("Navigating to student system...")
            student_system()
        elif choice == '2':
            print_infomation_message("Navigating to admin system...")
            admin_system()
        elif choice == '3':
            print_infomation_message("Exiting the system. Goodbye!")
            break
        else:
            print_errors_message("Invalid choice. Please try again.")


def student_system():
    while True:
        print_infomation_message("STUDENT SYSTEM")
        print_option_message("  1) Log in")
        print_option_message("  2) Register")
        print_option_message("  3) Back to main menu")

        choice = input("Enter your choice: ")
        is_user_authed = False
        student_info = False

        if choice == '1':
            login_result = process_student_login()
            is_user_authed = login_result['is_login_sucessfully']
            student_info = login_result['student']
            print(student_info)

        elif choice == '2':
            register_result = process_student_register()
            is_user_authed = register_result['is_registered_sucessfully']
            student_info = register_result['student']

        elif choice == '3':
            print_infomation_message("Returning to main menu...")
            break
        else:
            print_errors_message("Invalid choice. Please try again.")

        if is_user_authed == True:
            student = Student(
                student_info['name'], student_info['email'], student_info['password'], student_info['student_id'])
            student_system_menu(student)


def admin_system():
    while True:
        print_infomation_message("ADMIN SYSTEM")
        print_option_message("  1) Log in")
        print_option_message("  2) Back to main menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            print_infomation_message("Admin login...")
        elif choice == '2':
            print_infomation_message("Returning to main menu...")
            break
        else:
            print_errors_message("Invalid choice. Please try again.")


def student_system_menu(student: Student):
    while True:
        print_infomation_message("STUDENT SYSTEM MENU")
        print_option_message("  1) Change password")
        print_option_message("  2) Enrol in subject")
        print_option_message("  3) Remove a subject")
        print_option_message("  4) Show enrolled subject")
        print_option_message("  5) Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print_infomation_message("Change password...")
        elif choice == '2':
            print_infomation_message("Enrol in subject...")
        elif choice == '3':
            print_infomation_message("Remove a subject...")
        elif choice == '4':
            print_infomation_message("Show enrolled subject...")
        elif choice == '5':
            print_infomation_message("Exitting...")
            break
        else:
            print_errors_message("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
