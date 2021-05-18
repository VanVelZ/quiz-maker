class Answers:

    def __init__(self, id=0, description="", is_correct=True):
        self.id = id
        self.description = description
        self.is_correct = is_correct

    def json(self):
        return {
            'id': self.id,
            'description': self.description,
            'isCorrect': self.is_correct,

        }

    @staticmethod
    def json_parse(json):
        answers = Answers()
        answers.id = json["id"] if "id" else None
        answers.description = json["description"]
        answers.is_correct = json["isCorrect"]

        return answers
