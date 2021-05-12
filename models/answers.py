class Answers:

    def __init__(self, answers_id=0, description="", question_id=0, is_correct=True):
        self.answers_id = answers_id
        self.description = description
        self.question_id = question_id
        self.is_correct = is_correct

    def json(self):
        return {
            'answersId': self.answers_id,
            'description': self.description,
            'questionId': self.question_id,
            'isCorrect': self.is_correct,

        }

    @staticmethod
    def json_parse(json):
        answers = Answers()
        answers.answers_id = json["answersId"]
        answers.description = json["description"]
        answers.question_id = json["questionId"]
        answers.is_correct = json["isCorrect"]

        return answers
