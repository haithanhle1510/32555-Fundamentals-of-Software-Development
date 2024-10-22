from utils.file_operation import read_file_and_convert_to_list, update_data_to_file
        
# Delete course feature
def delete_course(student_id):
    studentList = read_file_and_convert_to_list('student.data')
    for idx in range(len(studentList)):
        if studentList[idx]['student_id'] == student_id:
            if 'enrollment_list' not in studentList[idx]:
                studentList[idx]['enrollment_list'] = []
            
            existing_courses = studentList[idx]['enrollment_list']
            break

    
    if not existing_courses:
        print("You have no registered courses to delete.")
        return

    # Show enrolled courses
    print("Your registered courses are:")
    for course in existing_courses:
        print(f"course name: {course['course_name']}, Course ID: {course['course_id']}, Score: {course['score']}, Grade: {course['grade']}")

    
   # Debug information, check if the course ID exists
    print(f"Available course IDs: {[course['course_id'] for course in existing_courses]}")  # Print an existing course ID
    
    course_id = input("Enter the course ID to delete: ").strip()  # Remove leading and trailing spaces
    
    # Check if the course ID exists
    for course in existing_courses:
        if course['course_id'] == course_id:
            existing_courses.remove(course)  # Delete the matching course
            course_found = True
            print(f"Course {course_id} deleted successfully.")
            update_data_to_file('student.data', studentList)  # Update data
            break  # Exit the loop after deletion

    if not course_found:
        print("Course ID not found.")