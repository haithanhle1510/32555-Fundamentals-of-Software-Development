import re
import random
from utils.file_operation import read_file_and_convert_to_list


def validate_email(email: str) -> bool:
    """
    Args: email: str \n
    validates email i.e checks weather email ends with "@university.com"
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@university\.com$'
    return re.match(pattern, email) is not None


def is_valid_password(password):
    # Check if the password starts with an upper-case character
    if not password[0].isupper():
        return False

    # Check if the password contains at least five letters
    letters = re.findall(r'[A-Za-z]', password)
    if len(letters) < 5:
        return False

    # Check if the password ends with three or more digits
    digits = re.findall(r'\d+', password)
    if not digits or len(digits[-1]) < 3:
        return False

    return True


def generate_new_student_id() -> str:
    existing_ids = list(
        map(lambda student: student['student_id'], read_file_and_convert_to_list('student.data')))
    while True:
        student_id = random.randint(1, 999999)
        # Convert to six digits with leading zeros if necessary
        student_id_str = f'{student_id:06}'

        # Ensure the ID is unique
        if student_id_str not in existing_ids:
            break

    return student_id_str
