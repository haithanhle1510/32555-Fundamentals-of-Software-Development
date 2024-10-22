import random
import json
from utils.file_operation import read_file_and_convert_to_list, update_data_to_file
#Use a collection to store existing course IDs
existing_ids = set()

# Randomly generate course ID
def generate_course_id():
    while True:
        course_id = str(random.randint(1, 999)).zfill(3)  # Convert to string and fill with 3 digits
        if course_id not in existing_ids:
            existing_ids.add(course_id) #Add a new ID to the collection
            return course_id

# Generate ratings based on scores
def get_grade(score):
    if score < 50:
        return 'Z'
    elif 50 <= score < 65:
        return 'P'
    elif 65 <= score < 75:
        return 'C'
    elif 75 <= score < 85:
        return 'D'
    else:
        return 'HD'
    
    
    # Course registration function
def register_courses(student_id):
    max_courses = 4
    studentList = read_file_and_convert_to_list('student.data')
    available_courses = [
        {"course_name": "Math", "course_id": generate_course_id()},
        {"course_name": "Science", "course_id": generate_course_id()},
        {"course_name": "History", "course_id": generate_course_id()},
        {"course_name": "Art", "course_id": generate_course_id()},
        {"course_name": "Physics", "course_id": generate_course_id()},
        {"course_name": "Chemistry", "course_id": generate_course_id()},
        {"course_name": "English", "course_id": generate_course_id()},
        {"course_name": "Programming", "course_id": generate_course_id()}
    ]
    
   

    for idx in range(len(studentList)):
        if studentList[idx]['student_id'] == student_id:
            if 'enrollment_list' not in studentList[idx]:
                studentList[idx]['enrollment_list'] = []
            
            existing_courses = studentList[idx]['enrollment_list']
            break
    
    if len(existing_courses) >= max_courses:
        print("You have already registered for the maximum number of courses.")
        return
    
    while len(existing_courses) < max_courses:
        select_course = random.choice(available_courses)
        
        if not any(course['course_id'] == select_course['course_id'] for course in existing_courses):
            score = random.randint(25, 100)  # Randomly generate scores
            grade = get_grade(score)  # Get ratings based on scores
            existing_courses.append({
                    "course_name": select_course["course_name"],
                    "course_id": select_course["course_id"],
                    "score": score,
                    "grade": grade
                })
            print(f"Registered course {select_course['course_name']} ({select_course['course_id']}) with score {score} and grade {grade}.")
            
    # Update the new data to the file
    update_data_to_file('student.data', studentList)
     