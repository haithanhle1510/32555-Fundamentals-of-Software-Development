
        
# Delete course feature
def delete_course(student_name):
    existing_courses = students[student_name]['courses']
    
    if not existing_courses:
        print("You have no registered courses to delete.")
        return

    # Show enrolled courses
    print("Your registered courses are:")
    for course_id, (score, grade) in existing_courses.items():
        print(f"Course ID: {course_id}, Score: {score}, Grade: {grade}")

    
   # Debug information, check if the course ID exists
    print(f"Available course IDs: {list(existing_courses.keys())}")  # Print an existing course ID
    
    course_id = input("Enter the course ID to delete: ").strip()  # Remove leading and trailing spaces
    
    # Check if the course ID exists
    if course_id in existing_courses:
        del existing_courses[course_id]
        print(f"Course {course_id} deleted successfully.")
        save_student_data()  # Save data after update
    else:
        print("Course ID not found.")