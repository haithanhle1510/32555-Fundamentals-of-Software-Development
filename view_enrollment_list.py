from utils.file_operation import read_file_and_convert_to_list, update_data_to_file

# Show registered courses function
def display_courses(student_id):
    studentList = read_file_and_convert_to_list('student.data')
    
    for idx in range(len(studentList)):
        if studentList[idx]['student_id'] == student_id:
            if 'enrollment_list' not in studentList[idx]:
                studentList[idx]['enrollment_list'] = []
            
            existing_courses = studentList[idx]['enrollment_list']
            break
        
        
    if not existing_courses:
        print("You have not registered for any courses.")
        return
    
    print("Registered courses:")
    for course in existing_courses:
        print(f"course name: {course['course_name']}, Course ID: {course['course_id']}, Score: {course['score']}, Grade: {course['grade']}")
