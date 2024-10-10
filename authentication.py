from utils.helpers import validate_email, is_valid_password
from utils.file_operation import write_new_data_to_file, read_file_and_convert_to_list
from classes.User import Student


def process_student_register():
    print("Student register")
    is_registered_sucessfully = False
    while True:
        email = input("Please enter your email: ")
        is_email_existed(email)
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
