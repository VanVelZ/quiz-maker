class Questions:

    def __init__(self, questions_id=0, quiz_id=0, description=""):
        self.questions_id = questions_id
        self.quiz_id = quiz_id
        self.description = description

    def json(self):
        return {
            'questionsId': self.questions_id,
            'quizId': self.quiz_id,
            'description': self.description,

        }

    @staticmethod
    def json_parse(json):
        questions = Questions()
        questions.questions_id = json["questionsId"]
        questions.quiz_id = json["quizId"]
        questions.description = json["description"]

        return questions
