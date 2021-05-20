import unittest
from models.quizzes import Quizzes
from daos.quizzes_dao import QuizesDAO
from daos.daos_impl.quizzes_dao_impl import QuizzesDaoImpl

quizzes_dao = QuizzesDaoImpl()

test_quiz = Quizzes(1, 'Light Quiz', 1)
test_quiz2 = Quizzes(0, 'TEST QUIZ', 0)


class QuizzesTest(unittest.TestCase):

    def test_get_all_quizzes_for_course(self):
        retrieved_quiz = quizzes_dao.get_all_quizzes_for_course(
            test_quiz.course_id)
        assert all(retrieved_quiz)

    def test_get_quiz(self):
        retrieved_quiz = quizzes_dao.get_quiz(test_quiz.id)
        assert test_quiz.name == retrieved_quiz.name

    def test_create_quiz(self):
        new_quiz = quizzes_dao.create_quiz(test_quiz2)
        assert new_quiz == True
