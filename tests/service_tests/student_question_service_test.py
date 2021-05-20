import unittest
from unittest.mock import MagicMock

from models.student_questions import StudentQuestions
from daos.student_questions_dao import StudentQuestionsDAO
from daos.daos_impl.student_questions_dao_impl import StudentQuestionsDAOImpl
from service.student_questions_services import StudentQuestionsServices

student_question1 = StudentQuestions(1, 0, 1, 1)
student_question2 = StudentQuestions(2, 1, 1, 1)
student_questions = [student_question1, student_question2]


mock_student_question_dao = StudentQuestionsDAOImpl()
mock_student_question_dao.get_all_questions = MagicMock(
    return_value=student_questions)
student_question_service = StudentQuestionsServices()


class StudentQuestionService(unittest.TestCase):

    def test_service_get_all_questions(self):
        student_question = student_question_service.get_all_student_questions()
        assert all(student_question)
