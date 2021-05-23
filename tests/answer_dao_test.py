import unittest
from models.answers import Answers
from daos.answers_dao import AnswersDAO
from daos.daos_impl.answers_dao_impl import AnswersDaoImpl

from models.questions import Questions
from daos.questions_dao import QuestionsDAO
from daos.daos_impl.questions_dao_impl import QuestionDaoImpl


answer_dao = AnswersDaoImpl()
question_dao = QuestionDaoImpl()

test_answer = Answers(0, 'Test answer', False)
test_question = Questions(1, 1, 'What is the speed of light?')


class AnswerTest(unittest.TestCase):

    def test_get_all_answers_for_question(self):
        retrieved_answer = answer_dao.get_all_answers_for_question(
            test_question.id)
        assert all(retrieved_answer)

    def test_create_answer(self):
        new_answer = answer_dao.create_answer(
            test_answer, test_question.id, False)
        assert new_answer == True


if __name__ == "__main__":
    unittest.main()
