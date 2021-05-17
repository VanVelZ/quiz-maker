from daos.daos_impl.quizzes_dao_impl import QuizzesDAOImpl
from models.quizzes import Quizzes


class QuizService:
    quizzes_dao = QuizzesDAOImpl()
    @staticmethod
    def get_all_quizzes_for_course(course_id):
        quizzes = QuizzesDAOImpl.get_all_quizzes_for_course(course_id)
        quizzes_as_json = []
        for quiz in quizzes:
            quizzes_as_json.append(quiz.json())
        return quizzes_as_json

    @staticmethod
    def create_quiz(quiz: Quizzes):
        return QuizService.create_quiz(quiz)
