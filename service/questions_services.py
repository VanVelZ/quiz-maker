from daos.daos_impl.questions_dao_impl import QuestionsDAOImpl


class QuestionsService:
    questions_dao = QuestionsDAOImpl()

    @classmethod
    def get_all_questions(cls):
        return cls.questions_dao.get_all_questions()