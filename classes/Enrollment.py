class Enrollment:
    def __init__(self, enrollment_id:int, student:str, subject, score:int):
        self.enrollment_id = enrollment_id
        self.student = student
        self.subject = subject
        self.score = score
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.score >= 85:
            return 'HD'  # High Distinction
        elif self.score >= 75:
            return 'D'   # Distinction
        elif self.score >= 65:
            return 'C'   # Credit
        elif self.score >= 50:
            return 'P'   # Pass
        else:
            return 'F'   # Fail

    def enrol_subjects(self, subject):
        self.subject = subject

    def remove_subject_enrollment(self):
        self.subject = None

    def get_enrollment_info(self):
        return {
            'enrollment_id': self.enrollment_id,
            'student': self.student,
            'subject': self.subject,
            'score': self.score,
            'grade': self.grade
        }

if __name__ == "__main__":
    student = {'name': 'John Doe', 'id': '123456'}
    subject = {'name': 'Data Analytics', 'id': '101'}
    enrollment = Enrollment('E001', student, subject, 88)
    print(enrollment.get_enrollment_info())
