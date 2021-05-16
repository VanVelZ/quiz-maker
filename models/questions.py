from models.answers import Answers


class Questions:

    def __init__(self, id=0, description="", answers=None, students_answer=None):
        if answers is None:
            self.answers = []
        else:
            self.answers = answers
        self.id = id
        self.description = description
        self.students_answer = students_answer

    def json(self):
        return {
            'questionsId': self.id,
            'description': self.description,
            'answers': self._convert_answers_to_json(),
            'studentAnswer': self.students_answer
        }

    @staticmethod
    def json_parse(json):
        questions = Questions()
        questions.id = json["questionsId"]
        questions.description = json["description"]
        questions.answers = map(Answers.json_parse, json["answers"])
        questions.students_answer = json["studentAnswer"]
        return questions

    def _convert_answers_to_json(self):
        answers_as_json = []
        for answer in self.answers:
            answers_as_json.append(answer.json())
        return answers_as_json

