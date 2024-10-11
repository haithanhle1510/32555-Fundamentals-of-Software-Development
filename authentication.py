from utils.helpers import validate_email, is_valid_password
from utils.file_operation import write_new_data_to_file, read_file_and_convert_to_list
from classes.User import Student


def process_student_register():
    print("Student register")
    is_registered_sucessfully = False
    while True:
        email = input("Please enter your email: ")
        if is_email_existed(email) == False:
            password = input("Please enter your password: ")

            if validate_email(email) is False:
                {
                    print(
                        "Something went wrong with your email, please re-enter, make sure your email is correctly formatted")
                }
            if is_valid_password(password) is False:
                {
                    print(
                        "Something went wrong with your password, please re-enter, make sure your email is correctly formatted")
                }
            else:
                name = input("Please enter name: ")
                print("Successfully registered")
                post_student_register(email, password, name)
                is_registered_sucessfully = True
                break
            retry = input("Do you want to try again?(Y/N):")
            if retry == "N":
                break
        else:
            print("Email already exists")
            retry = input("Do you want to try again?(Y/N):")
            if retry == "N":
                break
    return is_registered_sucessfully


def post_student_register(email, password, name):
    student = Student(name, email, password, )
    write_new_data_to_file('student.data', student.read_student_informations())


def is_email_existed(email):
    studentList = read_file_and_convert_to_list('student.data')
    for student in studentList:
        if student['email'] == email:
            return True  # Account already exists

    return False  # Account not found


def process_student_login():
    print("Student login")
    is_login_sucessfully = False
    while True:
        email = input("Please enter your email: ")
        password = input("Please enter your password: ")
        if is_email_existed(email) == False:
            print("Your email not exists, please try again or register new account.")

            retry = input("Do you want to try again?(Y/N):")
            if retry == "N":
                break
        else:
            if (validate_student_account(email, password)) == False:
                print("Incorrect password, please try again.")

                retry = input("Do you want to try again?(Y/N):")
                if retry == "N":
                    break
            else:
                print("Successfully logged in")
                is_login_sucessfully = True
                break

    return is_login_sucessfully


def validate_student_account(email, password):
    studentList = read_file_and_convert_to_list('student.data')
    for student in studentList:
        if student['email'] == email and student['password'] == password:
            return True  # Account is valid
    return False  # Account is invalid
