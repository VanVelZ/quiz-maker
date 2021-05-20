import unittest
from unittest.mock import MagicMock

from models.questions import Questions
from daos.questions_dao import QuestionsDAO
from daos.daos_impl.questions_dao_impl import QuestionDaoImpl
from service.questions_services import QuestionsServices

from models.quizzes import Quizzes
from daos.quizzes_dao import QuizesDAO
from daos.daos_impl.quizzes_dao_impl import QuizzesDaoImpl
from service.quiz_service import QuizService

question = Questions(1, 1, 'What is the speed of light?')
question2 = Questions(0, 'What is a test')
questions = [question, question2]
quiz = Quizzes(1, 'Light Quiz', 1)


mock_question_dao = QuestionDaoImpl()
mock_question_dao.get_all_questions_for_quiz = MagicMock(
    return_value=questions)
mock_quizzes_dao = QuizzesDaoImpl()
mock_quizzes_dao.get_quiz = MagicMock(return_value=quiz)

questions_service = QuestionsServices()


class QuestionsTest(unittest.TestCase):

    def test_service_get_all_questions_for_quiz(self):
        retrieved_question = questions_service.get_all_questions(quiz.id)
        assert all(retrieved_question)
