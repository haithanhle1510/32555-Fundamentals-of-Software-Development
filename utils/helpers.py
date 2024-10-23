import re
import random
import bcrypt
from tabulate import tabulate
from classes.Database import Database
from colorama import Fore


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
    database = Database()
    existing_ids = list(
        map(lambda student: student['student_id'], database.read_file_and_convert_to_list('student.data')))
    while True:
        student_id = random.randint(1, 999999)
        # Convert to six digits with leading zeros if necessary
        student_id_str = f'{student_id:06}'

        # Ensure the ID is unique
        if student_id_str not in existing_ids:
            break

    return student_id_str


def generate_hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


def validate_password(password: str, hashPassword: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashPassword.encode('utf-8'))


def print_errors_message(content):
    print(f"{Fore.RED} {content}{Fore.RESET} \n")


def print_successful_message(content):
    print(f"{Fore.GREEN} {content}{Fore.RESET} \n")


def get_warning_message(content):
    return (f"{Fore.YELLOW} {content}{Fore.RESET} \n")


def print_information_message(content):
    print(f"{Fore.BLUE} {content}{Fore.RESET}")


def print_option_message(content):
    print(f"{Fore.MAGENTA} {content}{Fore.RESET}")


def print_list_in_table(list, headers):
    rows = [element.values() for element in list]
    print(tabulate(rows, headers, tablefmt="grid"))
    print('\n')
