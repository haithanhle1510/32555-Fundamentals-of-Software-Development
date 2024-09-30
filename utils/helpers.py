import re
import json


def validate_email(email:str)->bool:
        """
        Args: email: str \n
        validates email i.e checks weather email ends with "@university.com"
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@university\.com$'
        return re.match(pattern, email) is not None


# Function to load student data from file
def load_student_data(filename='student.data'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist
    except json.JSONDecodeError:
        print("Error reading the student data file. Please check the file format.")
        return []

# Function to check registration
def check_registration(student_id, email, password, filename='student.data'):
    students = load_student_data(filename)
    
    for student in students:
        if (student['student_id'] == student_id and 
            student['email'] == email and 
            student['password'] == password):
            return True  # Registration is valid
    
    return False  # Registration not found

if __name__ == "__main__":
    student_id = input("Enter Student ID: ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    if check_registration(student_id, email, password):
        print("Registration is valid.")
    else:
        print("Invalid registration.")