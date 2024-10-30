import math
import random
from tkinter import messagebox
import tkinter as tk
from tkinter import *
from GUI.utils.helpers import clear_window
from authentication_controller import is_email_existed, post_student_register, validate_student_account
from classes.Subject import Subject
from classes.Database import Database
from GUI.view.component import exit_button, menu_label, information_label, option_button, table
from classes.User import Student
from utils.helpers import generate_hash_password, is_valid_password, validate_email


def show_main_menu():
    clear_window(root)
    menu = tk.Frame(root)
    menu.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    menu_label(menu, "MAIN MENU")
    information_label(menu, "Welcome to university system"),
    information_label(menu, "Please choose your system")

    button_frame_top = tk.Frame(menu)
    button_frame_top.pack(pady=10, anchor="center")

    tk.Button(button_frame_top, text="Student System", bg='black', fg='white', font='Helvetica 14',
              command=show_student_authentication_menu, height=2).pack(side="left")
    tk.Button(button_frame_top, text="Admin System", bg='black', fg='white', font='Helvetica 14',
              command=show_admin_menu, height=2).pack(side="left")

    tk.Button(menu, text="Exit", bg='red', fg='white', font='Helvetica 14', command=confirm_exit, width=12, height=2).pack(
        pady=10, anchor="center")


def show_student_authentication_menu():
    clear_window(root)
    menu = tk.Frame(root)
    menu.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    menu_label(menu, "STUDENT MENU")
    information_label(menu, "Welcome to student system")
    information_label(menu, "Please choose your options")
    option_button(menu, "Log in", show_student_login_screen)
    option_button(menu, "Register", show_student_register)
    exit_button(menu, "Back to Main Menu", show_main_menu)


def show_admin_menu():
    clear_window(root)
    menu = tk.Frame(root)
    menu.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    menu_label(menu, "ADMIN MENU")
    information_label(menu, "Welcome to student system")
    information_label(menu, "Please choose your options")
    option_button(menu, "Clear Database", clear_database)
    option_button(menu, "View All Students", view_all_students)
    option_button(menu, "Get Students by Grade", get_students_by_grade)
    option_button(menu, "Categorize Students by PASS/FAIL",
                  categorize_students)
    option_button(menu, "Remove Students by ID", remove_student_by_id)
    exit_button(menu, "Back to Main Menu", show_main_menu)


def confirm_exit():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()


def show_student_login_screen():
    clear_window(root)
    menu = tk.LabelFrame(root, text='Log In', bg='#607b8d',
                         fg='white', padx=20, pady=20, font='Helvetica 18 bold', bd=5)
    menu.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    emailLbl = tk.Label(menu, text="Email:", justify='left', fg='#ffc107',
                        font='Helvetica 16 bold', bg='#607b8d')
    emailLbl.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)
    emailText = tk.StringVar()
    emailField = tk.Entry(menu, textvariable=emailText,
                          width=30, font='Helvetica 16')
    emailField.grid(column=1, row=0, padx=5, pady=5)
    emailField.focus()

    passwordLbl = tk.Label(menu, text="Password:", fg='#ffc107',
                           font='Helvetica 16 bold', bg='#607b8d')
    passwordLbl.grid(column=0, row=1, padx=5, pady=5, sticky=tk.W)

    passwordTxt = tk.StringVar()
    passwordField = tk.Entry(
        menu, textvariable=passwordTxt, show="*", width=30,  font='Helvetica 16')
    passwordField.grid(column=1, row=1, padx=5, pady=5)

    loginBtn = tk.Button(menu, text="Login",
                         bg='blue', fg='#ffc107',
                         font='Helvetica 15 bold', width=5, height=2, command=lambda: student_login_handler(emailText.get(), passwordTxt.get()))
    loginBtn.grid(column=1, row=3, padx=5, sticky=tk.W, pady=10)
    cancelBtn = tk.Button(menu,
                          bg='red', fg='white',
                          font='Helvetica 15 bold',
                          text="Back", height=2, command=show_student_authentication_menu)
    cancelBtn.grid(column=1, row=3, sticky=tk.E, padx=5, pady=10)


def student_login_handler(email, password):
    if is_email_existed(email) is False:
        messagebox.showerror(
            "Error", "Your email not exists, please try again or register new account.")
    else:
        validated_result = validate_student_account(email, password)
        is_login_successfully = validated_result['account_valid']
        student_data = validated_result['student']
        if is_login_successfully == False:
            messagebox.showerror(
                "Error", "Incorrect password, please try again.")

        else:
            messagebox.showinfo("Log In", "Successfully logged in")
            student = Student(
                student_data['name'],
                student_data['email'],
                student_data['password'],
                student_data['student_id'],
                student_data['enrollment_list']
            )
            show_student_main_system(student)


def show_student_register():
    clear_window(root)
    menu = tk.LabelFrame(root, text='Register', bg='#607b8d',
                         fg='white', padx=20, pady=20, font='Helvetica 18 bold', bd=5)
    menu.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    row_existing = 0

    # Email
    emailLbl = tk.Label(menu, text="Email:", justify='left', fg='#ffc107',
                        font='Helvetica 16 bold', bg='#607b8d')
    emailLbl.grid(column=0, row=row_existing, padx=5, pady=5, sticky=tk.W)
    emailText = tk.StringVar()
    emailField = tk.Entry(menu, textvariable=emailText,
                          width=30, font='Helvetica 16')
    emailField.grid(column=1, row=row_existing, padx=5, pady=5)
    emailField.focus()
    row_existing += 1

    # Password
    passwordLbl = tk.Label(menu, text="Password:", fg='#ffc107',
                           font='Helvetica 16 bold', bg='#607b8d')
    passwordLbl.grid(column=0, row=row_existing, padx=5, pady=5, sticky=tk.W)
    passwordTxt = tk.StringVar()
    passwordField = tk.Entry(
        menu, textvariable=passwordTxt, show="*", width=30, font='Helvetica 16')
    passwordField.grid(column=1, row=row_existing, padx=5, pady=5)
    row_existing += 1

    # Confirm Password
    confirmPasswordLbl = tk.Label(menu, text="Confirm Password:", fg='#ffc107',
                                  font='Helvetica 16 bold', bg='#607b8d')
    confirmPasswordLbl.grid(column=0, row=row_existing,
                            padx=5, pady=5, sticky=tk.W)
    confirmPasswordTxt = tk.StringVar()
    confirmPasswordField = tk.Entry(
        menu, textvariable=confirmPasswordTxt, show="*", width=30, font='Helvetica 16')
    confirmPasswordField.grid(column=1, row=row_existing, padx=5, pady=5)
    row_existing += 1

    # Name
    nameLbl = tk.Label(menu, text="Name:", justify='left', fg='#ffc107',
                       font='Helvetica 16 bold', bg='#607b8d')
    nameLbl.grid(column=0, row=row_existing, padx=5, pady=5, sticky=tk.W)
    nameText = tk.StringVar()
    nameField = tk.Entry(menu, textvariable=nameText,
                         width=30, font='Helvetica 16')
    nameField.grid(column=1, row=row_existing, padx=5, pady=5)
    row_existing += 1

    # Register Button
    registerBtn = tk.Button(menu, text="Register",
                            bg='blue', fg='#ffc107',
                            font='Helvetica 15 bold', width=8, height=2, command=lambda: student_register_handler(emailText.get(), passwordTxt.get(), confirmPasswordTxt.get(), nameText.get()))
    registerBtn.grid(column=0, row=row_existing, padx=5, sticky=tk.W, pady=10)

    # Cancel Button
    cancelBtn = tk.Button(menu,
                          bg='red', fg='white',
                          font='Helvetica 15 bold',
                          text="Back", height=2, command=show_main_menu)
    cancelBtn.grid(column=1, row=row_existing, padx=5, sticky=tk.E, pady=10)


def student_register_handler(email, password, confirm_password, name):
    error_messages = []
    if is_email_existed(email) is True:
        error_messages.append(
            "Email already exists")
    if password != confirm_password:
        error_messages.append("Password and confirm password are unmatched")
    if is_valid_password(password) is False:
        error_messages.append(
            "Something went wrong with your password, please re-enter, make sure your password is correctly formatted")
    if validate_email(email) is False:
        error_messages.append(
            "Something went wrong with your email, please re-enter, make sure your email is correctly formatted")
    if len(error_messages) > 0:
        messagebox.showerror("Error", "\n\n".join(error_messages))
        return

    student_data = post_student_register(email, password, name)

    messagebox.showinfo("Register", "Successfully register")
    student = Student(
        student_data['name'],
        student_data['email'],
        student_data['password'],
        student_data['student_id'],
        student_data['enrollment_list']
    )
    show_student_main_system(student)


def show_student_main_system(student: Student):
    clear_window(root)
    menu = tk.Frame(root)
    menu.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    menu_label(menu, "STUDENT MENU")
    information_label(menu, f"Welcome {student.name}")
    information_label(menu, "Please choose your options")
    option_button(menu, "Change password",
                  lambda: show_change_password_screen(student))
    option_button(menu, "Enrol in subject", lambda: enroll_subjects(student))
    option_button(menu, "Remove a subject",
                  lambda: remove_subject_by_id(student))
    option_button(menu, "Show enrolled subject",
                  lambda: view_enrollment_list(student))

    exit_button(menu, "Back to Main Menu", show_main_menu)


def show_change_password_screen(student: Student):
    clear_window(root)
    menu = tk.LabelFrame(root, text='Change Password', bg='#607b8d',
                         fg='white', padx=20, pady=20, font='Helvetica 18 bold', bd=5)
    menu.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # New Password
    newPasswordLbl = tk.Label(menu, text="New Password:", fg='#ffc107',
                              font='Helvetica 16 bold', bg='#607b8d')
    newPasswordLbl.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)
    newPasswordTxt = tk.StringVar()
    newPasswordField = tk.Entry(
        menu, textvariable=newPasswordTxt, show="*", width=30, font='Helvetica 16')
    newPasswordField.grid(column=1, row=0, padx=5, pady=5)
    newPasswordField.focus()

    # Confirm New Password
    confirmNewPasswordLbl = tk.Label(menu, text="Confirm New Password:", fg='#ffc107',
                                     font='Helvetica 16 bold', bg='#607b8d')
    confirmNewPasswordLbl.grid(column=0, row=1, padx=5, pady=5, sticky=tk.W)
    confirmNewPasswordTxt = tk.StringVar()
    confirmNewPasswordField = tk.Entry(
        menu, textvariable=confirmNewPasswordTxt, show="*", width=30, font='Helvetica 16')
    confirmNewPasswordField.grid(column=1, row=1, padx=5, pady=5)

    # Change Password Button
    changePasswordBtn = tk.Button(menu, text="Change Password",
                                  bg='blue', fg='#ffc107',
                                  font='Helvetica 15 bold', width=15, height=2, command=lambda: change_password_handler(newPasswordTxt.get(), confirmNewPasswordTxt.get(), student))
    changePasswordBtn.grid(column=1, row=2, padx=5, sticky=tk.W, pady=10)

    # Cancel Button
    cancelBtn = tk.Button(menu,
                          bg='red', fg='white',
                          font='Helvetica 15 bold',
                          text="Back", height=2, command=show_student_authentication_menu)
    cancelBtn.grid(column=1, row=2, sticky=tk.E, padx=5, pady=10)


def change_password_handler(new_password, confirm_new_password, student: Student):
    error_messages = []
    if is_valid_password(new_password) is False:
        error_messages.append("Invalid new password, please try again.")
    if new_password != confirm_new_password:
        error_messages.append("Password and confirm password are unmatched")
    if len(error_messages) > 0:
        messagebox.showerror("Error", "\n\n".join(error_messages))
        return
    student.password = generate_hash_password(new_password)

    messagebox.showinfo("Change password", "Successfully change password")
    student.database.update_data_to_file(
        'student.data', student.read_student_information())
    show_student_main_system(student)


def enroll_subjects(student: Student):
    max_courses = 4
    available_subject = [
        Subject("001", "Math"),
        Subject("002", "Science"),
        Subject("003", "History"),
        Subject("004", "Art"),
        Subject("005", "Physics"),
        Subject("006", "Chemistry"),
        Subject("007", "English"),
        Subject("008", "Programming"),
    ]

    if len(student.enrollment_list) >= max_courses:
        messagebox.showerror(
            "Error", "You have already registered for the maximum number of subjects.")
        return

    success_message = []

    while len(student.enrollment_list) < max_courses:
        select_subject = random.choice(
            available_subject).read_subject_detail()

        if not any(subject['subject_id'] == select_subject['subject_id'] for subject in student.enrollment_list):
            mark = random.randint(25, 100)  # Randomly generate scores
            grade = student.get_grade(mark)  # Get ratings based on scores
            student.enrollment_list.append({
                "subject_id": select_subject["subject_id"],
                "subject_name": select_subject["subject_name"],
                "mark": mark,
                "grade": grade
            })
            success_message.append(f"Registered subject {select_subject['subject_name']} ({
                select_subject['subject_id']}) with mark {mark} and grade {grade}.")

    messagebox.showinfo(
        "Enrol subject", "\n".join(success_message))

    # Update the new data to the file
    student.database.update_data_to_file(
        'student.data', student.read_student_information())


def view_enrollment_list(student: Student):
    clear_window(root)
    screen = tk.Frame(root)
    screen.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    headers = [[
        "Subject ID", "Subject Name", "Mark", 'Grade']]

    if len(student.enrollment_list) == 0:
        tk.Label(screen, text="You have not registered for any courses", padx=20,
                 pady=20, font='Helvetica 16 bold').grid()
        button = tk.Button(screen, text="Back to Student System", bg='red', fg='white',
                       font='Helvetica 14', command=lambda: show_student_main_system(student), height=2)
        button.grid(column=2, columnspan=2, pady=(20, 20))
        return

    tk.Label(screen, text="ENROLLED SUBJECT:", padx=20,
             pady=20, font='Helvetica 16 bold').grid(row=0, column=1, columnspan=2)
    table(screen, [[enrollment['subject_id'],  enrollment['subject_name'],  enrollment['mark'], enrollment['grade']]
                   for enrollment in student.enrollment_list], headers, 1)
    button = tk.Button(screen, text="Back to Student System", bg='red', fg='white',
                       font='Helvetica 14', command=lambda: show_student_main_system(student), height=2)

    button.grid(column=2, columnspan=2, pady=(20, 20))


def remove_subject_by_id(student: Student):
    row_existing = 0
    clear_window(root)
    screen = tk.Frame(root)
    screen.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    headers = [["Subject Id", "Subject Name", "Mark", "Grade"]]
    if (len(student.enrollment_list) > 0):
        label = tk.Label(screen, text="ENROLLED SUBJECT:", padx=20, pady=20,
                         font='Helvetica 16 bold')
        row_existing += 1
        label.grid(row=0, column=1, columnspan=3, pady=(20, 20))
        table(screen, [[enrollment['subject_id'],  enrollment['subject_name'],  enrollment['mark'], enrollment['grade']]
                       for enrollment in student.enrollment_list], headers, 1)
        row_existing += len([[enrollment['subject_id'],  enrollment['subject_name'],  enrollment['mark'], enrollment['grade']]
                             for enrollment in student.enrollment_list] + headers)
        subjectIdLabel = tk.Label(screen, text="Enter subject id to remove:", justify='left', fg='#ffc107',
                                  font='Helvetica 12 bold', bg='#607b8d',)
        subjectIdLabel.grid(column=1, row=row_existing,
                            padx=5, pady=20, columnspan=2)

        subjectIdText = tk.StringVar()
        subjectIdField = tk.Entry(screen, textvariable=subjectIdText)
        subjectIdField.grid(column=3, row=row_existing, padx=5, pady=20)
        subjectIdField.focus()
        row_existing += 1
        tk.Button(screen, text="Remove",
                  bg='#252525', fg='#ffc107',
                  font='Helvetica 10 bold', command=lambda: remove_subject_event_handler(subjectIdField.get(), student)).grid(column=1, row=row_existing, padx=5, pady=5, sticky=tk.E, columnspan=2)
        row_existing += 1

    else:
        tk.Label(screen, text="You have not registered for any courses.", padx=20, pady=20,
                 font='Helvetica 16 bold', fg="red").grid(column=3)

    button = tk.Button(screen, text="Back to Student System", bg='red', fg='white',
                       font='Helvetica 14', command=lambda: show_student_main_system(student), height=2)
    button.grid(column=2, columnspan=2, pady=(20, 20))


def remove_subject_event_handler(subject_id, student: Student):
    enrollment_record_found = False
    for enrollment_record in student.enrollment_list:
        if enrollment_record['subject_id'] == subject_id:
            student.enrollment_list.remove(enrollment_record)
            enrollment_record_found = True
            messagebox.showinfo("Remove subject",
                                f"Subject {subject_id}-{enrollment_record['subject_name']} deleted successfully from enrollment list.")
            student.database.update_data_to_file(
                'student.data', student.read_student_information())  # Update data
            show_student_main_system(student)

    if not enrollment_record_found:
        messagebox.showerror("Error", "Subject ID not found.")


def clear_database():
    database = Database()
    if messagebox.askyesno("Exit", "Are you sure you want to clear system database?"):
        database.clear_file('student.data')
        messagebox.showinfo("Clear Database", "Database Cleared")


def view_all_students():
    database = Database()
    clear_window(root)
    screen = tk.Frame(root)
    screen.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    studentList = database.read_file_and_convert_to_list('student.data')
    headers = [["Student Id", "Student Name", "Email"]]
    student_data = [[student['student_id'],  student['name'],  student['email']]
                    for student in studentList]
    label = tk.Label(screen, text="STUDENT DATA", padx=20, pady=20,
                     font='Helvetica 16 bold')
    label.grid(row=0, column=1, columnspan=3, pady=(20, 20))
    if (len(student_data) > 0):
        table(screen, student_data, headers, 1)
    else:
        tk.Label(screen, text="NOTHING TO SHOW", padx=20, pady=20,
                 font='Helvetica 16 bold').grid(column=3)

    button = tk.Button(screen, text="Back to Admin System", bg='red', fg='white',
                       font='Helvetica 14', command=show_admin_menu, height=2)
    button.grid(column=1, columnspan=3, pady=(20, 20))


def get_students_by_grade():
    database = Database()
    clear_window(root)
    # Creating Canvas and Scrollbar
    screen_canvas = tk.Canvas(root, width=1100, height=700)
    screen_canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    # screen_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    
    scrollbar = tk.Scrollbar(root, orient="vertical", command=screen_canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Place the Frame in the Canvas
    screen = tk.Frame(screen_canvas)
    screen_canvas.create_window((0, 0), window=screen, anchor="n")
    screen_canvas.configure(yscrollcommand=scrollbar.set)
    
    # Update the scrollregion of the Canvas
    def configure_canvas(event):
        screen_canvas.configure(scrollregion=screen_canvas.bbox("all"))
    screen.bind("<Configure>", configure_canvas)
    
    row_existing = 0

    studentList = database.read_file_and_convert_to_list('student.data')

    student_enrolled = [
        student for student in studentList if len(student['enrollment_list']) > 0]

    z_mark_student = []
    p_mark_student = []
    c_mark_student = []
    d_mark_student = []
    hd_mark_student = []

    for student in student_enrolled:
        for enrollment_record in student['enrollment_list']:
            student_record_with_enrollment_details = [
                student['student_id'], student['name'], student['email'], enrollment_record['subject_name'], enrollment_record['mark'], enrollment_record['grade']]
            if enrollment_record['grade'] == 'Z':
                z_mark_student.append(student_record_with_enrollment_details)
            elif enrollment_record['grade'] == 'P':
                p_mark_student.append(student_record_with_enrollment_details)
            elif enrollment_record['grade'] == 'C':
                c_mark_student.append(student_record_with_enrollment_details)
            elif enrollment_record['grade'] == 'D':
                d_mark_student.append(student_record_with_enrollment_details)
            elif enrollment_record['grade'] == 'HD':
                hd_mark_student.append(student_record_with_enrollment_details)

    headers = [["Student Id", "Student Name",
                "Student Email", "Subject Name", "Mark", 'Grade']]

    tk.Label(screen, text="STUDENT DATA WITH GRADE", padx=20, pady=20,
             font='Helvetica 16 bold').grid(row=row_existing, column=math.floor(len(headers[0])/2-1), columnspan=4, pady=(20, 20))
    row_existing += 1

    tk.Label(screen, text="Z GRADE:", pady=20,
             font='Helvetica 16 bold').grid(row=row_existing, column=0, columnspan=2)
    row_existing += 1

    if (len(z_mark_student) > 0):
        table(screen, z_mark_student, headers, row_existing)
        row_existing += len(z_mark_student + headers)
    else:
        tk.Label(screen, text="NOTHING TO SHOW", padx=20, pady=20,
                 font='Helvetica 16 bold').grid(column=3)
        row_existing += 1

    tk.Label(screen, text="P GRADE:", padx=20, pady=20,
             font='Helvetica 16 bold').grid(row=row_existing, column=0, columnspan=2)
    row_existing += 1

    if (len(p_mark_student) > 0):
        table(screen, p_mark_student, headers, row_existing)
        row_existing += len(p_mark_student + headers)
    else:
        tk.Label(screen, text="NOTHING TO SHOW", padx=20, pady=20,
                 font='Helvetica 16 bold').grid(column=3)
        row_existing += 1

    tk.Label(screen, text="C GRADE:", padx=20, pady=20,
             font='Helvetica 16 bold').grid(row=row_existing, column=0, columnspan=2)
    row_existing += 1

    if (len(c_mark_student) > 0):
        table(screen, c_mark_student, headers, row_existing)
        row_existing += len(c_mark_student + headers)
    else:
        tk.Label(screen, text="NOTHING TO SHOW", padx=20, pady=20,
                 font='Helvetica 16 bold').grid(column=3)
        row_existing += 1

    tk.Label(screen, text="D GRADE:", padx=20, pady=20,
             font='Helvetica 16 bold').grid(row=row_existing, column=0, columnspan=2)
    row_existing += 1

    if (len(d_mark_student) > 0):
        table(screen, d_mark_student, headers, row_existing)
        row_existing += len(d_mark_student + headers)
    else:
        tk.Label(screen, text="NOTHING TO SHOW", padx=20, pady=20,
                 font='Helvetica 16 bold').grid(column=3)
        row_existing += 1

    tk.Label(screen, text="HD GRADE:", padx=20, pady=20,
             font='Helvetica 16 bold').grid(row=row_existing, column=0, columnspan=2)
    row_existing += 1

    if (len(hd_mark_student) > 0):
        table(screen, hd_mark_student, headers, row_existing)
        row_existing += len(hd_mark_student + headers)
    else:
        tk.Label(screen, text="NOTHING TO SHOW", padx=20, pady=20,
                 font='Helvetica 16 bold').grid(column=3)
        row_existing += 1

    button = tk.Button(screen, text="Back to Admin System", bg='red', fg='white',
                       font='Helvetica 14', command=show_admin_menu, height=2)
    button.grid(column=math.floor(
        len(headers[0])/2), columnspan=2, pady=(20, 20))


def categorize_students():
    database = Database()
    clear_window(root)
  # Creating Canvas and Scrollbar
    screen_canvas = tk.Canvas(root, width=1100, height=700)
    screen_canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    # screen_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    
    scrollbar = tk.Scrollbar(root, orient="vertical", command=screen_canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Place the Frame in the Canvas
    screen = tk.Frame(screen_canvas)
    screen_canvas.create_window((0, 0), window=screen, anchor="n")
    screen_canvas.configure(yscrollcommand=scrollbar.set)
    
    # Update the scrollregion of the Canvas
    def configure_canvas(event):
        screen_canvas.configure(scrollregion=screen_canvas.bbox("all"))
    screen.bind("<Configure>", configure_canvas)
    
    row_existing = 0

    studentList = database.read_file_and_convert_to_list('student.data')

    student_enrolled = [
        student for student in studentList if len(student['enrollment_list']) > 0]

    fail_students = []
    pass_students = []

    for student in student_enrolled:
        for enrollment_record in student['enrollment_list']:
            student_record_with_enrollment_details = [
                student['student_id'], student['name'], student['email'], enrollment_record['subject_name'], enrollment_record['mark'], enrollment_record['grade']]
            if enrollment_record['mark'] >= 50:
                pass_students.append(student_record_with_enrollment_details)
            else:
                fail_students.append(student_record_with_enrollment_details)

    headers = [["Student Id", "Student Name",
                "Student Email", "Subject Name", "Mark", 'Grade']]

    tk.Label(screen, text="CATEGORIZE STUDENT", padx=20, pady=20,
             font='Helvetica 16 bold').grid(row=row_existing, column=math.floor(len(headers[0])/2-1), columnspan=4, pady=(20, 20))
    row_existing += 1

    tk.Label(screen, text="PASS STUDENT:", pady=20,
             font='Helvetica 16 bold', fg='green').grid(row=row_existing, column=1, columnspan=2)
    row_existing += 1

    if (len(pass_students) > 0):
        table(screen, pass_students, headers, row_existing)
        row_existing += len(pass_students + headers)
    else:
        tk.Label(screen, text="NOTHING TO SHOW", padx=20, pady=20,
                 font='Helvetica 16 bold').grid(column=3)
        row_existing += 1

    tk.Label(screen, text="FAIL STUDENT:", padx=20, pady=20,
             font='Helvetica 16 bold', fg='red').grid(row=row_existing, column=1, columnspan=2)
    row_existing += 1

    if (len(fail_students) > 0):
        table(screen, fail_students, headers, row_existing)
        row_existing += len(fail_students + headers)
    else:
        tk.Label(screen, text="NOTHING TO SHOW", padx=20, pady=20,
                 font='Helvetica 16 bold').grid(column=3)
        row_existing += 1

    button = tk.Button(screen, text="Back to Admin System", bg='red', fg='white',
                       font='Helvetica 14', command=show_admin_menu, height=2)
    button.grid(column=math.floor(
        len(headers[0])/2), columnspan=2, pady=(20, 20))


def remove_student_by_id():
    database = Database()
    row_existing = 0
    clear_window(root)
    screen = tk.Frame(root)
    screen.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    studentList = database.read_file_and_convert_to_list('student.data')
    headers = [["Student Id", "Student Name", "Email"]]
    student_data = [[student['student_id'],  student['name'],  student['email']]
                    for student in studentList]
    label = tk.Label(screen, text="LIST STUDENT:", padx=20, pady=20,
                     font='Helvetica 16 bold')
    row_existing += 1
    label.grid(row=0, column=1, columnspan=3, pady=(20, 20))
    if (len(student_data) > 0):
        table(screen, student_data, headers, 1)
        row_existing += len(student_data + headers)
        studentIdLabel = tk.Label(screen, text="Enter student id to remove:", justify='left', fg='#ffc107',
                                  font='Helvetica 12 bold', bg='#607b8d',)
        studentIdLabel.grid(column=1, row=row_existing,
                            padx=5, pady=20, columnspan=2)

        studentIdText = tk.StringVar()
        studentIdField = tk.Entry(screen, textvariable=studentIdText)
        studentIdField.grid(column=3, row=row_existing, padx=5, pady=20)
        studentIdField.focus()
        row_existing += 1
        tk.Button(screen, text="Remove",
                  bg='#252525', fg='#ffc107',
                  font='Helvetica 10 bold', command=lambda: remove_student_event_handler(studentIdText.get(), studentList, database)).grid(column=1, row=row_existing, padx=5, pady=5, sticky=tk.E, columnspan=2)
        row_existing += 1

    else:
        tk.Label(screen, text="NOTHING TO SHOW", padx=20, pady=20,
                 font='Helvetica 16 bold').grid(column=3)

    button = tk.Button(screen, text="Back to Admin System", bg='red', fg='white',
                       font='Helvetica 14', command=show_admin_menu, height=2)
    button.grid(column=1, columnspan=3, pady=(20, 20))


def remove_student_event_handler(student_id, studentList, database: Database):

    if any(student['student_id'] == student_id for student in studentList):
        database.remove_data_from_file('student.data', student_id)
        messagebox.showinfo(
            "Remove student", f"Student {
                student_id} have been removed from the system."
        )
        show_admin_menu()

    else:
        messagebox.showerror(
            "Error", "This student_id does not exist. Please check again.")
    return True


root = tk.Tk()
root.title("University System Menu")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
# root.attributes('-fullscreen', True)
# root.configure(bg='steel blue')
show_main_menu()
root.mainloop()
