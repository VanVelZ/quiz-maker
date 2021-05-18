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
            'id': self.id,
            'description': self.description,
            'answers': self._convert_answers_to_json(),
            'studentsAnswer': self.students_answer.json() if self.students_answer else None
        }

    @staticmethod
    def json_parse(json):
        questions = Questions()
        questions.id = json["id"] if json["id"] else None
        questions.description = json["description"]
        questions.answers = map(Answers.json_parse, json["answers"])
        try:
            questions.students_answer = json["studentsAnswer"]
        except KeyError:
            questions.students_answer = None
        return questions

    def _convert_answers_to_json(self):
        answers_as_json = []
        for answer in self.answers:
            answers_as_json.append(answer.json())
        return answers_as_json

