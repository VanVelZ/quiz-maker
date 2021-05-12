class StudentQuestions:

    def __init__(self, student_questions_id=0, student_id=0, question_id=0, answer_id=0):
        self.student_questions_id = student_questions_id
        self.student_id = student_id
        self.question_id = question_id
        self.answer_id = answer_id

    def json(self):
        return {
            'studentQuestionsId': self.student_questions_id,
            'studentId': self.student_id,
            'questionId': self.question_id,
            'answerId': self.answer_id,
        }

    @staticmethod
    def json_parse(json):
        student_questions = StudentQuestions()
        student_questions.student_questions_id = json["studentQuestionsId"]
        student_questions.student_id = json["studentId"]
        student_questions.question_id = json["questionId"]
        student_questions.answer_id = json["answerId"]

        return student_questions
