from utils.helpers import validate_email
from authentication import process_student_register


def main():
    while True:
        print("Please choose an option:")
        print("1) Go to student system")
        print("2) Go to admin system")
        print("3) Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("Navigating to student system...")
            student_system()
        elif choice == '2':
            print("Navigating to admin system...")
            admin_system()
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def student_system():
    while True:
        print("STUDENT SYSTEM")
        print("1) Log in")
        print("2) Register")
        print("3) Back to main menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("Student login...")
        elif choice == '2':
            print("Student register...")
        elif choice == '3':
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Please try again.")


def admin_system():
    while True:
        print("ADMIN SYSTEM")
        print("1) Log in")
        print("2) Back to main menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("Admin login...")
        elif choice == '2':
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
