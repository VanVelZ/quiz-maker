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
            'questions': self._convert_questions_to_json()
        }

    @staticmethod
    def json_parse(json):
        quizzes = Quizzes()
        quizzes.id = json["quizzesId"]
        quizzes.name = json["name"]

        return quizzes

    def _convert_questions_to_json(self):
        question_as_json = []
        for question in self.questions:
            question_as_json.append(question.json())
        return question_as_json