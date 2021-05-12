class Quizzes:

    def __init__(self, id=0, name="", course_id=0, questions=None):
        if questions is None:
            self.questions = []
        else:
            self.questions = questions
        self.id = id
        self.name = name
        self.course_id = course_id

    def json(self):
        return {
            'quizzesId': self.id,
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
