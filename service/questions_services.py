from daos.daos_impl.questions_dao_impl import QuestionDaoImpl


class QuestionsServices:
    questions_dao = QuestionDaoImpl()

    @classmethod
    def get_all_questions(cls):
        return cls.questions_dao.get_all_questions()