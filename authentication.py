from utils.helpers import validate_email, is_valid_password, print_errors_message, print_sucessfuly_message, print_infomation_message, generate_new_student_id
from utils.file_operation import write_new_data_to_file, read_file_and_convert_to_list
from classes.User import Student


def process_student_register():
    print_infomation_message("Student register")
    is_registered_sucessfully = False
    while True:
        email = input("Please enter your email: ")
        if is_email_existed(email) == False:
            password = input("Please enter your password: ")

            if validate_email(email) is False:
                {
                    print_errors_message(
                        "Something went wrong with your email, please re-enter, make sure your email is correctly formatted")
                }
            if is_valid_password(password) is False:
                {
                    print_errors_message(
                        "Something went wrong with your password, please re-enter, make sure your email is correctly formatted")
                }
            else:
                name = input("Please enter name: ")
                print_sucessfuly_message("Successfully registered")
                student = post_student_register(email, password, name)
                is_registered_sucessfully = True
                break
            retry = input("Do you want to try again?(Y/N):")
            if retry == "N":
                break
        else:
            print_errors_message("Email already exists")
            retry = input("Do you want to try again?(Y/N):")
            if retry == "N":
                break
    return {
        'is_registered_sucessfully': is_registered_sucessfully,
        'student': student
    }


def post_student_register(email, password, name):
    student = Student(email, password, name, generate_new_student_id())
    write_new_data_to_file('student.data', student.read_student_informations())
    return student.read_student_informations()


def is_email_existed(email):
    studentList = read_file_and_convert_to_list('student.data')
    for student in studentList:
        if student['email'] == email:
            return True  # Account already exists

    return False  # Account not found


def process_student_login():
    print_infomation_message("Student login")
    while True:
        email = input("Please enter your email: ")
        password = input("Please enter your password: ")
        if is_email_existed(email) == False:
            print_errors_message(
                "Your email not exists, please try again or register new account.")

            retry = input("Do you want to try again?(Y/N):")
            if retry == "N":
                break
        else:
            validated_result = validate_student_account(email, password)
            if (validated_result['account_valid']) == False:
                print_errors_message("Incorrect password, please try again.")

                retry = input("Do you want to try again?(Y/N):")
                if retry == "N":
                    break
            else:
                print_sucessfuly_message("Successfully logged in")
                break

    return {
        'is_login_sucessfully': validated_result['account_valid'],
        'student': validated_result['student'],
    }


def validate_student_account(email, password):
    studentList = read_file_and_convert_to_list('student.data')
    studentFound = False
    for student in studentList:
        if student['email'] == email and student['password'] == password:
            # Account is valid
            studentFound = student
    if studentFound == False:
        return {
            'account_valid': False,
            'student': studentFound
        }
    else:
        return {
            'account_valid': True,
            'student': studentFound
        }
