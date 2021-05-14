from daos.daos_impl.answers_dao_impl import AnswersDAOImpl


class AnswersServices:
    answers_dao = AnswersDAOImpl()

    @classmethod
    def get_all_answers(cls):
        return cls.answers_dao.get_all_answers()