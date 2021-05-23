import unittest

from models.student_questions import StudentQuestions
from daos.student_questions_dao import StudentQuestionsDAO
from daos.daos_impl.student_questions_dao_impl import StudentQuestionsDAOImpl

student_question_dao = StudentQuestionsDAOImpl()


class StudentQuestionTest(unittest.TestCase):

    def test_get_all_questions(self):
        student_question = student_question_dao.get_all_questions()
        assert all(student_question)
