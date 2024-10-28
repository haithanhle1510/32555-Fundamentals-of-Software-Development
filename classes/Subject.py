class Subject:
    def __init__(self, subject_id, subject_name):
        self.subject_id = subject_id
        self.subject_name = subject_name

    def read_subject_detail(self):
        return {
            'subject_id': self.subject_id,
            'subject_name': self.subject_name,
        }
