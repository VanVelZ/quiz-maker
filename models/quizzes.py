class Quizzes:

    def __init__(self, quizzes_id=0, name="", course_id=0):
        self.quizzes_id = quizzes_id
        self.name = name
        self.course_id = course_id

    def json(self):
        return {
            'quizzesId': self.quizzes_id,
            'name': self.name,
            'courseId': self.course_id,

        }

    @staticmethod
    def json_parse(json):
        quizzes = Quizzes()
        quizzes.quizzes_id = json["quizzesId"]
        quizzes.name = json["name"]
        quizzes.course_id = json["courseId"]

        return quizzes
