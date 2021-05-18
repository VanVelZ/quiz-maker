import unittest
from models.questions import Questions
from daos.questions_dao import QuestionsDAO
from daos.daos_impl.questions_dao_impl import QuestionDaoImpl

from models.quizzes import Quizzes
from daos.quizzes_dao import QuizesDAO
from daos.daos_impl.quizzes_dao_impl import QuizzesDaoImpl


question_dao = QuestionDaoImpl()
quizzes_dao = QuizzesDaoImpl()


test_question = Questions(1, 1, 'What is the speed of light?')
test_question2 = Questions(0, 'What is a test')
test_quiz = Quizzes(1, 'Light Quiz', 1)


class QuestionsTest(unittest.TestCase):

    def test_get_all_questions_for_quiz(self):
        retrieved_question = question_dao.get_all_questions_for_quiz(
            test_quiz.id)
        assert all(retrieved_question)

    def test_create_question(self):
        new_question = question_dao.create_question(
            test_question2, test_quiz.id)
        assert new_question == True
