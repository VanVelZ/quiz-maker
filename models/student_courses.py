class StudentCourses:

    def __init__(self, student_id=0, course_id=0):
        self.student_id = student_id
        self.course_id = course_id

    def json(self):
        return {
            'studentId': self.student_id,
            'courseId': self.course_id,
        }

    @staticmethod
    def json_parse(json):
        student_courses = StudentCourses()
        student_courses.student_id = json["studentId"]
        student_courses.course_id = json["courseId"]

        return student_courses
