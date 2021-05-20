import unittest
from unittest.mock import MagicMock
from models.quizzes import Quizzes
from daos.quizzes_dao import QuizesDAO
from daos.daos_impl.quizzes_dao_impl import QuizzesDaoImpl
from service.quiz_service import QuizService

quiz1 = Quizzes(1, 'Light Quiz', 1)
quiz2 = Quizzes(0, 'TEST QUIZ', 0)

quizzes = [quiz1, quiz2]

mock_quiz_dao = QuizzesDaoImpl()
mock_quiz_dao.get_all_quizzes_for_course = MagicMock(
    return_value=quizzes)
quiz_service = QuizService()


class QuizzesTest(unittest.TestCase):

    def test_service_get_all_quizzes_for_course(self):
        retrieved_quiz = quiz_service.get_all_quizzes_for_course(
            quiz1.course_id)
        assert all(retrieved_quiz)

    def test_service_get_quiz(self):
        retrieved_quiz = quiz_service.get_quiz(quiz1.id)
        print(retrieved_quiz)
        assert all(retrieved_quiz)

    def test_service_create_quiz(self):
        new_quiz = quiz_service.create_quiz(quiz2)
        assert new_quiz == True
