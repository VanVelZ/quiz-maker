from daos.daos_impl.answers_dao_impl import AnswersDAOImpl


class AnswersServices:
    answers_dao = AnswersDAOImpl()

    @classmethod
    def create_answers(cls,answer,question_id):
        return cls.answers_dao.create_answer(answer,question_id)

    @classmethod
    def get_all_answers_by_questionID(cls,question_id):
        return cls.answers_dao.get_all_answers_for_question(question_id)

    @classmethod
    def get_answers_by_answerID(cls, answer_id):
        return cls.answers_dao.get_answer(answer_id)

    @classmethod
    def get_students_answer(cls, question_id, student_id):
        return cls.answers_dao.get_students_answer(question_id, student_id)
