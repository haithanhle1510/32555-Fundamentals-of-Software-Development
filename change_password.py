from utils.file_operation import read_file_and_convert_to_list, update_data_to_file
from utils.helpers import is_valid_password, print_errors_message, print_infomation_message, print_sucessfuly_message, generate_hash_password


def update_password(student_id, new_password):
    studentList = read_file_and_convert_to_list('student.data')
    # Update password directly in dictionary
    for idx in range(len(studentList)):
        if studentList[idx]['student_id'] == student_id:
            studentList[idx]['password'] = generate_hash_password(new_password)

    # Write the new data to the file
    update_data_to_file('student.data', studentList)
    print_sucessfuly_message(f"Your password has been updated.")


def modify_password(student_id):
    """
   Allow the user to enter a new password, which is then verified and updated in the student.data file.
    """
    while True:
        new_password = input(
            "Please enter a new password (requirements: start with a capital letter, at least 5 letters, followed by 3 or more numbers): ")

        # Check if the user wants to log out
        
        if is_valid_password(new_password):
            update_password(student_id, new_password)
            break
        else:
            print_errors_message("Invalid password, please try again.")
            retry = input("Would you like to try again? (Y/N): ").strip().upper()
            if retry == 'N':
                print_infomation_message("Exiting password modification.")
                return  # 退出密码修改
            elif retry != 'Y':
                print_errors_message("Invalid input. Exiting password modification.")
                return  # 处理无效输入，直接退出
