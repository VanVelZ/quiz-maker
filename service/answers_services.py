from daos.daos_impl.answers_dao_impl import AnswersDaoImpl


class AnswersServices:
    answers_dao = AnswersDaoImpl()

    @classmethod
    def get_all_answers(cls):
        return cls.answers_dao.get_all_answers()
