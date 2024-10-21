import re
import json
import os
from utils.file_operation import read_file_and_convert_to_list
def validate_password(password):
    """
   Verify that the password meets the requirements:
    (i) starts with a capital letter,
    (ii) contains at least five letters,
    (iii) followed by three or more numbers.
    """
    pattern = r'^[A-Z][a-zA-Z]{4,}\d{3,}$'  # ^[A-Z]Cap Letter  [a-zA-Z]{4,} 4+Letters \d{3,} 3+Numbers
    return bool(re.match(pattern, password))

def update_password(student_id, new_password):
    """
    Modify the student's password, or update the password if the student exists.
    """
    studentList = read_file_and_convert_to_list('student.data')
    studentList[student_id]['password'] = new_password  # Update password directly in dictionary
    
    print(f"Password for student {student_id} has been updated.")


def modify_password(student_id):
    """
   Allow the user to enter a new password, which is then verified and updated in the student.data file.
    """
    while True:
        new_password = input("Please enter a new password (requirements: start with a capital letter, at least 5 letters, followed by 3 or more numbers): ")
        
         # Check if the user wants to log out
        if new_password.lower() == 'exit':
            print("Exit password modification.")
            return  
        
    
        if validate_password(new_password):
            print("Password is valid! Modification successful.")
            update_password(student_id, new_password)
            break
        else:
            print("Invalid password, please try again.")
            return 
 