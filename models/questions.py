class Questions:

    def __init__(self, id=0, description="", answers=None):
        if answers is None:
            answers = []
        else:
            answers = answers
        self.id = id
        self.description = description

    def json(self):
        return {
            'questionsId': self.id,
            'description': self.description,

        }

    @staticmethod
    def json_parse(json):
        questions = Questions()
        questions.id = json["questionsId"]
        questions.description = json["description"]

        return questions
