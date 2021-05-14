from daos.daos_impl.quizzes_dao_impl import QuizzesDao


class QuizesServices:
    quizes_dao = QuizzesDao()

    @classmethod
    def create_quizes(cls):
        return cls.quizes_dao.create_quiz()

    @classmethod
    def get_all_quizes(cls):
        return cls.quizes_dao.get_quiz()

    @classmethod
    def get_quizes_by(cls, course_id):
        return cls.quizes_dao.get_all_quizzes_for_course(course_id)

