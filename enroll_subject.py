import random
import json


# Randomly generate course ID
def generate_course_id(existing_ids):
    while True:
        course_id = str(random.randint(1, 999)).zfill(3)  # Convert to string and fill with 3 digits
        if course_id not in existing_ids:
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
    existing_courses = students[student_id]['courses']
    
    if len(existing_courses) >= max_courses:
        print("You have already registered for the maximum number of courses.")
        return
    
    while len(existing_courses) < max_courses:
        course_id = generate_course_id(existing_courses.keys())
        score = random.randint(25, 100)  # Randomly generate scores
        grade = get_grade(score)  # Get ratings based on scores
        existing_courses[course_id] = (score, grade)  # Recording scores and ratings
        print(f"Registered course {course_id} with score {score} and grade {grade}.")
        
     