class Courses:

    def __init__(self, courses_id=0, name="", teacher_id=0):
        self.courses_id = courses_id
        self.name = name
        self.teacher_id = teacher_id

    def json(self):
        return {
            'coursesId': self.courses_id,
            'name': self.name,
            'teacherId': self.teacher_id,

        }

    @staticmethod
    def json_parse(json):
        courses = Courses()
        courses.courses_id = json["coursesId"]
        courses.name = json["name"]
        courses.teacher_id = json["teacherId"]

        return courses
