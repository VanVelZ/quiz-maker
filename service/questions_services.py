from daos.daos_impl.questions_dao_impl import QuestionDAOImpl


class QuestionsServices:
    questions_dao = QuestionDAOImpl()

    @classmethod
    def get_all_questions_by_id(cls, quiz_id):
        return cls.questions_dao.get_all_questions_for_quiz(quiz_id)