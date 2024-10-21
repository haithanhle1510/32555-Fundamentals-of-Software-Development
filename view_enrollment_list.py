

# Show registered courses function
def display_courses(student_name):
    existing_courses = students[student_name]['courses']
    if not existing_courses:
        print("You have not registered for any courses.")
        return
    
    print("Registered courses:")
    for course_id, (score, grade) in existing_courses.items():
        print(f"Course ID: {course_id}, Score: {score}, Grade: {grade}")

