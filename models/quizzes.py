from models.questions import Questions


class Quizzes:

    def __init__(self, id=0, name="", course_id=0, questions=None, grade=None):
        if questions is None:
            self.questions = []
        else:
            self.questions = questions
        self.id = id
        self.name = name
        self.course_id = course_id
        self.grade = grade

    def json(self):
        return {
            'quizzesId': self.id,
            'name': self.name,
            'courseId': self.course_id,
            'questions': self._convert_questions_to_json(),
            'grade': self.grade
        }

    @staticmethod
    def json_parse(json):
        quizzes = Quizzes()
        quizzes.id = json["id"]
        quizzes.name = json["name"]
        quizzes.course_id = json["courseId"]
        quizzes.questions = map(Questions.json_parse, json["questions"])

        return quizzes

    def _convert_questions_to_json(self):
        question_as_json = []
        for question in self.questions:
            question_as_json.append(question.json())
        return question_as_json

    
    def get_quiz_grade(self):
        amount_correct = 0
        for question in self.questions:
            if question.students_answer is None:
                self.grade = None
                return
            if question.students_answer:
                amount_correct += 1
        self.grade = amount_correct / len(self.questions) * 100